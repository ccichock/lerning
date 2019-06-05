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
        super().add_href(url)
        self.text = text


class form(Html_Tag):

    def __init__(self):
        super().__init__('form')


class textarea(Html_Tag):

    def __init__(self):
        super().__init__('textarea')


class script(Html_Tag):

    def __init__(self):
        super().__init__('script')


    def bootstrap_script(self):
        super().add_src("https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js")
        super().add_integrity("sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM")
        super().add_crossorigin("anonymous")


class link(Html_Tag):

    def __init__(self):
        super().__init__('link')


    def bootstrap_link(self):
        super().add_rel("stylesheet")
        super().add_href("https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css")
        super().add_integrity("sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T")
        super().add_crossorigin("anonymous")


    def html(self):
        tag_params = self.tag_params_list.params_string()
        tag_start = f'<{self.tag}{tag_params}>'
        return f'{tag_start}{self.text_value()}'