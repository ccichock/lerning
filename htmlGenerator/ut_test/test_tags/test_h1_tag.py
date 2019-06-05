import unittest
from Html_Tags import h1


class Test_h1(unittest.TestCase):


    def setUp(self):
        self.sut = h1("text")


    def test_h1(self):
        self.assertEqual(self.sut.html(), """<h1>text</h1>""")


    def test_h1_class(self):
        self.sut.add_class("text-center")
        self.assertEqual(self.sut.html(), """<h1 class="text-center">text</h1>""")


    def test_h1_many_classes(self):
        self.sut.add_class("text-center p-3")
        self.assertEqual(self.sut.html(), """<h1 class="text-center p-3">text</h1>""")


    def test_h1_modify_class(self):
        self.sut.add_class("text-left p-5 m-4")
        self.assertEqual(self.sut.html(), """<h1 class="text-left p-5 m-4">text</h1>""")