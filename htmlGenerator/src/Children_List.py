

class Children_List:

    def __init__(self):
        self.children = []


    def __iter__(self):
        return self.children.__iter__()


    def is_empty(self):
        return not self.children


    def add_child(self, htmlTarget):
        self.children.append(htmlTarget)
        return htmlTarget


    def find_child_by_tag(self, tag):
        child = [child for child in self.children if child.tag == tag]
        if child:
            return child[0]
        return None


    def create_new_tag(self, tag, **kwargs):
        from Html_Tags import head, title, link, a, div, h1, button, script, body, p, form, textarea #to do remove import circle dependency
        if tag == "head":
            return self.add_child(head())
        elif tag == "title":
            return self.add_child(title(kwargs["title_text"]))
        elif tag == "body":
            return self.add_child(body())
        elif tag == "link":
            return self.add_child(link())
        elif tag == "a":
            return self.add_child(a(kwargs["text"], kwargs["url"]))
        elif tag == "div":
            return self.add_child(div())
        elif tag == "h1":
            return self.add_child(h1(kwargs["text"]))
        elif tag == "h2":
            return self.add_child(h2(kwargs["text"]))
        elif tag == "p":
            return self.add_child(p(kwargs["text"]))
        elif tag == "form":
            return self.add_child(form())
        elif tag == "textarea":
            return self.add_child(textarea())
        elif tag == "button":
            return self.add_child(button(kwargs["on_click_text"]))
        elif tag == "script":
            return self.add_child(script())
        else:
            return None


    def child(self, tag, **kwargs):
        html_tag = self.find_child_by_tag(tag)
        if not html_tag:
            html_tag = self.create_new_tag(tag, **kwargs)

        return html_tag