class HTMLNode():
    def __init__(self, tag: str = None, value: str = None, children: list = None, props: dict = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        return "".join(list( 
            map(lambda item: f' {item[0]}="{item[1]}"', self.props.items()) 
            )) if self.props != None else ""

    def __repr__(self):
        return f"HTMLNode(\ntag = {self.tag}\nvalue = {self.value}\nchildren = {self.children}\nprops = {self.props}\n)"