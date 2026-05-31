import unittest
from name_function import get_formatted_name


class NameTestCase(unittest.TestCase):
    """test for 'name_function.py.'"""

    def test_first_last_name(self):
        """do names like 'janis joplin work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

unittest.main()