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
        

