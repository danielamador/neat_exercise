from typing import List
import re


def _process_inputs(input_string):
    result_string = re.sub("[^A-Za-z]+", " ", input_string)
    result_string = result_string.lower()
    result_list   = result_string.split()
    return result_list


def _elimin_dupli(input_list):
    new_list = []
    for elem in input_list:
        if elem not in new_list:
            new_list.append(elem)
    return new_list


def gen_params(a, b) -> List[str]:
    input_list_a = _process_inputs(a)
    input_list_b = _process_inputs(b)
    merged_list = input_list_a + input_list_b
    return _elimin_dupli(merged_list)


par_1 = "Dog,caTfish,Frog,FIsh,apple  ,    Monkey,appLe,fox"
par_2 = "Frog  apple    fox cat fish fish"

print(gen_params(par_1, par_2))
