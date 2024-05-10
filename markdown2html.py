#!/usr/bin/python3

import os
import sys
import markdown


def parse_markdown_heading(line):
    """Parse Markdown heading syntax and generate corresponding HTML."""
    # Count the number of '#' characters at the beginning of the line
    count = 0
    for char in line:
        if char == '#':
            count += 1
        else:
            break

    # Generate HTML heading tag based on the number of '#' characters
    if count > 6:  # Limit to heading levels 1 to 6
        count = 6
    return f"<h{count}>{line.strip('# ').strip()}</h{count}>\n"


def parse_markdown_unordered_list(line):
    """Parse Markdown unordered list syntax and generate corresponding HTML."""
    return f"<li>{line.strip('-* ').strip()}</li>\n"


def parse_markdown_ordered_list(line):
    """Parse Markdown ordered list syntax and generate corresponding HTML."""
    return f"<li>{line.strip('* ').strip()}</li>\n"


def main():
    """Converts a markdown file to HTML.

    This script takes two arguments:
        - markdown_file: The path to the markdown file.
        - output_file: The path to write the generated HTML.

    Raises:
        SystemExit: If there are less than two arguments,
        or the markdown file doesn't exist.
    """
    # Check if correct number of arguments provided
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py <markdown_file> <output_file>",
              file=sys.stderr)
        sys.exit(1)

    # Extract arguments
    markdown_file, output_file = sys.argv[1:]

    # Check if Markdown file exists
    if not os.path.exists(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)

    # Convert Markdown to HTML
    with open(markdown_file, 'r') as f:
        markdown_lines = f.readlines()

    html_lines = []
    in_list = False
    list_type = None
    in_paragraph = False

    for line in markdown_lines:
        if line.startswith('-') or line.startswith('*') or \
                (line[0].isdigit() and line[1] == '.'):
            # List item start
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
            if line.startswith('* '):  # Check for the space after the asterisk
                html_lines.append(parse_markdown_ordered_list(line))
            else:
                html_lines.append(parse_markdown_unordered_list(line))
        elif line.startswith('#'):
            # Heading
            if in_paragraph:
                html_lines.append("</p>\n")
                in_paragraph = False
            if in_list:
                # Close the previous list if it's open
                if list_type == 'unordered':
                    html_lines.append("</ul>\n")
                elif list_type == 'ordered':
                    html_lines.append("</ol>\n")
                in_list = False
                list_type = None
            html_lines.append(parse_markdown_heading(line))
        elif line.strip() == '':
            # Empty line, end of paragraph
            if in_paragraph:
                html_lines.append("</p>\n")
                in_paragraph = False
        else:
            # Paragraph
            if not in_paragraph:
                if in_list:
                    # Close the list if it's open before starting a paragraph
                    if list_type == 'unordered':
                        html_lines.append("</ul>\n")
                    elif list_type == 'ordered':
                        html_lines.append("</ol>\n")
                    in_list = False
                    list_type = None
                html_lines.append("<p>\n")
                in_paragraph = True
            html_lines.append(line.strip() + "\n")

            # Check if it's not the last line of the paragraph
            next_line_index = markdown_lines.index(line) + 1
            if next_line_index < len(markdown_lines) and markdown_lines[next_line_index].strip() != '':
                html_lines.append("<br/>\n")

            # Close any paragraph that might still be open at the end
            if in_paragraph:
                html_lines.append("</p>\n")

    # Writing the HTML content to the output file
    with open(output_file, 'w') as f:
        f.writelines(html_lines)

    sys.exit(0)


if __name__ == "__main__":
    main()
