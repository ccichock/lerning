

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


    def child_match(self, child, tag, **kwargs):
        return child.tag == tag and child.id == kwargs["id"]


    def find_child(self, tag, **kwargs):
        child = [child for child in self.children if self.child_match(child, tag, **kwargs)]
        if child:
            return child[0]
        return None


    def create_new_tag(self, tag, **kwargs):
        from Html_Tags import head, title, link, a, div, h1, h2, button, script, body, p, form, textarea, label, input_text #to do remove import circle dependency
        try:
            if tag == "head":
                return self.add_child(head(kwargs["id"]))
            elif tag == "title":
                return self.add_child(title(kwargs["title_text"], kwargs["id"]))
            elif tag == "body":
                return self.add_child(body(kwargs["id"]))
            elif tag == "link":
                return self.add_child(link(kwargs["id"]))
            elif tag == "a":
                return self.add_child(a(kwargs["text"], kwargs["url"], kwargs["id"]))
            elif tag == "div":
                return self.add_child(div(kwargs["id"]))
            elif tag == "h1":
                return self.add_child(h1(kwargs["text"], kwargs["id"]))
            elif tag == "h2":
                return self.add_child(h2(kwargs["text"], kwargs["id"]))
            elif tag == "p":
                return self.add_child(p(kwargs["text"], kwargs["id"]))
            elif tag == "form":
                return self.add_child(form(kwargs["id"]))
            elif tag == "label":
                return self.add_child(label(kwargs["text"], kwargs["id"]))
            elif tag == "input":
                return self.add_child(input_text(kwargs["id"]))
            elif tag == "textarea":
                return self.add_child(textarea(kwargs["id"]))
            elif tag == "button":
                return self.add_child(button(kwargs["on_click_text"], kwargs["id"]))
            elif tag == "script":
                return self.add_child(script(kwargs["id"]))
            else:
                print(f'Unsupported tag: {tag}')
                return None
        except NameError:
            print(f'NameError on tag: {tag}')
        except KeyError:
            print(f'KeyError on tag: {tag}, kwargs = {kwargs}')

        return None



    def child(self, tag, **kwargs):
        html_tag = self.find_child(tag, **kwargs)
        if not html_tag:
            html_tag = self.create_new_tag(tag, **kwargs)

        return html_tag