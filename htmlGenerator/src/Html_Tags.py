from Html_Tag import Html_Tag


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


class p(Html_Tag):

    def __init__(self, text):
        super().__init__('p')
        self.text = text


class button(Html_Tag):

    def __init__(self, text):
        super().__init__('button')
        self.text = text


class a(Html_Tag):

    def __init__(self, text='', url='#'):
        super().__init__('a')
        self.text = text
        self.tag_params_list.add_href(url)


class form(Html_Tag):

    def __init__(self):
        super().__init__('form')


class textarea(Html_Tag):

    def __init__(self):
        super().__init__('textarea')


class script(Html_Tag):

    def __init__(self):
        super().__init__('script')
        self.src = ""
        self.integrity = ""
        self.crossorigin = ""


    def bootstrap_script(self):
        self.src = "https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"
        self.integrity = "sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM"
        self.crossorigin = crossorigin="anonymous"


    def html(self):

        if self.src and self.integrity and self.crossorigin:
            return f'<script src="{self.src}" integrity="{self.integrity}" crossorigin="{self.crossorigin}"></script>'
        else:
            return f'<script></script>'


class link(Html_Tag):

    def __init__(self):
        super().__init__('link')
        self.rel = ""
        self.href = ""
        self.integrity = ""
        self.crossorigin = ""


    def bootstrap_link(self):
        self.rel = "stylesheet"
        self.href = "https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
        self.integrity = "sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T"
        self.crossorigin = "anonymous"


    def html(self):
        return f'<link rel="{self.rel}" href="{self.href}" integrity="{self.integrity}" crossorigin="{self.crossorigin}">'