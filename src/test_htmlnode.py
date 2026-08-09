import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(
            "p", 
            "This is an html node", 
            None, 
            { "href": "https://test.com", "target": "_blank" }
        )
        self.assertEqual(
            ' href="https://test.com" target="_blank"', 
            node.props_to_html()
        )

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_repr(self):
        node = HTMLNode(
            "p", 
            "This is an html node", 
            None, 
            { "href": "https://test.com" }
        )
        self.assertEqual(
            "HTMLNode(p, This is an html node, children: None, {'href': 'https://test.com'})", 
            repr(node)
        )

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Hello, world!", { "href": "https://test.com", "target": "_blank" })

        self.assertEqual(node.to_html(), '<a href="https://test.com" target="_blank">Hello, world!</a>')

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_leaf_repr(self):
        node = LeafNode(
            "p", 
            "This is an leaf node", 
            { "href": "https://test.com" }
        )
        self.assertEqual(
            "LeafNode(p, This is an leaf node, {'href': 'https://test.com'})", 
            repr(node)
        )

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")


    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_children_with_props(self):
        child_node = LeafNode("a", "child", { "href": "https://test.com", "target": "_blank" })
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), '<div><a href="https://test.com" target="_blank">child</a></div>')

    def test_to_html_with_grandchildren_with_props(self):
        grandchild_node = LeafNode("b", "grandchild", { "class": "grandchild" })
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            '<div><span><b class="grandchild">grandchild</b></span></div>',
        )

    def test_to_html_with_children_with_grandchildren(self):
        grandchild_node1 = LeafNode("a", "grandchild1")
        child_node1 = ParentNode("span", [grandchild_node1])
        grandchild_node2 = LeafNode("b", "grandchild2", { "class": "grandchild" })
        grandchild_node3 = LeafNode("a", "grandchild3", { "href": "https://test.com", "target": "_blank" })
        child_node2 = ParentNode("span", [grandchild_node2, grandchild_node3])
        parent_node = ParentNode("div", [child_node1, child_node2])
        self.assertEqual(
            parent_node.to_html(),
            '<div><span><a>grandchild1</a></span><span><b class="grandchild">grandchild2</b><a href="https://test.com" target="_blank">grandchild3</a></span></div>',
        )


if __name__ == "__main__":
    unittest.main()
