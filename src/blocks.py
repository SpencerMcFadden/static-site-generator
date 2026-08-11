from enum import Enum
from htmlnode import LeafNode, ParentNode
from markdown import text_to_textnodes
from textnode import TextNode, TextType, text_node_to_html_node


class BlockType(Enum):
    PARAGRAPH = ("paragraph",)
    HEADING = ("heading",)
    CODE = ("code",)
    QUOTE = ("quote",)
    ULIST = ("unordered_list",)
    OLIST = "ordered_list"


def markdown_to_blocks(markdown: str) -> list[str]:
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks


def block_to_block_type(markdown: str) -> BlockType:
    lines = markdown.split("\n")

    if markdown.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    if markdown.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if markdown.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.ULIST
    if markdown.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.OLIST
    return BlockType.PARAGRAPH


def markdown_to_html_node(markdown: str) -> ParentNode:
    nodes = []
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        nodes.append(block_to_html_node(block))
    return ParentNode("div", nodes, None)


def block_to_html_node(block: str) -> ParentNode:
    block_type = block_to_block_type(block)
    if block_type == BlockType.PARAGRAPH:
        return paragraph_to_html_node(block)
    if block_type == BlockType.QUOTE:
        return quote_to_html_node(block)
    if block_type == BlockType.HEADING:
        return heading_to_html_node(block)
    if block_type == BlockType.ULIST:
        return ulist_to_html_node(block)
    if block_type == BlockType.OLIST:
        return olist_to_html_node(block)
    if block_type == BlockType.CODE:
        return code_to_html_node(block)
    raise ValueError("invalid block type")


def text_to_children(text: str) -> list["LeafNode"]:
    textnodes = text_to_textnodes(text)
    leafnodes = []
    for node in textnodes:
        leafnodes.append(text_node_to_html_node(node))
    return leafnodes


def paragraph_to_html_node(block: str) -> ParentNode:
    children = text_to_children(" ".join(block.split("\n")))
    return ParentNode("p", children)


def quote_to_html_node(block: str) -> ParentNode:
    lines = block.split("\n")
    stripped_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("invalid quote block")
        stripped_lines.append(line[1:].strip())
    children = text_to_children(" ".join(stripped_lines))
    return ParentNode("blockquote", children)


def heading_to_html_node(block: str) -> ParentNode:
    index = block.index(" ")
    children = text_to_children(block[index + 1 :])
    return ParentNode(f"h{index}", children)


def ulist_to_html_node(block: str) -> ParentNode:
    children = []
    for line in block.split("\n"):
        children.append(ParentNode("li", text_to_children(line[2:])))
    return ParentNode("ul", children)


def olist_to_html_node(block: str) -> ParentNode:
    children = []
    for line in block.split("\n"):
        children.append(ParentNode("li", text_to_children(line.split(". ", 1)[1])))
    return ParentNode("ol", children)


def code_to_html_node(block: str) -> ParentNode:
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("invalid code block")
    child = text_node_to_html_node(TextNode(block[4:-3], TextType.TEXT))
    code = ParentNode("code", [child])
    return ParentNode("pre", [code])
