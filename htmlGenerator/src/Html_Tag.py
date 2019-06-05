from Tag_Params_List import Tag_Params_List
from Children_List import Children_List

class Html_Tag:


    def __init__(self, tag):
        self.tag = tag
        self.string_html = ''
        self.tag_params_list = Tag_Params_List()
        self.text = ''
        self.children = Children_List()

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


    def add_child(self, htmlTarget):
        self.children.add_child(htmlTarget)
        return htmlTarget


    def add_class(self, class_name):
        self.tag_params_list.add_class(class_name)


    def placeholder(self, text):
        self.tag_params_list.add_placeholder(text)


    def add_href(self, url):
        self.tag_params_list.add_href(url)


    def head(self):
        return self.children.child("head")


    def h1(self, text=""):
        return self.children.child("h1", text=text)


    def h2(self, text=""):
        return self.children.child("h2", text=text)


    def p(self, text=""):
        return self.children.child("p", text=text)


    def body(self):
        return self.children.child("body")


    def div(self):
        return self.children.child("div")


    def title(self, page_title=""):
        return self.children.child("title", title_text=page_title)


    def script(self):
        return self.children.child("script")


    def link(self):
        return self.children.child("link")


    def a(self, text, url):
        return self.children.child("a", text=text, url=url)


    def form(self):
        return self.children.child("form")


    def textarea(self):
        return self.children.child("textarea")


    def button(self, text):
        return self.children.child("button", on_click_text=text)