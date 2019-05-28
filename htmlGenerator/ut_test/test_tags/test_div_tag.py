import unittest
from generator import div, h1, h2


class Test_div(unittest.TestCase):


    def setUp(self):
        self.sut = div()


    def test_div(self):
        self.assertEqual(self.sut.html(), """<div class="">\n\n</div>""")


    def test_div_add_class_and_h1(self):
        self.sut.add_class("text-success")
        self.sut.add_child(h1("h1 text"))

        h1_html = """<h1 class="">\nh1 text\n</h1>"""
        self.assertEqual(self.sut.html(), f"""<div class="text-success">\n{h1_html}\n</div>""")


    def test_div_add_class_and_h1_h2_children(self):
        self.sut.add_class("text-white bg-dark")
        self.sut.add_child(h1("h1 text"))
        self.sut.add_child(h2("h2 text"))
        self.sut.add_child(h2("h2 second text"))

        h1_html = """<h1 class="">\nh1 text\n</h1>"""
        h2_html = """<h2 class="">\nh2 text\n</h2>"""
        h2_second_html = """<h2 class="">\nh2 second text\n</h2>"""
        self.assertEqual(self.sut.html(), f"""<div class="text-white bg-dark">\n{h1_html}\n{h2_html}\n{h2_second_html}\n</div>""")


    def test_div_add_div_h2_children(self):
        self.sut.add_child(div())
        self.sut.add_child(h2("H2 text"))

        div_html = """<div class="">\n\n</div>"""
        h2_html = """<h2 class="">\nH2 text\n</h2>"""
        self.assertEqual(self.sut.html(), f"""<div class="">\n{div_html}\n{h2_html}\n</div>""")