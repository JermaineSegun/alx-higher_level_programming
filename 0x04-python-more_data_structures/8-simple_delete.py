#!/usr/bin/python3

""" function deletes a key in a dictionary """

def simple_delete(a_dictionary, key=""):
    a_dictionary = sorted(a_dictionary.keys())
    if key in (a_dictionary):
        del a_dictionary[key]
    return a_dictionary

