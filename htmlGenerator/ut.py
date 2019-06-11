import unittest
import sys

sys.path.append('./src')

from ut_test.test_class_name import Test_Class_Name
from ut_test.test_class_list import Test_Class_List
from ut_test.test_tags.test_h1_tag import Test_h1
from ut_test.test_tags.test_h2_tag import Test_h2
from ut_test.test_tags.test_div_tag import Test_div
from ut_test.test_tags.test_html_tag import Test_html
from ut_test.test_tags.test_script_tag import Test_script
from ut_test.test_tags.test_link_tag import Test_link
from ut_test.test_tags.test_button_tag import Test_button
from ut_test.test_tags.test_a_tag import Test_a
from ut_test.test_tags.test_p_tag import Test_p
from ut_test.test_tags.test_form_tag import Test_form
from ut_test.test_tags.test_nav_tag import Test_nav

from ut_test.test_templates.test_registration_form import Test_Registration_Form

from ut_test.test_tools.test_remove_indentination import Test_remove_indentination
from ut_test.test_tools.test_add_indentination import Test_add_indentination

if __name__ == '__main__':
    unittest.main()