'''

Given a circularly sorted array of distinct integers, find the total number of times the array is rotated. You may assume that the rotation is in anti-clockwise direction.

Input: [8, 9, 10, 2, 5, 6]
Output: 3

Input: [2, 5, 6, 8, 9, 10]
Output: 0

'''

class Solution:
	def findRotationCount(self, nums):
		j = 0
		for i in range(1,len(nums)):
			if nums[i] < nums[j]:
				return i
			j +=1
		return 0
	
ob  = Solution()
print(ob.findRotationCount([8, 9, 10, 2, 5, 6]))