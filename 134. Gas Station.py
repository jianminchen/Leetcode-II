class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        for i in xrange(len(gas)):
            tank=gas[i]
            check=1
            for j in xrange(i+1,len(gas)):
                tank-=cost[j-1]
                if tank<0:
                    check=0
                    break
                tank+=gas[j]
            if check:
                for j in xrange(i+1):
                    if j==0:
                        tank-=cost[len(cost)-1]
                    else:
                        tank-=cost[j-1]
                    if tank<0:
                        check=0
                        break
                    tank+=gas[j]
            if check:
                return i
        return -1
