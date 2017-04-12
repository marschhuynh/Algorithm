class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        result = []
        for i in findNums:
            index = nums.index(i)
            nextGreaterElement = -1
            for j in range(index+1, len(nums)):
                if i < nums[j]:
                    nextGreaterElement = nums[j]
                    break
            result.append(nextGreaterElement)
        return result
