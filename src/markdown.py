from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
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

