import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props(self):
        props_list = [
            {
                "href": "https://www.google.com",
                "target": "_blank",
            },
            {
                "src": "img_girl.jpg",
            },
            {

            }
        ]
        test_strings = [
            ' href="https://www.google.com" target="_blank"',
            ' src="img_girl.jpg"',
            ''
        ]
        for k in range(len(props_list)):
            node = HTMLNode(props = props_list[k])
            #print("Testing: ", node)
            self.assertEqual(node.props_to_html(), test_strings[k])