class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        index = 0
        for i in range(n):
            if nums[i] != 0:
                if i != index:
                    nums[i], nums[index] = nums[index], nums[i]
                    nums[i] = 0
                index += 1


a = [0, 0, 0, 1, 2, 0, 0, 0, 7, 0, 0, 9]
Solution().moveZeroes(a)
print(a)
