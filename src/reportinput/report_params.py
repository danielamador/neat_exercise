from typing import List
import re


def _process_inputs(input_string) -> List[str]:
    result_string = re.sub("[^0-9A-Za-zÀ-ỿ]+", " ", input_string)
    result_list   = result_string.lower().split()
    return result_list


def _elimin_dupli(input_list) -> List[str]:
    new_list = []
    for elem in input_list:
        if elem not in new_list:
            new_list.append(elem)
    return new_list


def _find_common(list_a, list_b) -> List[str]:
    new_list = []
    for elem in list_a:
        if elem in list_b:
            new_list.append(elem)
    return new_list


def gen_params(input_list_a, input_list_b) -> List[str]:
    res_list_a = _process_inputs(input_list_a)
    res_list_a = _elimin_dupli(res_list_a)
    res_list_b = _process_inputs(input_list_b)
    res_list_b = _elimin_dupli(res_list_b)
    return _find_common(res_list_a, res_list_b)


a = "Dog,caTfish,Frog,FIsh,apple  ,    Monkey,appLe,fox"
b = "Frog  apple    fox cat fish fish"

print(gen_params(a, b))
