import unittest

from unittest import TestCase

from main import remove_value_from_list


class TestRemoveValueFromList(unittest.TestCase):

    def test_removes_first_instance_of_value(self):
        list = [1, 2, 3, 4, 5]
        value = 3
        new_list = remove_value_from_list(list, value)
        self.assertEqual(new_list, [1, 2, 3, 5])

    def test_returns_original_list_if_value_not_present(self):
        list = [1, 2, 3, 4, 5]
        value = 6
        new_list = remove_value_from_list(list, value)
        self.assertEqual(new_list, [1, 2, 3, 4, 5])

    def test_removes_only_first_instance_of_value(self):
        list = [1, 2, 3, 4, 6, 5]
        value = 3
        new_list = remove_value_from_list(list, value)
        self.assertEqual(new_list, [1, 2, 3, 6, 5])
