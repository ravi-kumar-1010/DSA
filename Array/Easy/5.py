def findMajorityElement(nums):
		mydict = {}
		for i in nums:
			mydict[i] = mydict.get(i,0) + 1
		Keymax = max(zip(mydict.values(), mydict.keys()))[1]
		return Keymax

print(findMajorityElement([1,4,3,4,5,6,4,5,6,3]))