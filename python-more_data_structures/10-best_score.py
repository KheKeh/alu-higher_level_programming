#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        maximum = (max(a_dictionary, key=a_dictionary.get))
        if maximum == 0:
            return None
        else:
            return maximum
    else:
        return None
