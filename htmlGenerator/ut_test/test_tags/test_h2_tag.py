import unittest
from generator import h2


class Test_h2(unittest.TestCase):


    def setUp(self):
        self.sut = h2("dummy text")


    def test_h2(self):
        self.assertEqual(self.sut.html(), """<h2>\ndummy text\n</h2>""")