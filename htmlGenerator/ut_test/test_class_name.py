import unittest
from Class_Name import Class_Name

class Test_Class_Name(unittest.TestCase):


    def test_class_name(self):
        class_name = Class_Name("text-center")

        self.assertEqual(class_name.type(), "text")
        self.assertEqual(class_name.to_string(), "text-center")


    def test_class_name_set_value(self):
        class_name = Class_Name("text-center")

        self.assertEqual(class_name.type(), "text")
        class_name.set_value("left")
        self.assertEqual(class_name.to_string(), "text-left")


    def test_class_name_set_value(self):
        class_name = Class_Name("border-left-width")

        self.assertEqual(class_name.type(), "border")
        class_name.set_value("left-style")
        self.assertEqual(class_name.to_string(), "border-left-style")


    def test_class_name_set_value(self):
        class_name = Class_Name("border-top")

        self.assertEqual(class_name.type(), "border")
        class_name.set_value("top-color")
        self.assertEqual(class_name.to_string(), "border-top-color")