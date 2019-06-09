import unittest
from Html_Tags import button, div
from tools.remove_tabs import remove_indentination

class Test_button(unittest.TestCase):


    def setUp(self):
        self.sut = button('Submit')


    def test_button(self):
        self.assertEqual(self.sut.html(), '<button>Submit</button>')


    def test_button_with_classes(self):

        self.sut.add_class('btn btn-default')
        self.assertEqual(self.sut.html(), '<button class="btn btn-default">Submit</button>')


    def test_many_buttons(self):

        div_html = div()
        div_html.add_class('container')
        div_html.button('btn1', id='btn1').add_class('btn btn-default')
        div_html.button('btn2', id='btn2').add_class('btn btn-primary')

        expect = """<div class="container">
                    <button class="btn btn-default">btn1</button>
                    <button class="btn btn-primary">btn2</button>
                    </div>"""

        self.assertEqual(div_html.html(), remove_indentination(expect))