import unittest
from generator import html, head, title, body, div


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


    def test_default_html_With_class(self):

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

