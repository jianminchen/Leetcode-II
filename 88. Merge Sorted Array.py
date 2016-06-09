class Solution(object):
    def merge(self, nums1, m, nums2, n):
        index=m+n-1
        i, j=m-1, n-1
        while index>=0 and i>=0 and j>=0:
            if nums1[i]>nums2[j]:
                nums1[index], nums1[i]=nums1[i], nums1[index]
                i-=1
            else:
                nums1[index], nums2[j]=nums2[j], nums1[index]
                j-=1
            index-=1
        if j>=0:
            nums1[:j+1]=nums2[:j+1]
