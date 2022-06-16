
def getAllZeroSumSubarrays(nums):
    subarrays = set()
    sum = 0
    for i in range(len(nums)):
        for j in range(i,len(nums)):
            sum = sum + nums[j]
            if sum == 0:
                subarrays.add(tuple(nums[i:j+1]))
        sum = 0      
    return subarrays
getAllZeroSumSubarrays([3, 4, -7, 3, 1, 3, 1, -4, -2, -2])