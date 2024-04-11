import pytest
from reportinput import report_params


generate = report_params.gen_params


class TestClass():
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
        a = 'A B-C,D.E\\F@ G|H I J K£$%^&*()L'
        b = 'A B C D E  F  G H!I#J*K........L'
        assert generate(a, b) == ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']


    def test_multiple_duplication(self):
        a = 'banana banana banana banana banana banana banana banana banana banana banana banana banana '
        b = 'banana banana banana banana banana banana banana banana banana banana banana banana banana '
        assert generate(a, b) == ['banana']


    def test_alternated_duplication(self):
        a = 'banana ananas banana ananas banana ananas banana ananas banana ananas banana ananas banana '
        b = 'ananas banana ananas banana ananas banana ananas banana ananas banana ananas banana ananas '
        assert generate(a, b) == ['banana', 'ananas']


    def test_needle_in_a_haystack(self):
        a = 'banana PEAR Strawberry pea Raspberry GRAPE melon Mango, waterMelon, jackfruit, lemon, lime'
        b = 'coco Orange PEA tangerine, mandarines, EggPlant, cinnamon, avocado, blueberry, apple, PER, passIon'
        assert generate(a, b) == ['pea']

    
    def test_non_supported_types(self):
        with pytest.raises(TypeError):
            generate([], "")
            generate("", [])
            generate([], [])
            generate(1, "")
            generate("", None)
            generate(object, "")