#!/usr/bin/python3

def no_c(my_string):
    if my_string:
        new_string = my_string.lower()
        let = new_string.removeprefix('c')
    return let
