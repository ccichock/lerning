import unittest
from Html_Tags import nav
from tools.remove_indents import remove_indentination
from templates.Search_Navbar import Search_Navbar_Html


class Test_nav(unittest.TestCase):


    def setUp(self):
        self.sut = nav('Navbar')


    def test_nav(self):
        self.assertEqual(self.sut.html(), '<nav></nav>')


    def test_search_nav(self):
        nav = Search_Navbar_Html()

        expect = '''<nav class="nav justify-content-end bg-dark p-1">
                    <form class="form-inline my-2 my-lg-0">
                    <input class="form-control mr-sm-2" placeholder="Search">
                    <button class="btn btn-outline-success my-2 my-sm-0">Search</button>
                    </form>
                    </nav>'''

        self.assertEqual(nav.html(), remove_indentination(expect))