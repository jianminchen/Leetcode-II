class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1)==0 or len(nums2)==0:
            return []
        s1=set(nums1)
        s2=set(nums2)
        return list(s1 & s2)
