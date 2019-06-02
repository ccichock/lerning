import unittest
from Html_Tags import form


class Test_form(unittest.TestCase):


    def setUp(self):
        self.sut = form()


    def test_form(self):
        self.assertEqual(self.sut.html(), '<form>\n\n</form>')


    def test_form(self):
        self.sut.div().add_class('form-group')

        expect_div = f'<div class="form-group">\n\n</div>'
        self.assertEqual(self.sut.html(), f'<form>\n{expect_div}\n</form>')