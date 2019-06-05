import unittest
from Html_Tags import form, textarea


class Test_form(unittest.TestCase):


    def setUp(self):
        self.sut = form()


    def test_form(self):
        self.assertEqual(self.sut.html(), '<form></form>')


    def test_form(self):
        self.sut.div().add_class('form-group')

        expect_div = f'<div class="form-group"></div>'
        self.assertEqual(self.sut.html(), f'<form>\n{expect_div}\n</form>')


    def test_textarea(self):
        textarea_html = textarea()
        self.assertEqual(textarea_html.html(), f'<textarea></textarea>')


    def test_textarea_class(self):
        textarea_html = textarea()
        textarea_html.add_class("from-control")
        self.assertEqual(textarea_html.html(), f'<textarea class="from-control"></textarea>')


    def test_textarea_class_placeholder(self):
        textarea_html = textarea()
        textarea_html.add_class("from-control")
        textarea_html.placeholder("Type your message")
        self.assertEqual(textarea_html.html(), f'<textarea class="from-control" placeholder="Type your message"></textarea>')


    def test_Form_textarea_class_placeholder(self):
        self.sut.textarea().add_class("from-control")
        self.sut.textarea().placeholder("Type your message")

        expect_textarea = f'<textarea class="from-control" placeholder="Type your message"></textarea>'

        self.assertEqual(self.sut.html(), f'<form>\n{expect_textarea}\n</form>')