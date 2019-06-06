import unittest
from Html_Tags import p, div


class Test_p(unittest.TestCase):


    def setUp(self):
        self.sut = p('dummy paragaph text')


    def test_p(self):
        self.assertEqual(self.sut.html(), '<p>dummy paragaph text</p>')


    def test_many_p(self):
        div_html = div()
        div_html.p('dummy paragaph text', id='p1')
        div_html.p('dummy paragaph text', id='p2')

        expect_p = '<p>dummy paragaph text</p>'
        self.assertEqual(div_html.html(), f'<div>\n{expect_p}\n{expect_p}\n</div>')