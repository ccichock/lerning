import unittest

from ut_test.test_class_name import Test_Class_Name
from ut_test.test_class_list import Test_Class_List

from generator import h1


class TestStringMethods(unittest.TestCase):

    def test_h1(self):
        h1_tag = h1("text")
        self.assertEqual(h1_tag.html(), """<h1 class="bg-dark">\ntext\n</h1>""")


    def test_h1_class(self):
        h1_tag = h1("text and texts")
        h1_tag.add_class("text-center")
        self.assertEqual(h1_tag.html(), """<h1 class="bg-dark text-center">\ntext and texts\n</h1>""")


    def test_h1_many_classes(self):
        h1_tag = h1("")
        h1_tag.add_class("text-center p-3")
        self.assertEqual(h1_tag.html(), """<h1 class="bg-dark text-center p-3">\n\n</h1>""")


    def test_h1_modify_class(self):
        h1_tag = h1("text")

        h1_tag.add_class("text-center p-3 m-4")
        h1_tag.add_class("p-5")
        h1_tag.add_class("text-left")

        self.assertEqual(h1_tag.html(), """<h1 class="bg-dark text-left p-5 m-4">\ntext\n</h1>""")


    def test_h1_add_child(self):
        h1_tag = h1("text")
        child_h1_tag = h1("child text")

        h1_tag.add_child(child_h1_tag)
        expected_h1_child = """<h1 class="bg-dark">\nchild text\n</h1>"""
        self.assertEqual(h1_tag.html(), """<h1 class="bg-dark">\n{}\n</h1>""".format(expected_h1_child))


    def test_h1_add_many_children(self):
        h1_tag = h1("text")
        first_child_h1_tag = h1("first text")
        child_h1_tag = h1("child text")

        h1_tag.add_child(first_child_h1_tag)
        h1_tag.add_child(child_h1_tag)

        expected_first_h1_child = """<h1 class="bg-dark">\nfirst text\n</h1>"""
        expected_h1_child = """<h1 class="bg-dark">\nchild text\n</h1>"""

        self.assertEqual(h1_tag.html(), """<h1 class="bg-dark">\n{}\n{}\n</h1>""".format(expected_first_h1_child, expected_h1_child))


    def test_h1_add_many_children(self):
        h1_tag = h1("text")
        child_h1_tag = h1("child text")

        h1_tag.add_child(child_h1_tag)
        h1_tag.children[0].add_class("m-3 p-5")

        expected_h1_child = """<h1 class="bg-dark m-3 p-5">\nchild text\n</h1>"""

        self.assertEqual(h1_tag.html(), """<h1 class="bg-dark">\n{}\n</h1>""".format(expected_h1_child))



    # def test_isupper(self):
    #     self.assertTrue('FOO'.isupper())
    #     self.assertFalse('Foo'.isupper())

    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)


def sut():
    sut = unittest.TestSuite()
    suite.addTests(TestStringMethods)

if __name__ == '__main__':
    unittest.main()