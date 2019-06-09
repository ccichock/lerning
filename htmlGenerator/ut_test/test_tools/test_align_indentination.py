import unittest
from tools.align_indents import align_indentination
import templates.Registration_Form as form_template
import Html_Tags as tags


def html_with_children():
    return '''<html>
    <head>
        <title>new title</title>
    </head>
    <body>
        <div class="container">
            <h1>Header</h1>
        </div>
    </body>
</html>'''


def registration_form():
    return '''<form class="p-2">
    <div class="form-group">
        <label>Name:</label>
        <input placeholder="Type your name" class="form-control">
    </div>
    <div class="form-group">
        <label>Surname:</label>
        <input placeholder="Type your surname" class="form-control">
    </div>
    <div class="form-group">
        <label>Email:</label>
        <input placeholder="Type your email" class="form-control">
    </div>
    <div class="form-group">
        <label>Password:</label>
        <input placeholder="Type your pasword" class="form-control mb-1">
        <input placeholder="Repeat pasword" class="form-control mt-1">
    </div>
    <button class="btn btn-dark">Register</button>
</form>'''

class Test_align_indentination(unittest.TestCase):


    def setUp(self):
        self.sut = tags.html()


    def test_align_html(self):
        self.sut.head()

        expect_head = '<head></head>'
        self.assertEqual(align_indentination(self.sut.html()), f'<html>\n    {expect_head}\n</html>')


    def test_align_html_with_children(self):
        self.sut.head().title('new title')
        self.sut.body().div().add_class("container")
        self.sut.body().div().h1('Header')

        self.assertEqual(align_indentination(self.sut.html()), html_with_children())


    def test_align_registration_form(self):
        form = form_template.Registration_Form()

        self.maxDiff = None

        self.assertEqual(align_indentination(form.html()), registration_form())