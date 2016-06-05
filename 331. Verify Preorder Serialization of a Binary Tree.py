class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        preorder=preorder.split(',')
        degree_difference=1 #root
        for i in xrange(len(preorder)):
            degree_difference-=1
            if degree_difference<0:
                return False
            if preorder[i]!=u'#':
                degree_difference+=2
        return degree_difference==0
