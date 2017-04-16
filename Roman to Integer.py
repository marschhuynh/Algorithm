class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "K": 0
        }
        s = s.upper()
        result = 0
        n = len(s)
        s += "K"
        tmp = 0
        for i in range(n):
            if d[s[i]] < d[s[i+1]]:
                tmp += d[s[i]]
            else:
                result += d[s[i]] - tmp
                tmp = 0
        return result

# print(Solution().romanToInt("DCXXI"))
print(Solution().romanToInt("ixdcd"))
