import queue
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        remainders = [[] for i in range(16)]
        
        def check_predecessor(a,b):
            j = 0
            count = False
            for i in range(len(b)):
                if len(a)==j or a[j]!=b[i]:
                    if count:
                        return False
                    count = True
                else:
                    j+=1
            return True
        
        for w in words:
            remainders[len(w)-1].append(w)  
        q = []
        chainCount = 1
        for i in range(16):
            nq = []
            wordDict = {}
            for pair in q:
                w, steps = pair
                for nextw in remainders[i]:
                    if check_predecessor(w,nextw):
                        if nextw in wordDict:
                            wordDict[nextw] = max(steps+1,wordDict[nextw])
                        else:
                            wordDict[nextw] = steps+1
            for w in remainders[i]:
                if not w in wordDict:
                    nq.append([w,1])
                else:
                    nq.append([w,wordDict[w]])
                    chainCount = max(chainCount,wordDict[w])
            q=nq

        return chainCount
