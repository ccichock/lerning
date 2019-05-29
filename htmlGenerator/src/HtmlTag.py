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


    def add_class(self, class_name):
        self.class_names.add_class(class_name)


    def head(self):
        head = self.find_child_by_tag('head')
        return head


    def body(self):
        body = self.find_child_by_tag('body')
        return body


    def div(self):
        div = self.find_child_by_tag('div')
        return div

        