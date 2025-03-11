import unittest
from random import choices, randint
from string import ascii_letters, digits

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_type_eq(self):
        types = [TextType.BOLD, TextType.NORMAL, TextType.CODE, TextType.IMAGE, TextType.LINK, TextType.ITALIC]
        for type in types:
            self.assertEqual(TextNode("Test", type), TextNode("Test", type))
    
    def test_url_neq(self):
        node = TextNode("This is a text node", TextType.NORMAL)
        node_url = TextNode("This is a text node", TextType.NORMAL, url="https://google.com")
        self.assertNotEqual(node, node_url)
    
    def test_type_neq(self):
        types = [TextType.BOLD, TextType.NORMAL, TextType.CODE, TextType.IMAGE, TextType.LINK, TextType.ITALIC]
        for k in range(len(types) - 1):
            type = types[k]
            for other_type in types[k+1:]:
                self.assertNotEqual(TextNode("Test", type), TextNode("Test", other_type))

    def test_text(self):
        letters = ascii_letters + digits
        
        for strlen in range(1000):
            text1 = "".join(choices(letters, k=strlen))
            text2 = "".join(choices(letters, k=strlen))
            if text1 == text2:
                self.assertEqual(TextNode(text1, TextType.NORMAL), TextNode(text2, TextType.NORMAL))
            else:
                self.assertNotEqual(TextNode(text1, TextType.NORMAL), TextNode(text2, TextType.NORMAL))
        


if __name__ == "__main__":
    unittest.main()