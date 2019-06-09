import unittest
from Html_Tags import div, h1, h2, a
from tools.remove_indents import remove_indentination


class Test_div(unittest.TestCase):


    def setUp(self):
        self.sut = div()


    def test_div(self):
        self.assertEqual(self.sut.html(), '<div></div>')


    def test_div_add_class_and_h1(self):
        self.sut.add_class("text-success")
        self.sut.add_child(h1("h1 text"))

        expect = """<div class="text-success">
                    <h1>h1 text</h1>
                    </div>"""

        self.assertEqual(self.sut.html(), remove_indentination(expect))


    def test_div_add_class_and_h1_h2_children(self):
        self.sut.add_class("text-white bg-dark")
        self.sut.add_child(h1("h1 text"))
        self.sut.add_child(h2("h2 text"))
        self.sut.add_child(h2("h2 second text"))

        expect = """<div class="text-white bg-dark">
                    <h1>h1 text</h1>
                    <h2>h2 text</h2>
                    <h2>h2 second text</h2>
                    </div>"""

        self.assertEqual(self.sut.html(), remove_indentination(expect))


    def test_div_add_div_h2_children(self):
        self.sut.add_child(div())
        self.sut.add_child(h2("H2 text"))

        expect = """<div>
                    <div></div>
                    <h2>H2 text</h2>
                    </div>"""

        self.assertEqual(self.sut.html(), remove_indentination(expect))


    def test_div_with_button(self):
        self.sut.button("Click")
        self.sut.add_class("container")

        expect = """<div class="container">
                    <button>Click</button>
                    </div>"""

        self.assertEqual(self.sut.html(), remove_indentination(expect))


    def test_many_div(self):
        self.sut.div(id="div_1").h1("h1")
        self.sut.div(id="div_2").a()

        expect = """<div>
                    <div>
                    <h1>h1</h1>
                    </div>
                    <div>
                    <a href="#"></a>
                    </div>
                    </div>"""

        self.assertEqual(self.sut.html(), remove_indentination(expect))