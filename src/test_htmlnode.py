import unittest
from htmlnode import HTMLNode


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


if __name__ == "__main__":
    unittest.main()
