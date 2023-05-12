#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    my_list_rev = reversed(my_list)
    for i in my_list_rev:
        print("{:d}".format(i))
