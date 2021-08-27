class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        if preorder[0]=='#':
            if preorder=="#":
                return True
            else:
                return False
        leftStack=[[preorder[0],'L']]
        num=len(preorder)
        l=preorder.split(',')
        l=l[1:]
        for o in l:
            if len(leftStack)==0:
                return False
            else:
                if o=='#':
                    if leftStack[-1][1]=='L':
                        leftStack[-1][1]='R'
                    else:
                        while len(leftStack)!=0 and leftStack[-1][1]=='R':
                                leftStack.pop()
                        if len(leftStack)!=0 and leftStack[-1][1]=='L':
                            leftStack[-1][1]='R'
                else:
                    leftStack.append([o,'L'])
        if len(leftStack)==0:
                   return True
        else:
                   return False
