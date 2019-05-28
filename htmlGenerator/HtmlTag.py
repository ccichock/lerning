from Class_Name import Class_List


class Html_Tag:


    def __init__(self, tag):
        self.tag = tag
        self.class_names = Class_List()
        self.string_html = ''
        self.text = ''
        self.parent = None
        self.children = []


    def html(self):

        tag_start = f'<{self.tag} class="{self.class_names.to_string()}">'
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

        