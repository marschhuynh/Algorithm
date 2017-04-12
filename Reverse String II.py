import math


class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        result = ""
        part = int(math.ceil(len(s)/(2.0*k)))
        arr = [s[i*2*k:i*2*k+2*k] for i in range(part)]
        for item in arr:
          result += item[:k][::-1] + item[k:]

        return result

