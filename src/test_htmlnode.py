import unittest
from htmlnode import HTMLNode, LeafNode


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


if __name__ == "__main__":
    unittest.main()
