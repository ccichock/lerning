import unittest
from Html_Tags import p, div
from tools.remove_indents import remove_indentination


class Test_p(unittest.TestCase):


    def setUp(self):
        self.sut = p('dummy paragaph text')


    def test_p(self):
        self.assertEqual(self.sut.html(), '<p>dummy paragaph text</p>')


    def test_many_p(self):
        div_html = div()
        div_html.p('dummy paragaph text', id='p1')
        div_html.p('dummy paragaph text', id='p2')

        expect = """<div>
                    <p>dummy paragaph text</p>
                    <p>dummy paragaph text</p>
                    </div>"""

        self.assertEqual(div_html.html(), remove_indentination(expect))