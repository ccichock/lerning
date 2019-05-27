
from HtmlTag import HtmlTarget


class h1(HtmlTarget):

    def __init__(self, text):
        super().__init__('h1')
        self.text = text


class h2(HtmlTarget):

    def __init__(self, text):
        super().__init__('h2')
        self.text = text