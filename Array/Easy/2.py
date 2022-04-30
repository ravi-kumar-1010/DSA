# Sort binary array in linear time
# Given a binary array, sort it in linear time and constant space. The output should print all zeroes, followed by all ones.

# For example,

# Input:  { 1, 0, 1, 0, 1, 0, 0, 1 }
 
# Output: { 0, 0, 0, 0, 1, 1, 1, 1 }



def sort(A):
    total_zero_count = A.count(0)
    length = len(A)
    result1 = [0]*total_zero_count
    result2 = [1]*(length - total_zero_count)
    result = result1+result2
    return result

if __name__ == '__main__':
 
    A = [0, 0, 1, 0, 1, 1, 0, 1, 0, 0]
 
    print(sort(A))
