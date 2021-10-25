# class Solution(object):
#     def partitionLabels(self, s):
#         """
#         :type s: str
#         :rtype: List[int]
#         """
#         dic=[0]*26
#         cur=[0]*26
#         ret=[]
#         sumCur=0
#         ma=ord('a')
        
#         for i in range(len(s)):
#             dic[ord(s[i])-ma]+=1
#         ans=0
        
#         for i in range(len(s)):
#             mem=ord(s[i])
#             ans+=1
#             dic[mem-ma]-=1
#             if cur[mem-ma]>0:
#                 cur[mem-ma]-=1
#                 sumCur-=1
#             else:
#                 cur[mem-ma]=dic[mem-ma]
#                 sumCur+=dic[mem-ma]
#             if sumCur==0:
#                 ret.append(ans)
#                 ans=0
        
#         return ret
class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        last=[-1]*26
        for i in range(len(s)):
            last[ord(s[i])-ord('a')]=i
        
        curLast=0
        curLen=0
        ret=[]
        for i in range(len(s)):
            if i>curLast:
                ret.append(curLen)
                curLen=0
            curLen+=1
            if last[ord(s[i])-ord('a')]>curLast:
                curLast=last[ord(s[i])-ord('a')]
        
        ret.append(curLen)
        return ret
