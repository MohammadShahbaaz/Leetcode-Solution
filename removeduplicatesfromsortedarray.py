class Solution(object):
    def removeDuplicates(self,nums):
        a = 1
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[a] = nums[i]
                a+=1
        return a



obj = Solution()
print(obj.removeDuplicates([0,0,0,1,1,1,2,2,2,3,3,4]))






#nums = [1,1,1]