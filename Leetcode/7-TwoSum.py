class Solution(object):
    def twoSum(self, nums, target):
        for i in range(0 , len(nums) - 1):
            for j in range(1, len(nums)):
                complement = target - nums[i]
                if(nums[j] == complement):
                    print(i, j)

obj = Solution()
nums = [2,7,11,15]
target = 9
obj.twoSum(nums, target)