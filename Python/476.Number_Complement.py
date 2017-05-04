class Solution(object):
    def findComplement(self, num):
        nu = "{0:b}".format(num)
        a = list(nu)
        for i in range(len(a)):
            if a[i] == "1":
                a[i] = "0"
            else:
                a[i] = "1"
        b = "".join(a)
        return int(b,2)