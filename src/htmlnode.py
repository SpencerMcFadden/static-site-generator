class HTMLNode():
    def __init__(
            self, 
            tag: str | None = None, 
            value: str | None = None, 
            children: list["HTMLNode"] | None = None,
            props: dict[str, str] | None = None
    ) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self) -> str:
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self) -> str:
        if self.props is None:
            return ""
        tag_props = ""
        for prop in self.props:
            tag_props += f' {prop}="{self.props[prop]}"'
        return tag_props

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(
            self, tag: str | None, value: str, props: dict[str, str] | None = None
    ) -> None:
        super().__init__(tag, value, None, props)

    def to_html(self) -> str:
        if not self.value:
            raise ValueError("Leaf nodes must have a value")
        if self.tag:
            return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
        return self.value

    def __repr__(self) -> str:
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
