class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        arr = [0]*256
        for i in s:
            arr[ord(i)] += 1
        have_one = 0
        count = 0
        for i in s:
            if arr[ord(i)] > 0:
                if arr[ord(i)] % 2 == 1:
                    have_one = 1
                count += (arr[ord(i)] / 2) * 2
                arr[ord(i)] = 0
        return count + have_one


print(Solution().longestPalindrome("abccccdd"))
