"""
PROBLEM 2
This file contains code for problem 2 which asks us to make a function that removes 
the first and last element of a list and return it
"""
def middle(a):
        c = a[1:len(a)-1] #list going from index 1 (second term) to index length of A - 1. Everything except first and last term
        return c

