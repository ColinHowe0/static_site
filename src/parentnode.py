from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list, props: dict = None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag == None:
            raise ValueError("Tag is None")
        if self.children == None:
            raise ValueError("Children is None")
        if len(self.children) == 0:
            return f'<{self.tag}></{self.tag}>'
        
        return "".join(list(
            map(lambda child: f'<{self.tag + self.props_to_html()}>{child.to_html()}</{self.tag}>', self.children)
        )) 