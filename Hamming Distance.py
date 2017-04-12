class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        xor = x ^ y
        xor = list(bin(xor))[2:]
        int_arr = [int(k) for k in xor]
        result = sum(int_arr)
        return result


