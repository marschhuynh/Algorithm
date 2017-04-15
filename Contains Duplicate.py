class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        S = set()

        for i in nums:
            if i in S:
                return True
            else:
                S.add(i)
        return False

a = [3, 3]

print(Solution().containsDuplicate(a))
