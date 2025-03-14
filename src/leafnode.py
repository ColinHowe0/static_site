from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag: str, value: str, props: dict = None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value == None:
            raise ValueError("LeafNode has no value specified")
        return f'<{self.tag + self.props_to_html()}>{self.value}</{self.tag}>' if self.tag != None else self.value
    