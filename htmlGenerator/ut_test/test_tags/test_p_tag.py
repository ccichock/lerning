import unittest
from Html_Tags import p


class Test_p(unittest.TestCase):


    def setUp(self):
        self.sut = p("dummy paragaph text")


    def test_p(self):
        self.assertEqual(self.sut.html(), """<p>\ndummy paragaph text\n</p>""")