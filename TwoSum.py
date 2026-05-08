class Solution(object):
    def twoSum(self,nums, target):
        seen = {}

        for i, num in enumerate(nums):
            diff = target - num

            if diff in seen:
                return [seen[diff], i]

            seen[num] = i


obj = Solution()
print(obj.twoSum([1,2,3,4,5,6,7],8))
print([1,2,3,4,5,6,7])