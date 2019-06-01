import unittest
from HtmlTag import h1


class Test_h1(unittest.TestCase):


    def setUp(self):
        self.sut = h1("text")


    def test_h1(self):
        self.assertEqual(self.sut.html(), """<h1>\ntext\n</h1>""")


    def test_h1_class(self):
        self.sut.add_class("text-center")
        self.assertEqual(self.sut.html(), """<h1 class="text-center">\ntext\n</h1>""")


    def test_h1_many_classes(self):
        self.sut.add_class("text-center p-3")
        self.assertEqual(self.sut.html(), """<h1 class="text-center p-3">\ntext\n</h1>""")


    def test_h1_modify_class(self):
        self.sut.add_class("text-left p-5 m-4")
        self.assertEqual(self.sut.html(), """<h1 class="text-left p-5 m-4">\ntext\n</h1>""")


    def test_h1_add_child(self):
        child_h1_tag = h1("child text")

        self.sut.add_child(child_h1_tag)
        expected_h1_child = """<h1>\nchild text\n</h1>"""
        self.assertEqual(self.sut.html(), f"""<h1>\n{expected_h1_child}\n</h1>""")


    def test_h1_add_many_children(self):
        first_child_h1_tag = h1("first text")
        child_h1_tag = h1("child text")

        self.sut.add_child(first_child_h1_tag)
        self.sut.add_child(child_h1_tag)

        expected_first_h1_child = """<h1>\nfirst text\n</h1>"""
        expected_h1_child = """<h1>\nchild text\n</h1>"""

        self.assertEqual(self.sut.html(), f"""<h1>\n{expected_first_h1_child}\n{expected_h1_child}\n</h1>""")


    def test_h1_add_many_children_modify_class(self):
        child_h1_tag = h1("child text")

        self.sut.add_child(child_h1_tag)
        self.sut.children[0].add_class("m-3 p-5")

        expected_h1_child = """<h1 class="m-3 p-5">\nchild text\n</h1>"""

        self.assertEqual(self.sut.html(), f"""<h1>\n{expected_h1_child}\n</h1>""")