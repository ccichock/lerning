import unittest
from generator import html, head, title, body


class Test_html(unittest.TestCase):


    def setUp(self):
        self.sut = html()


    def test_html(self):
        self.assertEqual(self.sut.html(), """<html class="">\n\n</html>""")


    def test_default_html(self):
        title_html = title("Page Title")
        head_html = head()
        head_html.add_child(title_html)

        body_html = body()

        self.sut.add_child(head_html)
        self.sut.add_child(body_html)

        expect_title = """<title class="">\nPage Title\n</title>"""
        expect_head = f"""<head class="">\n{expect_title}\n</head>"""
        expect_body = """<body class="">\n\n</body>"""

        expect_html = f"""<html class="">\n{expect_head}\n{expect_body}\n</html>"""

        self.assertEqual(self.sut.html(), expect_html)

