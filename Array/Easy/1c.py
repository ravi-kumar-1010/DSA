# Using Hasing 
# Problem 1
# Find a pair with the given sum in an array
# Given an unsorted integer array, find a pair with the given sum in it.

import enum


def findPair(nums,target):
    found = {}
    print(nums)
    for i,n in enumerate(nums):
        if (target-n in found):
            print(f"Found pair {target-n},{n} at location {found.get(target-n)},{i} respectively ")
            return
        else:
            found[n] = i
    print("Not found")

if __name__ == '__main__':
 
    nums = [8, 7, 2, 5, 3, 1]
    target = 10
 
    findPair(nums, target)