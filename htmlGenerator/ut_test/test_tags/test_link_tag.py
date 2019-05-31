import unittest
from generator import link


class Test_link(unittest.TestCase):


    def setUp(self):
        self.sut = link()


    def test_bootstrap_link(self):
        self.sut.bootstrap()

        expect_rel="stylesheet" 
        expect_href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" 
        expect_integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" 
        expect_crossorigin="anonymous"

        expect_link = f'<link rel="{expect_rel}" href="{expect_href}" integrity="{expect_integrity}" crossorigin="{expect_crossorigin}">'
        self.assertEqual(self.sut.html(), expect_link)