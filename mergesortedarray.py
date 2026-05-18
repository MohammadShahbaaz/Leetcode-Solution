class Solution(object):
    def merge(self, nums1, m, nums2, n):
        a = []
        for i in range(m):
            a.append(nums1[i])
        for j in range(n):
            a.append(nums2[j])
        a.sort()
        nums1[:] = a
        return nums1
        

obj = Solution()
print(obj.merge([1,2,3],3,[2,5,6],3))

[1,2,3,4,0,0,0] m=4 [5,6,7] n = 3
