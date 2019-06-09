import unittest
from Html_Tags import form, textarea, label, input_text, div
from tools.remove_tabs import remove_indentination


class Test_form(unittest.TestCase):


    def setUp(self):
        self.sut = form()


    def test_form(self):
        self.assertEqual(self.sut.html(), '<form></form>')


    def test_form(self):
        self.sut.div().add_class('form-group')

        expect = """<form>
                    <div class="form-group"></div>
                    </form>"""

        self.assertEqual(self.sut.html(), remove_indentination(expect))


    def test_label(self):
        label_html = label()
        self.assertEqual(label_html.html(), f'<label></label>')


    def test_label_text(self):
        label_html = label("Label:")
        self.assertEqual(label_html.html(), f'<label>Label:</label>')


    def test_input(self):
        input_html = input_text()
        self.assertEqual(input_html.html(), f'<input>')


    def test_input_class_placeholder(self):
        input_html = input_text()
        input_html.placeholder("Your input")
        input_html.add_class("form-control")
        self.assertEqual(input_html.html(), f'<input placeholder="Your input" class="form-control">')


    def test_textarea(self):
        textarea_html = textarea()
        self.assertEqual(textarea_html.html(), f'<textarea></textarea>')


    def test_textarea_class(self):
        textarea_html = textarea()
        textarea_html.add_class('form-control')
        self.assertEqual(textarea_html.html(), f'<textarea class="form-control"></textarea>')


    def test_textarea_class_placeholder(self):
        textarea_html = textarea()
        textarea_html.add_class('form-control')
        textarea_html.placeholder('Type your message')
        self.assertEqual(textarea_html.html(), f'<textarea class="form-control" placeholder="Type your message"></textarea>')


    def test_form_textarea_class_placeholder(self):
        self.sut.textarea().add_class('form-control')
        self.sut.textarea().placeholder('Type your message')


        expect = """<form>
                    <textarea class="form-control" placeholder="Type your message"></textarea>
                    </form>"""

        expect_textarea = f'<textarea class="form-control" placeholder="Type your message"></textarea>'
        self.assertEqual(self.sut.html(), remove_indentination(expect))


    def test_form_input_label(self):
        self.sut.label("Label")
        self.sut.input().placeholder("...")

        expect = """<form>
                    <label>Label</label>
                    <input placeholder="...">
                    </form>"""

        self.assertEqual(self.sut.html(), remove_indentination(expect))


    def test_many_forms(self):
        div_html = div()
        div_html.form(id='form1')
        div_html.form(id='form2')

        expect = """<div>
                    <form></form>
                    <form></form>
                    </div>"""

        self.assertEqual(div_html.html(), remove_indentination(expect))