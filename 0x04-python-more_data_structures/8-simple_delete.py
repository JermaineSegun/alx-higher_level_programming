#!/usr/bin/python3

""" function deletes a key in a dictionary """

def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        del a_dictionary[key]
    return sorted(a_dictionary.items())

