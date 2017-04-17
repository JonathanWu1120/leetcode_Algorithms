class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = a.split("+")
        b = b.split("+")
        c = int(a[0])
        d = int(b[0])
        e = int(a[1][:-1])
        f = int(b[1][:-1])
        g = c*d
        h = c*f
        i = e*d
        j = e*f*-1
        k = str(g + j)
        l = str(h + i)
        return k+"+"+l+"i"