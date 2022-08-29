#!/usr/bin/python3
"""def no_c(my_string):
    new_str = ""
    for i in my_string:
        if i is not 'c' or i is not 'C':
            new_str += i
    return (new_str)"""
# return my_string.translate({ord(c): None for c in "cC"})

""" program removes all characters c and C from a string """
def no_c(my_string):
    table = my_string.translate({ord(c): None for c in "cC"})
    return(table)
