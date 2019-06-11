from Html_Tag import Html_Tag


class Search_Navbar_Html(Html_Tag):

    def __init__(self):
        super().__init__('nav')

        self.add_class('nav justify-content-end bg-dark p-1')
        self.form().input().add_class('form-control mr-sm-2')
        self.form().input().placeholder('Search')
        self.form().button('Search').add_class('btn btn-outline-success my-2 my-sm-0')

        self.form().add_class('form-inline my-2 my-lg-0')