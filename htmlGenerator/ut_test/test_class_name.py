import unittest
from Class_Name import Class_Name

class Test_Class_Name(unittest.TestCase):


    def test_class_name(self):
        class_name = Class_Name("text-center")

        self.assertEqual(class_name.type(), "text")
        self.assertEqual(class_name.to_string(), "text-center")