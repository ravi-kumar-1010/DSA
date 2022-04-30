# Problem 1
# Find a pair with the given sum in an array
# Given an unsorted integer array, find a pair with the given sum in it.

def findPair(nums,target):
    nums.sort()
    low = 0
    high = len(nums)-1
    print(nums)
    while(low<high):
        sum = nums[low] + nums[high]
        
        print(f"Low: {low} High: {high}")
        if sum == target:
            print("Yes")
            return 
        else:
            if sum < target:
                low = low + 1
            elif sum > target:
                high = high + 1
    print("No")

if __name__ == '__main__':
 
    nums = [8, 7, 2, 5, 3, 1]
    target = 10
 
    findPair(nums, target)