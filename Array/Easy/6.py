'''

Given an integer array, move all zeros present in it to the end. The solution should maintain the relative order of items in the array and should not use constant space.

Input : [6, 0, 8, 2, 3, 0, 4, 0, 1]
Output: [6, 8, 2, 3, 4, 1, 0, 0, 0]

'''
def rearrange(nums):
    zeroindex = []
    for i,n in enumerate(nums):
        if n == 0:
            zeroindex.append(i)
    counter = 0
    for i in zeroindex:
        nums.pop(i-counter)
        counter +=1
    for i in zeroindex:
        nums.append(0)
nums = [6, 0, 8, 2, 3, 0, 4, 0, 1]
rearrange(nums)
print(nums)