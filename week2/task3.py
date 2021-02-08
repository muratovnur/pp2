class Solution(object):
    def numIdenticalPairs(self, nums):
        x = 0
        i = 0
        while i < len(nums):
            j = i + 1
            while j < len(nums):
                if nums[i] == nums[j]:
                    x += 1
        return x
a = Solution()
print(a.numIdenticalPairs([1,2,3,1,1,3]))