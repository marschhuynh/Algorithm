import math


class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        sqrt = int(math.sqrt(area))
        print(sqrt)
        if (area % sqrt) == 0:
            L = int(area / sqrt)
            W = area / L
            return [L, W]
        else:
            while (area % sqrt):
                sqrt -= 1
            W = sqrt
            L = area / W
            return [L, W]


print(Solution().constructRectangle(2))
