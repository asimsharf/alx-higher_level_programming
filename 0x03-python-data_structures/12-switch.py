#!/usr/bin/python3
def switch(a_dictionary):
    new_dictionary = {}
    for key, value in a_dictionary.items():
        new_dictionary[value] = key
    return new_dictionary
