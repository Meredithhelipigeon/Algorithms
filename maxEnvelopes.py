class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        newList = sorted(envelopes, key=lambda x: (x[0],-x[1]))
        ans = []
        for e in newList:
            if len(ans)==0 or e[1]>ans[-1]:
                ans.append(e[1])
            else:
                k=bisect_right(ans,e[1])
                if not (0<=k-1<len(ans) and ans[k-1] == e[1]):
                    if 0<=k<len(ans):
                        ans[k]=e[1]
                    else:
                        ans[-1]=e[1]
        return len(ans)
