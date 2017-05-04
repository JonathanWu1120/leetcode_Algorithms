class Solution(object):
	def titleToNumber(self,s):
		arr = {}
		x = len(s)
		total = 0
		for i in range(65,91):
			arr[chr(i)] = i-64
		for c in range(x):
			total += arr[s[c]]*(26**(x-c-1))
		return total
