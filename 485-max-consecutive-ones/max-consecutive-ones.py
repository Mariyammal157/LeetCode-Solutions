class Solution:
    def findMaxConsecutiveOnes(self, nums):
        ans = cur = 0
        for n in nums:
            cur = cur + 1 if n == 1 else 0
            ans = max(ans, cur)
        return ans