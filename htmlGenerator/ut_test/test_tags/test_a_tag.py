import unittest
from Html_Tags import a


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