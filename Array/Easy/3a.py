# Find the maximum product of two integers in an array
# Given an integer array, find the maximum product of two integers in it.

# For example, consider array {-10, -3, 5, 6, -2}. The maximum product is the (-10, -3) or (5, 6) pair.
# using Itertools

import sys
import itertools as it


def findMaximumProduct(A):
    high = -sys.maxsize
    pair = []
    for a,b in it.combinations(A, 2):
        if a*b > high:
            high = a*b
            pair.append([a,b])
    print(pair[-1])



if __name__ == '__main__':
 
    A = [-10, -3, 5, 6, -2,-20]
    findMaximumProduct(A)