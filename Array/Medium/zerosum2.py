def hasZeroSumSubarray(nums):
    sumsofar = set()
    sumsofar.add(0)
    sum = 0
    for i in nums:
        print(sumsofar)
        sum+=i
        if sum in sumsofar:
            return True
        sumsofar.add(sum)
    return False
hasZeroSumSubarray([4, -7, 1, 2, -1])
