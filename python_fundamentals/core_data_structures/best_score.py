#!/usr/bin/env python3
def best_score(a_dictionary):
    if a_dictionary is None or not a_dictionary:
        return None
    key_max = list(a_dictionary.keys())[0]
    max_value = list(a_dictionary.values())[0]
    for keys in a_dictionary:
        if a_dictionary[keys] > max_value:
            max_value = a_dictionary[keys]
            key_max = keys
    return key_max, max_value
