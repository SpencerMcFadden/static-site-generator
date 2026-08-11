import re

from textnode import TextNode, TextType


def split_nodes_delimiter(
    old_nodes: list[TextNode], delimiter: str, text_type: TextType
) -> list[TextNode]:
    results = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            results.append(node)
            continue
        splits = []
        sections = node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invald markdown")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                splits.append(TextNode(sections[i], TextType.TEXT))
            else:
                splits.append(TextNode(sections[i], text_type))
        results.extend(splits)
    return results


def extract_markdown_images(text: str) -> list[tuple[str, str]]:
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(pattern, text)


def extract_markdown_links(text: str) -> list[tuple[str, str]]:
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(pattern, text)


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    results = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            results.append(node)
            continue
        text = node.text
        images_info = extract_markdown_images(text)
        if not images_info:
            results.append(node)
            continue
        for image in images_info:
            image_alt = image[0]
            image_link = image[1]
            sections = text.split(f"![{image_alt}]({image_link})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, image section not closed")
            if sections[0]:
                results.append(TextNode(sections[0], TextType.TEXT))
            results.append(TextNode(image_alt, TextType.IMAGE, image_link))
            text = sections[1]
        if text != "":
            results.append(TextNode(text, TextType.TEXT))
    return results


def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    results = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            results.append(node)
            continue
        text = node.text
        link_info = extract_markdown_links(text)
        if not link_info:
            results.append(node)
            continue
        for link in link_info:
            link_text = link[0]
            link_url = link[1]
            sections = text.split(f"[{link_text}]({link_url})", 1)
            if sections[0]:
                results.append(TextNode(sections[0], TextType.TEXT))
            results.append(TextNode(link_text, TextType.LINK, link_url))
            text = sections[1]
        if text != "":
            results.append(TextNode(sections[1], TextType.TEXT))
    return results


def text_to_textnodes(text: str) -> list[TextNode]:
    result_list = [TextNode(text, TextType.TEXT)]
    result_list = split_nodes_delimiter(result_list, "**", TextType.BOLD)
    result_list = split_nodes_delimiter(result_list, "_", TextType.ITALIC)
    result_list = split_nodes_delimiter(result_list, "`", TextType.CODE)
    result_list = split_nodes_image(result_list)
    result_list = split_nodes_link(result_list)
    return result_list
