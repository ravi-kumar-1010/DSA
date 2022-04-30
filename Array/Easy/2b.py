# Sort binary array in linear time
# Given a binary array, sort it in linear time and constant space. The output should print all zeroes, followed by all ones.

# For example,

# Input:  { 1, 0, 1, 0, 1, 0, 0, 1 }
 
# Output: { 0, 0, 0, 0, 1, 1, 1, 1 }



def sort(A):
    zero_index = 0
    for i in range(len(A)):
        if A[i] == 0:
            A[zero_index] = 0
            zero_index += 1
    for i in range(zero_index,len(A)):
        A[zero_index] = 1
        zero_index +=1
    
if __name__ == '__main__':
 
    A = [0, 0, 1, 0, 1, 1, 0, 1, 0, 0]
 
    sort(A)
    print(A)
