from Tag_Params_List import Tag_Params_List
from Children_List import Children_List
from tools.add_indents import Formater


class Html_Tag:


    def __init__(self, tag, id=None):
        self.tag = tag
        self.id = id
        self.tag_params_list = Tag_Params_List()
        self.text = ''
        self.children = Children_List()
        self.fromater = Formater()


    def text_value(self):

        if not self.children.is_empty() and not self.text:
            for child in self.children:
                self.text = self.text + f'\n{child.html()}'
            self.text += '\n'

        return self.text


    def html(self):

        tag_params = self.tag_params_list.params_string()

        tag_start = f'<{self.tag}{tag_params}>'
        tag_end = f'</{self.tag}>'

        return f'{tag_start}{self.text_value()}{tag_end}'


    def format_html(self):
        return self.fromater.format_indents(self.html())


    def add_child(self, htmlTarget):
        self.children.add_child(htmlTarget)
        return htmlTarget


    def add_class(self, class_name):
        self.tag_params_list.add_class(class_name)


    def placeholder(self, text):
        self.tag_params_list.add_placeholder(text)


    def add_href(self, url):
        self.tag_params_list.add_href(url)


    def add_src(self, src):
        self.tag_params_list.add_src(src)


    def add_rel(self, rel):
        self.tag_params_list.add_rel(rel)


    def add_integrity(self, integrity):
        self.tag_params_list.add_integrity(integrity)


    def add_crossorigin(self, crossorigin):
        self.tag_params_list.add_crossorigin(crossorigin)


    def head(self, id=None):
        return self.children.child("head", id=id)


    def h1(self, text="", id=None):
        return self.children.child("h1", text=text, id=id)


    def h2(self, text="", id=None):
        return self.children.child("h2", text=text, id=id)


    def p(self, text="", id=None):
        return self.children.child("p", id=id, text=text)


    def body(self, id=None):
        return self.children.child("body", id=id)


    def div(self, id=None):
        return self.children.child("div", id=id)


    def title(self, page_title="", id=None):
        return self.children.child("title", title_text=page_title, id=id)


    def script(self, id=None):
        return self.children.child("script", id=id)


    def link(self, id=None):
        return self.children.child("link", id=id)


    def a(self, text='', url='#', id=None):
        return self.children.child("a", id=id, text=text, url=url)


    def form(self, id=None):
        return self.children.child("form", id=id)


    def label(self, text='', id=None):
        return self.children.child("label", text=text, id=id)


    def input(self, id=None):
        return self.children.child("input", id=id)


    def textarea(self, id=None):
        return self.children.child("textarea", id=id)


    def button(self, text, id=None):
        return self.children.child("button", id=id, on_click_text=text)