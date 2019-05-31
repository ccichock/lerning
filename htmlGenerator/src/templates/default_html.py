
from generator import *
from HtmlTag import Html_Tag

class defalut_html(Html_Tag):

    def __init__(self, page_title):
        super().__init__('html')

        self.add_child(head())
        self.head().add_child(title(page_title))
        self.add_child(body())


class simple_html(Html_Tag):

    def __init__(self, page_title):
        super().__init__('html')

        self.add_child(head())
        self.head().add_child(link())
        self.head().link().bootstrap()
        self.head().add_child(title(page_title))
        self.head().add_child(h1("Hello World"))
        self.head().h1().add_class("text-center m-2 p-3 bg-secondary")
        self.add_child(body())
        self.body().add_child(script())
        self.body().script().bootstrap()