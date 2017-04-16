class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        n = len(g)
        m = len(s)
        i = 0
        j = 0
        result = 0
        while (i < n):
            while (j < m and g[i] > s[j]):
                j += 1
            if (j < m):
                result += 1
            i += 1
            j += 1
        return result


a = [1, 2, 3]
b = [1,1]

print(Solution().findContentChildren(a, b))
