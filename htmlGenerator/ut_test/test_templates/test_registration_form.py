import unittest
from templates.Registration_Form import Registration_Form


class Test_Registration_Form(unittest.TestCase):

    def test_registration_form(self):
        
        self.maxDiff = None

        form = Registration_Form()

        label_name = '<label>Name:</label>'
        input_name = '<input placeholder="Type your name" class="form-control">'
        div_name = f'<div class="form-group">\n{label_name}\n{input_name}\n</div>'

        label_surname = '<label>Surname:</label>'
        input_surname = '<input placeholder="Type your surname" class="form-control">'
        div_surname = f'<div class="form-group">\n{label_surname}\n{input_surname}\n</div>'

        label_emil = '<label>Email:</label>'
        input_emil = '<input placeholder="Type your email" class="form-control">'
        div_emil = f'<div class="form-group">\n{label_emil}\n{input_emil}\n</div>'

        label_password = '<label>Password:</label>'
        input_password = '<input placeholder="Type your pasword" class="form-control mb-1">'
        input_password_repeat = '<input placeholder="Repeat pasword" class="form-control mt-1">'
        div_password = f'<div class="form-group">\n{label_password}\n{input_password}\n{input_password_repeat}\n</div>'

        submit_button = '<button class="btn btn-dark">Register</button>'

        expect_from = f'<form class="p-2">\n{div_name}\n{div_surname}\n{div_emil}\n{div_password}\n{submit_button}\n</form>'

        self.assertEqual(form.html(), expect_from)