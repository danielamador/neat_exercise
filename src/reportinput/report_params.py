from typing import List
import re


def _process_inputs(input_string):
    result_string = re.sub("[^A-Za-zÀ-ȕ]+", " ", input_string)
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

a = "Redenção, Tromsø, ÂÊÎÔÛ, cow, FISH, Ajqk,               2342304892034, measure"
b = "TROMSØ, COW, RedENÇão, âêîôû"

print(gen_params(a, b))
