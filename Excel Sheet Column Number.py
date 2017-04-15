class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum = 0
        s = s.upper()
        s = s[::-1]
        mul = 1
        for i in range(len(s)):
            num = ord(s[i]) - 64
            sum += num * mul
            mul *= 26
        return sum

print(Solution().titleToNumber("ab"))
