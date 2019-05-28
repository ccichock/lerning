
from HtmlTag import Html_Tag


class html(Html_Tag):

    def __init__(self):
        super().__init__('html')


class body(Html_Tag):

    def __init__(self):
        super().__init__('body')


class head(Html_Tag):

    def __init__(self):
        super().__init__('head')


class title(Html_Tag):

    def __init__(self, text):
        super().__init__('title')
        self.text = text


class div(Html_Tag):

    def __init__(self):
        super().__init__('div')


class h1(Html_Tag):

    def __init__(self, text):
        super().__init__('h1')
        self.text = text


class h2(Html_Tag):

    def __init__(self, text):
        super().__init__('h2')
        self.text = text