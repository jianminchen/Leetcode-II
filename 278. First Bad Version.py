# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start=1
        end=n
        while start<=end:
            mid=(start+end)>>1
            if mid>1:
                if isBadVersion(mid) and isBadVersion(mid-1):
                    end=mid-1
                elif not isBadVersion(mid) and not isBadVersion(mid+1):
                    start=mid+1
                else:
                    if isBadVersion(mid):
                        return mid
                    else:
                        return mid+1
            else:
                if isBadVersion(mid):
                    return mid
                else:
                    return mid+1
