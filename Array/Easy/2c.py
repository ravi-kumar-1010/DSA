# Sort binary array in linear time
# Given a binary array, sort it in linear time and constant space. The output should print all zeroes, followed by all ones.

# For example,

# Input:  { 1, 0, 1, 0, 1, 0, 0, 1 }
 
# Output: { 0, 0, 0, 0, 1, 1, 1, 1 }

def swap(a,i,j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp  

def sort(A):
    pivot = 1
    pIndex = 0
    for i in range(len(A)):
        if A[i] < pivot:
            swap(A,i,pIndex)
            pIndex = pIndex + 1

if __name__ == '__main__':
 
    A = [0, 0, 1, 0, 1, 1, 0, 1, 0, 0]
 
    sort(A)
    print(A)
