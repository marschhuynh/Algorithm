class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        SET = set(t) or set(s)
        for c in SET:
            if s.count(c) != t.count(c):
                return c


print(Solution().findTheDifference("abcd", "abcde"))
