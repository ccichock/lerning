import unittest
from Html_Tags import a, div
from tools.remove_indents import remove_indentination

class Test_a(unittest.TestCase):


    def setUp(self):
        self.sut = a()


    def test_a(self):
        self.assertEqual(self.sut.html(), '<a href="#"></a>')


    def test_a_href(self):
        a_html = a(text='', url='https://www.youtube.com/')
        self.assertEqual(a_html.html(), '<a href="https://www.youtube.com/"></a>')


    def test_a_href_and_class(self):
        a_html = a(text='Link', url='https://www.youtube.com/')
        a_html.add_class("btn btn-light")
        self.assertEqual(a_html.html(), '<a href="https://www.youtube.com/" class="btn btn-light">Link</a>')


    def test_many_a_href(self):
        div_html = div()
        div_html.a(id="yt" ,text='Link', url='https://www.youtube.com/')
        div_html.a(id="gg" ,text='Link2', url='https://www.google.com/')
        div_html.a(id="yt").add_class("btn btn-light")

        expect_html = """<div>
                         <a href="https://www.youtube.com/" class="btn btn-light">Link</a>
                         <a href="https://www.google.com/">Link2</a>
                         </div>"""

        self.assertEqual(div_html.html(), remove_indentination(expect_html))