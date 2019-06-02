import unittest
from Html_Tags import script


class Test_script(unittest.TestCase):


    def setUp(self):
        self.sut = script()


    def test_script(self):
        self.assertEqual(self.sut.html(), """<script></script>""")


    def test_bootstrap_script(self):
        self.sut.bootstrap_script()

        expect_src = "https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"
        expect_integrity = "sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM"
        expect_crossorigin = "anonymous"
        self.assertEqual(self.sut.html(), f'<script src="{expect_src}" integrity="{expect_integrity}" crossorigin="{expect_crossorigin}"></script>')