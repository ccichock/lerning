import unittest
from Html_Tags import div, h1, h2, a


class Test_div(unittest.TestCase):


    def setUp(self):
        self.sut = div()


    def test_div(self):
        self.assertEqual(self.sut.html(), '<div></div>')


    def test_div_add_class_and_h1(self):
        self.sut.add_class("text-success")
        self.sut.add_child(h1("h1 text"))

        h1_html = '<h1>h1 text</h1>'
        self.assertEqual(self.sut.html(), f'<div class="text-success">\n{h1_html}\n</div>')


    def test_div_add_class_and_h1_h2_children(self):
        self.sut.add_class("text-white bg-dark")
        self.sut.add_child(h1("h1 text"))
        self.sut.add_child(h2("h2 text"))
        self.sut.add_child(h2("h2 second text"))

        h1_html = '<h1>h1 text</h1>'
        h2_html = '<h2>h2 text</h2>'
        h2_second_html = '<h2>h2 second text</h2>'
        self.assertEqual(self.sut.html(), f'<div class="text-white bg-dark">\n{h1_html}\n{h2_html}\n{h2_second_html}\n</div>')


    def test_div_add_div_h2_children(self):
        self.sut.add_child(div())
        self.sut.add_child(h2("H2 text"))

        div_html = '<div></div>'
        h2_html = '<h2>H2 text</h2>'
        self.assertEqual(self.sut.html(), f'<div>\n{div_html}\n{h2_html}\n</div>')


    def test_div_with_button(self):
        self.sut.button("Click")
        self.sut.add_class("container")

        button_html = '<button>Click</button>'
        self.assertEqual(self.sut.html(), f'<div class="container">\n{button_html}\n</div>')


    def test_many_div(self):
        self.sut.div(id="div_1").h1("h1")
        self.sut.div(id="div_2").a()

        h1_html = '<h1>h1</h1>'
        div_h1 = f'<div>\n{h1_html}\n</div>'
        a_html = '<a href="#"></a>'
        div_a = f'<div>\n{a_html}\n</div>'

        self.assertEqual(self.sut.html(), f'<div>\n{div_h1}\n{div_a}\n</div>')