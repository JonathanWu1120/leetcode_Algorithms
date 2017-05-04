class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        num = '{0:032b}'.format(n)
        rev = num[::-1]
        return int(rev,2)