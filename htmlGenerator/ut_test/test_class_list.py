import unittest
from Class_Name import Class_List

class Test_Class_List(unittest.TestCase):


    def setUp(self):
        self.sut = Class_List()


    def test_class_list(self):
        self.sut.add_class("text")
        self.assertEqual(self.sut.to_string(), "text")


    def test_class_list_add_many_class(self):
        self.sut.add_class("text")
        self.sut.add_class("p-4")
        self.sut.add_class("color-primary")

        self.assertEqual(self.sut.to_string(), "text p-4 color-primary")


    def test_class_list_modify_class(self):
        self.sut.add_class("text p-4")
        self.assertEqual(self.sut.to_string(), "text p-4")

        self.sut.add_class("p-3")
        self.assertEqual(self.sut.to_string(), "text p-3")


    def test_class_list_remove_class(self):
        self.sut.add_class("color-primary p-4")
        self.assertEqual(self.sut.to_string(), "color-primary p-4")

        self.sut.remove_class("color")
        self.assertEqual(self.sut.to_string(), "p-4")

        self.sut.remove_class("p")
        self.assertEqual(self.sut.to_string(), "")


    def test_class_list_remove_class_by_full_name(self):
        self.sut.add_class("color-primary p-4")
        self.assertEqual(self.sut.to_string(), "color-primary p-4")

        self.sut.remove_class("p-4")
        self.assertEqual(self.sut.to_string(), "color-primary")


    def test_class_list_remove_many_classes(self):
        self.sut.add_class("color-primary p-4")
        self.assertEqual(self.sut.to_string(), "color-primary p-4")

        self.sut.remove_class("color p")
        self.assertEqual(self.sut.to_string(), "")