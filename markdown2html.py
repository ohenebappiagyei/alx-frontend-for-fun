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
    for line in markdown_lines:
        if line.startswith('-') or line.startswith('*'):
            if not in_list:
                html_lines.append("<ul>\n")
                in_list = True
            html_lines.append(parse_markdown_unordered_list(line))
        elif line.startswith('#'):
            if in_list:

                html_lines.append("</ul>\n")
                in_list = False
            html_lines.append(parse_markdown_heading(line))
        else:
            if in_list:
                html_lines.append("</ul>\n")
                in_list = False
            html_lines.append(markdown.markdown(line))

        # Close list if it's still open
        if in_list:
            html_lines.append("</ul>\n")

    # Writing the HTML content to the output file
    with open(output_file, 'w') as f:
        f.writelines(html_lines)

    sys.exit(0)


if __name__ == "__main__":
    main()
