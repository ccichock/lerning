from Html_Tag import Html_Tag


class Default_Html(Html_Tag):

    def __init__(self, page_title):
        super().__init__('html')

        self.head().link().bootstrap_link()
        self.head().title(page_title)
        self.body().script().bootstrap_script()