from Html_Tag import Html_Tag


class html(Html_Tag):

    def __init__(self, id=None):
        super().__init__('html', id)


class body(Html_Tag):

    def __init__(self, id=None):
        super().__init__('body', id)


class head(Html_Tag):

    def __init__(self, id=None):
        super().__init__('head', id)


class title(Html_Tag):

    def __init__(self, text, id=None):
        super().__init__('title', id)
        self.text = text


class div(Html_Tag):

    def __init__(self, id=None):
        super().__init__('div', id)


class h1(Html_Tag):

    def __init__(self, text, id=None):
        super().__init__('h1', id)
        self.text = text


class h2(Html_Tag):

    def __init__(self, text, id=None):
        super().__init__('h2', id)
        self.text = text


class p(Html_Tag):

    def __init__(self, text, id=None):
        super().__init__('p', id)
        self.text = text


class button(Html_Tag):

    def __init__(self, text, id=None):
        super().__init__('button', id)
        self.text = text


class a(Html_Tag):

    def __init__(self, text='', url='#', id=None):
        super().__init__('a', id)
        super().add_href(url)
        self.text = text


class form(Html_Tag):

    def __init__(self, id=None):
        super().__init__('form', id)


class label(Html_Tag):

    def __init__(self, text='', id=None):
        super().__init__('label', id)
        self.text = text


class input_text(Html_Tag):

    def __init__(self, id=None):
        super().__init__('input', id)


    def html(self):
        tag_params = self.tag_params_list.params_string()
        tag_start = f'<{self.tag}{tag_params}>'
        return f'{tag_start}{self.text_value()}'


class textarea(Html_Tag):

    def __init__(self, id=None):
        super().__init__('textarea', id)


class script(Html_Tag):

    def __init__(self, id=None):
        super().__init__('script', id)


    def bootstrap_script(self):
        super().add_src("https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js")
        super().add_integrity("sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM")
        super().add_crossorigin("anonymous")


class link(Html_Tag):

    def __init__(self, id=None):
        super().__init__('link', id)


    def bootstrap_link(self):
        super().add_rel("stylesheet")
        super().add_href("https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css")
        super().add_integrity("sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T")
        super().add_crossorigin("anonymous")


    def html(self):
        tag_params = self.tag_params_list.params_string()
        tag_start = f'<{self.tag}{tag_params}>'
        return f'{tag_start}{self.text_value()}'