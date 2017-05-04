class Solution(object):
	def convertToBase7(self,num):
		arr = ""
		n = False
		if num == 0:
		    return "0"
		if num < 0: 
		    n = True
		    num = num * -1
		while num > 0:
			x = num % 7
			arr += str(int(x))
			num -= x
			num = num / 7
		if n == True:
		    return "-" + arr[::-1]
		return arr[::-1]