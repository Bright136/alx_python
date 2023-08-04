#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary == None or a_dictionary == {}:
        return None
    best_score_index = list(a_dictionary.values()).index(max(a_dictionary.values()))
    return list(a_dictionary.keys())[best_score_index]

