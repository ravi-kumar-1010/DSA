# Find a pair with the given sum in an array
# Given an unsorted integer array, find a pair with the given sum in it.

def findPair(nums,target):
    for i in range(len(nums)):
        for j in range(1,len(nums)):
            if nums[i] + nums[j] == target:
                print("Yes")
                return

    print("No")
        

if __name__ == '__main__':
 
    nums = [8, 7, 2, 5, 3, 1]
    target = 10
 
    findPair(nums, target)