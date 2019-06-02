import unittest
from HtmlTag import html, head, title, body, div
from templates.Default_Html import Default_Html

class Test_html(unittest.TestCase):


    def setUp(self):
        self.sut = html()


    def test_html(self):
        self.assertEqual(self.sut.html(), """<html>\n\n</html>""")


    def test_default_html(self):
        title_html = title("Page Title")
        head_html = head()
        head_html.add_child(title_html)

        body_html = body()

        self.sut.add_child(head_html)
        self.sut.add_child(body_html)

        expect_title = """<title>\nPage Title\n</title>"""
        expect_head = f"""<head>\n{expect_title}\n</head>"""
        expect_body = """<body>\n\n</body>"""
        expect_html = f"""<html>\n{expect_head}\n{expect_body}\n</html>"""

        self.assertEqual(self.sut.html(), expect_html)


    def test_default_html_reverse(self):

        self.sut.add_child(head())
        self.sut.head().add_child(title("title"))
        self.sut.add_child(body())

        expect_title = """<title>\ntitle\n</title>"""
        expect_head = f"""<head>\n{expect_title}\n</head>"""
        expect_body = """<body>\n\n</body>"""
        expect_html = f"""<html>\n{expect_head}\n{expect_body}\n</html>"""

        self.assertEqual(self.sut.html(), expect_html)


    def test_default_html_with_class(self):

        self.sut.add_child(head())
        self.sut.head().add_child(title("title"))
        self.sut.add_child(body())
        self.sut.body().add_class("p-5 m-2")
        self.sut.body().add_child(div())
        self.sut.body().div().add_class("container")

        expect_title = """<title>\ntitle\n</title>"""
        expect_head = f"""<head>\n{expect_title}\n</head>"""
        expect_div = """<div class="container">\n\n</div>"""
        expect_body = f"""<body class="p-5 m-2">\n{expect_div}\n</body>"""
        expect_html = f"""<html>\n{expect_head}\n{expect_body}\n</html>"""

        self.assertEqual(self.sut.html(), expect_html)


    def test_default_html_class(self):
        html = Default_Html("Page Title")

        expect_title = '<title>\nPage Title\n</title>'

        expect_rel="stylesheet" 
        expect_href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" 
        expect_integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" 
        expect_crossorigin="anonymous"
        expect_link = f'<link rel="{expect_rel}" href="{expect_href}" integrity="{expect_integrity}" crossorigin="{expect_crossorigin}">'

        expect_head = f'<head>\n{expect_link}\n{expect_title}\n</head>'

        expect_src = 'https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js'
        expect_integrity = 'sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM'
        expect_crossorigin = 'anonymous'
        expect_script = f'<script src="{expect_src}" integrity="{expect_integrity}" crossorigin="{expect_crossorigin}"></script>'

        expect_body = f'<body>\n{expect_script}\n</body>'
        expect_html = f'<html>\n{expect_head}\n{expect_body}\n</html>'

        self.assertEqual(html.html(), expect_html)
        self.assertEqual(html.head().html(), expect_head)
        self.assertEqual(html.body().html(), expect_body)
        self.assertEqual(html.html(), expect_html)


    def test_html_create_head_in_not_added_child(self):

        self.sut.head()
        expect_head = f"""<head>\n\n</head>"""
        expect_html = f"""<html>\n{expect_head}\n</html>"""
        self.assertEqual(self.sut.html(), expect_html)


    def test_html_create_children_in_not_added_child(self):

        self.sut.head().title("Title")
        self.sut.body().div()

        expect_title = f"""<title>\nTitle\n</title>"""
        expect_head = f"""<head>\n{expect_title}\n</head>"""
        expect_div = f"""<div>\n\n</div>"""
        expect_body = f"""<body>\n{expect_div}\n</body>"""

        expect_html = f"""<html>\n{expect_head}\n{expect_body}\n</html>"""
        self.assertEqual(self.sut.html(), expect_html)