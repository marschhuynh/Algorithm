class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        SET = set(t) | set(s)
        diff = None
        for c in SET:
            if s.count(c) != t.count(c):
                diff = c
        if diff:
            return False
        else:
            return True
