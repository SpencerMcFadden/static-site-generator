import os

from blocks import markdown_to_html_node


def extract_title(markdown: str) -> str:
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line.strip("# ")
    raise ValueError("no title found")


def generate_page(from_path: str, template_path: str, dest_path: str) -> None:
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as file:
        content = file.read()
    with open(template_path, "r") as file:
        template_file = file.read()

    title = extract_title(content)
    content_as_html = markdown_to_html_node(content).to_html()

    template_file = template_file.replace("{{ Title }}", title).replace(
        "{{ Content }}", content_as_html
    )

    if not os.path.dirname(dest_path):
        os.makedirs(dest_path)
    with open(dest_path, "w") as stream:
        stream.write(template_file)
