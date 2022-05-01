# Find the maximum product of two integers in an array
# Given an integer array, find the maximum product of two integers in it.

# For example, consider array {-10, -3, 5, 6, -2}. The maximum product is the (-10, -3) or (5, 6) pair.
# By sorting




def findMaximumProduct(A):
    A.sort()
    la,lb = A[0],A[1]
    ra,rb = A[-1],A[-2]
    if (la*lb > ra*rb):
        print(la,lb)
    else:
        print(ra,rb)



if __name__ == '__main__':
 
    A = [-10, -3, 5,-33, 6, -2,-20]
    findMaximumProduct(A)