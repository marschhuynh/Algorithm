class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        n = len(nums)
        c = zip(range(n), nums)
        c.sort(lambda a,b: b[1] - a[1])
        result = list(range(n))
        for i in range(n):
            nums[c[i][0]] = str(i + 1)
        try:
            nums[c[0][0]] = "Gold Medal"
            nums[c[1][0]] = "Silver Medal"
            nums[c[2][0]] = "Bronze Medal"
        except:
            pass
        return nums


print(Solution().findRelativeRanks([1,3,1,3,5,6,]))
