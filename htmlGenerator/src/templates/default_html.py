from HtmlTag import Html_Tag, title, h1, body, script, head

class defalut_html(Html_Tag):

    def __init__(self, page_title):
        super().__init__('html')

        self.add_child(head())
        self.head().add_child(title(page_title))
        self.add_child(body())


class simple_html(Html_Tag):

    def __init__(self, page_title):
        super().__init__('html')

        self.head().link().bootstrap_link()
        self.head().title(page_title)
        self.head().h1("Hello World")
        self.head().h1().add_class("text-light m-2 p-3 bg-dark text-center")
        self.body().add_class("bg-secondary")
        self.body().div().button("Submit")
        self.body().div().add_class("container")
        self.body().div().button("Submit").add_class("btn btn-dark")

        self.body().script().bootstrap_script()
        