class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        result = []
        mun = abs(num)
        if num == 0:
            return "0"
        while mun > 0:
            mod = mun % 7
            result.insert(0, mod)
            mun /= 7
        result = map(lambda x: str(x), result)
        result = "".join(result)
        if num < 0:
            result = "-" + result
        return result

print(Solution().convertToBase7(0))
