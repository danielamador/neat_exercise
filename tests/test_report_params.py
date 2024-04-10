import unittest
from reportinput import report_params


class TestClass(unittest.TestCase):
    def test_suggested_example(self):
        par_1 = "Dog,caTfish,Frog,FIsh,apple  ,    Monkey,appLe,fox"
        par_2 = "Frog  apple    fox cat fish fish"
        expected = ["frog", "fish", "apple", "fox"]

        res = report_params.gen_params(par_1, par_2)
        assert expected == res


    def test_empty_strings(self):
        par_1 = ""
        par_2 = ""
        assert report_params.gen_params(par_1, par_2) == []


    def test_first_empty(self):
        a = ""
        b = "Frog  apple    fox cat fish fish"
        assert report_params.gen_params(a, b) == []


    def test_second_empty(self):
        a = "Dog,caTfish,Frog,FIsh,apple  ,    Monkey,appLe,fox"
        b = ""
        assert report_params.gen_params(a, b) == []


    def test_letter_variations(self):
        a = "AEIOU, ÂÊÎÔÛ, ÃẼĨÕŨ, áéíóú, àèìòù, ÆØÅ, cow, FISH, Ajqk,     2342304892034, measure"
        b = "aeiou, âêîôû, ãẽĩõũ, ÀÈÌÒÙ, ÁÉÍÓÝ, æøå, MEASURE"
        assert report_params.gen_params(a, b) == ['aeiou', 'âêîôû', 'ãẽĩõũ', 'àèìòù', 'æøå', 'measure']


    def test_numbers(self):
        a = "1234567890 0987654321"
        b = "0987654321 1234567890"
        assert report_params.gen_params(a, b) == ["1234567890", "0987654321"]
