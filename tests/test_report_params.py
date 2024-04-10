import unittest
from reportinput import report_params


generate = report_params.gen_params


class TestClass(unittest.TestCase):
    def test_suggested_example(self):
        a = 'Dog,caTfish,Frog,FIsh,apple  ,    Monkey,appLe,fox'
        b = 'Frog  apple    fox cat fish fish'
        expected = ['frog', 'fish', 'apple', 'fox']

        res = generate(a, b)
        assert expected == res


    def test_empty_strings(self):
        a = ''
        b = ''
        assert generate(a, b) == []


    def test_first_empty(self):
        a = ''
        b = 'Frog  apple    fox cat fish fish'
        assert generate(a, b) == []


    def test_second_empty(self):
        a = 'Dog,caTfish,Frog,FIsh,apple  ,    Monkey,appLe,fox'
        b = ''
        assert generate(a, b) == []


    def test_letter_variations(self):
        a = 'AEIOU, ÂÊÎÔÛ, ÃẼĨÕŨ, áéíóú, àèìòù, ÆØÅ, cow, FISH, Ajqk,     2342304892034, measure'
        b = 'aeiou, âêîôû, ãẽĩõũ, ÀÈÌÒÙ, ÁÉÍÓÝ, æøå, MEASURE'
        assert generate(a, b) == ['aeiou', 'âêîôû', 'ãẽĩõũ', 'àèìòù', 'æøå', 'measure']


    def test_numbers(self):
        a = '1234567890 0987654321'
        b = '0987654321 1234567890'
        assert generate(a, b) == ['1234567890', '0987654321']


    def test_delimiters(self):
        a = 'A B-C,D.E\\F@ G|H I J K'
        b = 'A B C D E  F  G H!I#J*K'
        assert generate(a, b) == ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']


    def test_multiple_duplication(self):
        a = 'banana banana banana banana banana banana banana banana banana banana banana banana banana '
        b = 'banana banana banana banana banana banana banana banana banana banana banana banana banana '
        assert generate(a, b) == ['banana']