class Solution(object):
    def mkls(self,s):
        arr = []
        for c in s[::-1]:
            arr.append(int(c))
        return arr
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        arr1 = self.mkls(num1)
        arr2 = self.mkls(num2)
        arr3 = []
        a = len(arr1)
        b = len(arr2)
        x = 0
        if a > b:
            for i in range(b):
                s = arr1[i] + arr2[i] + x
                if s >= 10:
                    x = 1
                    arr3.append(s%10)
                elif s < 10:
                    arr3.append(s)
                    x = 0
            for i in range(b,a):
                if arr1[i] + x >= 10:
                    x = 1
                    arr3.append((arr1[i]+x)%10)
                else:
                    arr3.append((arr1[i]+x)%10)
                    x = 0
        elif b > a:
            for i in range(a):
                s = arr1[i] + arr2[i] + x
                if s >= 10:
                    x = 1
                    arr3.append(s%10)
                elif s < 10:
                    arr3.append(s)
                    x = 0
            for i in range(a,b):
                if arr2[i] + x >= 10:
                    x = 1
                    arr3.append((arr2[i]+x)%10)
                else:
                    arr3.append((arr2[i]+x)%10)
                    x = 0
        elif a == b:
            for i in range(a):
                s = arr1[i] + arr2[i] + x
                if s >= 10:
                    x = 1
                    arr3.append(s%10)
                elif s < 10:
                    arr3.append(s)
                    x = 0
        if x == 1:
            s = "1"
        else:
            s = ""
        arr3.reverse()
        c = len(arr3)
        for i in range(c):
            s += str(arr3[i])
        return s