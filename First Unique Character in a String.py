class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = [0]*256
        for i in s:
            count[ord(i)] += 1
        i = 0
        while i < len(s):
            if count[ord(s[i])] == 1:
                return i
            i += 1
        return -1

print(Solution().firstUniqChar("aabbcc"))
