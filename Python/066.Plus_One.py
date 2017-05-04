class Solution(object):
    def plusOne(self, digits):
        if len(digits) == 1 and digits[0] == 9:
            return [1,0]
        x = digits.pop() + 1
        w = False
        if len(digits) > 0:
            y = 0
            while x == 10 and len(digits) > 0:
                y += 1
                x = digits.pop() + 1
                w = True
            if w == True and x != 10:
                digits.append(x)
            elif w == True and x == 10:
                digits.append(1)
                digits.append(x%10)
            for i in range(y):
                digits.append(0)
        if w == False:
            digits.append(x)
        return digits