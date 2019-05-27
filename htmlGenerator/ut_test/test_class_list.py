import unittest
from Class_Name import Class_List

class Test_Class_List(unittest.TestCase):


    def test_class_list(self):
        class_name = Class_List()
        class_name.add_class("text")

        self.assertEqual(class_name.to_string(), "text")


    def test_class_list_add_many_class(self):
        class_name = Class_List()
        class_name.add_class("text")
        class_name.add_class("p-4")
        class_name.add_class("color-primary")

        self.assertEqual(class_name.to_string(), "text p-4 color-primary")


    def test_class_list_modify_class(self):
        class_name = Class_List()
        class_name.add_class("text p-4")
        self.assertEqual(class_name.to_string(), "text p-4")

        class_name.add_class("p-3")
        self.assertEqual(class_name.to_string(), "text p-3")


    # def test_class_list_remove_class(self):
    #     class_name = Class_List()
    #     class_name.add_class("color-primary p-4")
    #     self.assertEqual(class_name.to_string(), "color-primary p-4")

    #     class_name.remove_class("color")
    #     self.assertEqual(class_name.to_string(), "p-4")