import unittest
from Html_Tags import button


class Test_button(unittest.TestCase):


    def setUp(self):
        self.sut = button("Submit")


    def test_button(self):
        self.assertEqual(self.sut.html(), """<button>Submit</button>""")


    def test_button_with_classes(self):

        self.sut.add_class("btn btn-default")
        self.assertEqual(self.sut.html(), """<button class="btn btn-default">Submit</button>""")