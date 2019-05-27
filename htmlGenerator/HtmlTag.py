from Class_Name import Class_List


class HtmlTarget:
    def __init__(self):
        self.tag = ''
        self.class_names = Class_List()
        self.string_html = ''
        self.text = ''
        self.parent = None
        self.children = []


    def create_html(self, tag, class_name='', text=''):
        self.tag = tag
        self.text = text
        if class_name:
            self.class_names.add_class(class_name)
        self.string_html = '<{} class="{}">\n{}\n</{}>'.format(tag, class_name, text, tag)
        return self.string_html


    def html(self):

        tag_start = '<{} class="{}">'.format(self.tag, self.class_names.to_string())
        tag_end = '\n</{}>'.format(self.tag)

        value = ''
        if self.children:
            for child in self.children:
                value = value + '\n{}'.format(child.html())
        else:
            value = '\n{}'.format(self.text)

        self.string_html = '{}{}{}'.format(tag_start, value, tag_end)
        return self.string_html


    def add_child(self, htmlTarget):
        self.children.append(htmlTarget)


    def add_class(self, class_name):
        self.class_names.add_class(class_name)

        