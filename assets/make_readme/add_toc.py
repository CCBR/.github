import re
import argparse

def extract_headers(markdown_content):
    """
    Extract headers from the markdown content.
    """
    headers = re.findall(r'^(#{1,6})\s*(.*)', markdown_content, re.MULTILINE)
    return headers

def generate_toc(headers):
    """
    Generate the Table of Contents (TOC) from the headers.
    """
    toc_lines = ["## Table of Contents"]
    for header in headers:
        level = len(header[0])
        title = header[1].strip()
        anchor = title.lower().replace(' ', '-').replace('.', '')
        toc_lines.append(f"{'  ' * (level - 1)}- [{title}](#{anchor})")
    return '\n'.join(toc_lines)

def insert_toc(markdown_content, toc):
    """
    Insert TOC into the markdown content after the first header.
    """
    toc_placeholder = "<!-- TOC -->"
    if toc_placeholder in markdown_content:
        updated_content = markdown_content.replace(toc_placeholder, toc)
    else:
        first_header_pos = markdown_content.find('\n#')
        if first_header_pos == -1:
            first_header_pos = 0
        updated_content = markdown_content[:first_header_pos] + toc + '\n\n' + markdown_content[first_header_pos:]
    return updated_content

def main():
    parser = argparse.ArgumentParser(description='Add a Table of Contents (TOC) to a Markdown file.')
    parser.add_argument('--input', '-i', required=True, help='Input Markdown file')
    parser.add_argument('--output', '-o', required=True, help='Output Markdown file')
    
    args = parser.parse_args()

    with open(args.input, 'r') as f:
        markdown_content = f.read()

    headers = extract_headers(markdown_content)
    toc = generate_toc(headers)
    updated_content = insert_toc(markdown_content, toc)

    with open(args.output, 'w') as f:
        f.write(updated_content)

    print(f"TOC added to {args.output}")

if __name__ == "__main__":
    main()
