#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = "Sayan Mukherjee"
__version__ = "0.1.0"
__license__ = "MIT"

import unittest

def remove_vowels(string):
    ''' uses a list comprehension and returns a copy of the string with no vowels '''

    return "".join([c for c in string if c.lower() not in ['a', 'e', 'i', 'o', 'u']])

def check_pwd(pwd):
    ''' returns True if the password includes at least one upper case character, 
        at least one lower case character, and the password must end with at least one digit.
        Or else False '''

    return any([c.islower() for c in pwd]) and any([c.isupper() for c in pwd]) and pwd[-1].isdigit()

def insertion_sort(unsorted_list):
    ''' returns a copy of the argument sorted using a list and the insertion sort algorithm '''

    sorted_list = list()

    for u_item in unsorted_list:
        for i, s_item in reversed(list(enumerate(sorted_list))):
            if u_item > s_item:
                sorted_list.insert(i+1, u_item)
                break
        else:
            sorted_list.insert(0, u_item)

    return sorted_list


class AllTest(unittest.TestCase):
    ''' Test cases for all functions '''

    def test_remove_vowels(self):
        ''' test remove_vowels(string) '''

        self.assertEqual(remove_vowels('hello'), 'hll')
        self.assertEqual(remove_vowels('hello world'), 'hll wrld')
        self.assertEqual(remove_vowels('HELLO world'), 'HLL wrld')
        self.assertEqual(remove_vowels('RHYTHM'), 'RHYTHM')
        self.assertEqual(remove_vowels('aeiou'), '')
        self.assertEqual(remove_vowels(''), '')

    def test_check_pwd(self):
        ''' test check_pwd(pwd) '''

        self.assertTrue(check_pwd('Verbosity1'))
        self.assertTrue(check_pwd('verbositY1'))
        self.assertTrue(check_pwd('VERBOSe1'))
        self.assertFalse(check_pwd('VERBOSe'))
        self.assertFalse(check_pwd(''))
        self.assertFalse(check_pwd('verbose1'))
        self.assertFalse(check_pwd('VERBOSE1'))
        self.assertFalse(check_pwd('1Verbose'))
        self.assertFalse(check_pwd('Ver1Bose'))

    def test_insertion_sort(self):
        ''' test insertion_sort(list) '''

        seq = [3,2,5,7,1]
        self.assertEqual(insertion_sort(seq), sorted(seq))

        seq = [1,2,3,4,5,6,7,8]
        self.assertEqual(insertion_sort(seq), sorted(seq))

        seq = []
        self.assertEqual(insertion_sort(seq), sorted(seq))

        seq = [-1,-2,-3,-4,-5,-6]
        self.assertEqual(insertion_sort(seq), sorted(seq))

        seq = [1, 5, 3, 3]
        self.assertEqual(insertion_sort(seq), sorted(seq))


if __name__ == "__main__":
    ''' This is executed when run from the command line '''

    unittest.main(exit=False, verbosity=2)
