#!/usr/bin/python3

import os
import sys
import re


def parse_markdown_heading(line):
    """Parse Markdown heading syntax and generate corresponding HTML."""
    count = 0
    for char in line:
        if char == '#':
            count += 1
        else:
            break
    if count > 6:
        count = 6
    return f"<h{count}>{line.strip('# ').strip()}</h{count}>\n"


def parse_markdown_unordered_list(line):
    """Parse Markdown unordered list syntax and generate corresponding HTML."""
    return f"<li>{parse_bold_and_emphasis(line.strip('-* ').strip())}</li>\n"


def parse_markdown_ordered_list(line):
    """Parse Markdown ordered list syntax and generate corresponding HTML."""
    return f"<li>{parse_bold_and_emphasis(line.strip('* ').strip())}</li>\n"


def parse_bold_and_emphasis(text):
    """Parse bold and emphasis syntax and generate HTML."""
    text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)
    text = re.sub(r'__(.*?)__', r'<em>\1</em>', text)
    return text


def main():
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py <markdown_file> <output_file>", file=sys.stderr)
        sys.exit(1)

    markdown_file, output_file = sys.argv[1:]

    if not os.path.exists(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)

    with open(markdown_file, 'r') as f:
        markdown_lines = f.readlines()

    html_lines = []
    in_list = False
    list_type = None
    in_paragraph = False

    for line in markdown_lines:
        if line.startswith('-') or line.startswith('*') or \
                (line[0].isdigit() and line[1] == '.'):
            if in_paragraph:
                html_lines.append("</p>\n")
                in_paragraph = False
            if not in_list:
                if line.startswith('* ') or \
                        (line[0].isdigit() and line[1] == '.'):
                    html_lines.append("<ol>\n")
                    list_type = 'ordered'
                else:
                    html_lines.append("<ul>\n")
                    list_type = 'unordered'
                in_list = True
            if line.startswith('* '):
                html_lines.append(parse_markdown_ordered_list(line))
            else:
                html_lines.append(parse_markdown_unordered_list(line))
        elif line.startswith('#'):
            if in_paragraph:
                html_lines.append("</p>\n")
                in_paragraph = False
            if in_list:
                if list_type == 'unordered':
                    html_lines.append("</ul>\n")
                elif list_type == 'ordered':
                    html_lines.append("</ol>\n")
                in_list = False
                list_type = None
            html_lines.append(parse_markdown_heading(line))
        elif line.strip() == '':
            if in_paragraph:
                html_lines.append("</p>\n")
                in_paragraph = False
        else:
            if not in_paragraph:
                if in_list:
                    if list_type == 'unordered':
                        html_lines.append("</ul>\n")
                    elif list_type == 'ordered':
                        html_lines.append("</ol>\n")
                    in_list = False
                    list_type = None
                html_lines.append("<p>\n")
                in_paragraph = True
            line = parse_bold_and_emphasis(line.strip())
            html_lines.append(line)
            if '<br/>' in line:
                html_lines.append("</p>\n")
                in_paragraph = False
            else:
                html_lines.append("\n")

    if in_list:
        if list_type == 'unordered':
            html_lines.append("</ul>\n")
        elif list_type == 'ordered':
            html_lines.append("</ol>\n")
    if in_paragraph:
        html_lines.append("</p>\n")

    with open(output_file, 'w') as f:
        f.writelines(html_lines)

    sys.exit(0)


if __name__ == "__main__":
    main()
