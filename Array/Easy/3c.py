# Find the maximum product of two integers in an array

# Given an integer array, find the maximum product of two integers in it.

# For example, consider array {-10, -3, 5, 6, -2}. The maximum product is the (-10, -3) or (5, 6) pair.

# By sorting

import sys

def findMaximumProduct(A):
    # to store the maximum and second maximum element in a list
    max1 = A[0]
    max2 = -sys.maxsize
    
    # to store the minimum and second minimum element in a list
    min1 = A[0]
    min2 = sys.maxsize
    
    for i in range(1, len(A)):

        if A[i] > max1:  # max1 > max2
            max2 = max1
            max1 = A[i]  # still max1 > max2

        elif A[i] > max2:
            max2 = A[i]  # A[i] < max1
        
        if A[i] < min1:   # min1 < min2
            min2 = min1
            min1 = A[i]   # still min1 < min2
            
        elif A[i] < min2:
            min2 = A[i]   # A[i] > max2

    if (min1 * min2) > (max1 * max2):
        print(min1,min2)
    else:
        print(max1,max2)
    
if __name__ == '__main__':
 
    A = [-10, -3, 5,-33, 6, -2,-20]
    findMaximumProduct(A)