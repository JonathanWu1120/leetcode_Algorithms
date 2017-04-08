class Solution(object):
	def majorityElement(self,nums):
		arr = {}
		for c in nums:
			if c not in arr:
				arr[c] = 1
			elif c in arr:
				arr[c] += 1
		majority = float(len(nums))/float(2)
		for k,v in arr.items():
			if v >= majority:
				return k 
