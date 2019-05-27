from Class_Name import Class_List


class HtmlTarget:


    def __init__(self, tag):
        self.tag = tag
        self.class_names = Class_List()
        self.string_html = ''
        self.text = ''
        self.parent = None
        self.children = []


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

        