import unittest
from generator import h2


class Test_h1(unittest.TestCase):


    def setUp(self):
        self.sut = h2("bla")


    def test_h2(self):
        self.assertEqual(selfsut.html(), """<h2 class="">\nbla\n</h2>""")