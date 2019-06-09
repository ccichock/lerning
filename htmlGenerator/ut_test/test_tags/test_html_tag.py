import unittest
from Html_Tags import html, head, title, body, div
from templates.Default_Html import Default_Html
from tools.remove_tabs import remove_indentination


class Test_html(unittest.TestCase):


    def setUp(self):
        self.sut = html()


    def test_html(self):
        self.assertEqual(self.sut.html(), '<html></html>')


    def test_default_html(self):
        title_html = title("Page Title")
        head_html = head()
        head_html.add_child(title_html)

        body_html = body()

        self.sut.add_child(head_html)
        self.sut.add_child(body_html)

        expect = """<html>
                    <head>
                    <title>Page Title</title>
                    </head>
                    <body></body>
                    </html>"""

        self.assertEqual(self.sut.html(), remove_indentination(expect))


    def test_default_html_reverse(self):
        self.sut.add_child(head())
        self.sut.head().add_child(title("title"))
        self.sut.add_child(body())

        expect = """<html>
                    <head>
                    <title>title</title>
                    </head>
                    <body></body>
                    </html>"""

        self.assertEqual(self.sut.html(), remove_indentination(expect))


    def test_default_html_with_class(self):
        self.sut.add_child(head())
        self.sut.head().add_child(title("title"))
        self.sut.add_child(body())
        self.sut.body().add_class("p-5 m-2")
        self.sut.body().add_child(div())
        self.sut.body().div().add_class("container")

        expect = """<html>
                    <head>
                    <title>title</title>
                    </head>
                    <body class="p-5 m-2">
                    <div class="container"></div>
                    </body>
                    </html>"""

        self.assertEqual(self.sut.html(), remove_indentination(expect))


    def test_default_html_class(self):
        html = Default_Html("Page Title")

        link_rel="stylesheet" 
        link_href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" 
        link_integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" 
        link_crossorigin="anonymous"

        script_src = 'https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js'
        script_integrity = 'sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM'
        script_crossorigin = 'anonymous'

        expect = f"""<html>
                     <head>
                     <link rel="{link_rel}" href="{link_href}" integrity="{link_integrity}" crossorigin="{link_crossorigin}">
                     <title>Page Title</title>
                     </head>
                     <body>
                     <script src="{script_src}" integrity="{script_integrity}" crossorigin="{script_crossorigin}"></script>
                     </body>
                     </html>"""

        self.assertEqual(html.html(), remove_indentination(expect))


    def test_html_create_head_in_not_added_child(self):
        self.sut.head()

        expect = """<html>
                    <head></head>
                    </html>"""

        self.assertEqual(self.sut.html(), remove_indentination(expect))


    def test_html_create_children_in_not_added_child(self):

        self.sut.head().title('Title')
        self.sut.body().div()

        expect = """<html>
                    <head>
                    <title>Title</title>
                    </head>
                    <body>
                    <div></div>
                    </body>
                    </html>"""

        self.assertEqual(self.sut.html(), remove_indentination(expect))