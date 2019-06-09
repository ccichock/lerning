import unittest
from tools.remove_indents import remove_indentination


class Test_remove_indentination(unittest.TestCase):


    def test_remove_tabs(self):
        html = '\t<h2>dummy text</h2>'
        self.assertEqual(remove_indentination(html), '<h2>dummy text</h2>')


    def test_remove_tabs_child(self):
        h2_html = '\t<h2>dummy text</h2>'
        div_html = f'<div>\n{h2_html}\n</div>'
        self.assertEqual(remove_indentination(div_html), '<div>\n<h2>dummy text</h2>\n</div>')


    def test_remove_tabs_children(self):
        h2_html = '\t\t<h2>dummy text</h2>'
        div_1 = f'<div>\n\t{h2_html}\n</div>'
        div_2 = f'<div>\n{div_1}\n</div>'
        self.assertEqual(remove_indentination(div_2), '<div>\n<div>\n<h2>dummy text</h2>\n</div>\n</div>')


    def test_remove_space(self):
        html = '     <h2>dummy text</h2>'
        self.assertEqual(remove_indentination(html), '<h2>dummy text</h2>')


    def test_remove_spaces_child(self):
        h2_html = '     <h2>dummy text</h2>'
        div_html = f'<div>\n{h2_html}\n</div>'
        self.assertEqual(remove_indentination(div_html), '<div>\n<h2>dummy text</h2>\n</div>')


    def test_remove_tab_spaces_children(self):
        h2_html = '    \t<h2>dummy text</h2>'
        div_1 = f'<div>\n     {h2_html}\n</div>'
        div_2 = f'<div>\n{div_1}\n</div>'
        self.assertEqual(remove_indentination(div_2), '<div>\n<div>\n<h2>dummy text</h2>\n</div>\n</div>')
