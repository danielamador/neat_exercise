import unittest
from reportinput import report_params


class TestClass(unittest.TestCase):
    def test_suggested_example(self):
        par_1 = "Dog,caTfish,Frog,FIsh,apple  ,    Monkey,appLe,fox"
        par_2 = "Frog  apple    fox cat fish fish"
        expected = ['dog', 'catfish', 'frog', 'fish', 'apple', 'monkey', 'fox', 'cat']

        res = report_params.gen_params(par_1, par_2)
        assert expected == res


    def test_empty_strings(self):
        par_1 = ""
        par_2 = ""

        assert report_params.gen_params(par_1, par_2) == []


    def test_first_empty(self):
        a = ""
        b = "Frog  apple    fox cat fish fish"

        assert report_params.gen_params(a, b) == ["frog", "apple", "fox", "cat", "fish"]


    def test_second_empty(self):
        a = "Dog,caTfish,Frog,FIsh,apple  ,    Monkey,appLe,fox"
        b = ""

        assert report_params.gen_params(a, b) == ["dog", "catfish", "frog", "fish", "apple", "monkey", "fox"]