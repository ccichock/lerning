import unittest
from templates.Registration_Form import Registration_Form
from tools.remove_tabs import remove_indentination


class Test_Registration_Form(unittest.TestCase):


    def test_registration_form(self):

        form = Registration_Form()

        expect = """<form class="p-2">
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
                    </form>"""

        self.assertEqual(form.html(), remove_indentination(expect))