class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        a = "".join(map(lambda x: '1' if x =='0' else '0', bin(num)[2:]))
        return int(a, 2)

