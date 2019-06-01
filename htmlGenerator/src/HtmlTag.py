from Class_Name import Class_List


class Html_Tag:


    def __init__(self, tag):
        self.tag = tag
        self.class_names = Class_List()
        self.string_html = ''
        self.text = ''
        self.parent = None
        self.children = []


    def find_child_by_tag(self, tag):
        child = [child for child in self.children if child.tag == tag]
        if child:
            return child[0]
        return None


    def class_string(self):
        class_string = ""

        if not self.class_names.is_empty():
            class_string = f' class="{self.class_names.to_string()}"'

        return class_string


    def html(self):

        tag_start = f'<{self.tag}{self.class_string()}>'
        tag_end = f'\n</{self.tag}>'

        value = ''
        if self.children:
            for child in self.children:
                value = value + f'\n{child.html()}'
        else:
            value = f'\n{self.text}'

        self.string_html = f'{tag_start}{value}{tag_end}'
        return self.string_html


    def add_child(self, htmlTarget):
        self.children.append(htmlTarget)
        return htmlTarget


    def add_class(self, class_name):
        self.class_names.add_class(class_name)


    def child(self, tag, *args):
        html_tag = self.find_child_by_tag(tag)
        if not html_tag:
            # if args:
            #     html_tag = self.add_child(Html_Tag(tag, args[0]))
            # else:
            if tag == "head":
                html_tag = self.add_child(head())
            elif tag == "title":
                if args:
                    html_tag = self.add_child(title(args[0]))
            elif tag == "link":
                html_tag = self.add_child(link())
            elif tag == "h1":
                if args:
                    html_tag = self.add_child(h1(args[0]))
            elif tag == "script":
                html_tag = self.add_child(script())
            else:
                html_tag = self.add_child(Html_Tag(tag))

        return html_tag


    def head(self):
        return self.child("head")


    def h1(self, text=""):
        return self.child("h1", text)


    def h2(self, text=""):
        h2 = self.find_child_by_tag('h2', text)
        return h2


    def body(self):
        return self.child("body")


    def div(self):
        return self.child("div")


    def title(self, page_title=""):
        return self.child("title", page_title)


    def script(self):
        return self.child("script")


    def link(self):
        return self.child("link")



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