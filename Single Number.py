class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr = set()
        for num in nums:
            arr.add(num) if num not in arr else arr.remove(num)
        return arr.pop()

print(Solution().singleNumber([1,4,2,3,1,5,3,2,5]))
