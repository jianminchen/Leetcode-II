class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack=[]
        for i in tokens:
            if i=="+":
                temp2=stack.pop()
                temp1=stack.pop()
                stack+=[temp1+temp2]
            elif i=="-":
                temp2=stack.pop()
                temp1=stack.pop()
                stack+=[temp1-temp2]
            elif i=="*":
                temp2=stack.pop()
                temp1=stack.pop()
                stack+=[temp1*temp2]
            elif i=="/":
                temp2=stack.pop()
                temp1=stack.pop()
                if temp1*temp2<0 and temp1%temp2!=0:
                    stack+=[temp1/temp2+1]
                else:
                    stack+=[temp1/temp2]
            else:
                stack+=[int(i)]
        return stack.pop()
