# class Solution(object):
#     def minWindow(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: str
#         """
#         def trans(cc):
#             if 'a'<=cc<='z':
#                 return ord(cc)-ord('a')
#             else:
#                 return ord(cc)-ord('A')+ord('z')-ord('a')+1
            
#         remain=[0]*(26+26)
#         deepRemain=[0]*(26+26)
#         cur=[[]for i in range(26*2)]
#         for c in t:
#             trs=trans(c)
#             remain[trs]+=1
#             deepRemain[trs]+=1
                
#         add=0
#         index=0
#         hMin=[]
#         mans=float('inf')
#         curPair=[]
        
#         for c in s:
#             trs=trans(c)
#             if deepRemain[trs]>0:
#                 if remain[trs]>0:
#                     add+=1
#                     remain[trs]-=1
#                 cur[trs].append(index)
#                 heappush(hMin,[index,c])
#                 if add==len(t):
#                     temp=heappop(hMin)
#                     while not temp[0]==cur[trans(temp[1])][len(cur[trans(temp[1])])-deepRemain[trans(temp[1])]]:
#                                                            temp=heappop(hMin)
#                     heappush(hMin,temp)
#                     if index-temp[0]<mans:
#                                 mans=index-temp[0]
#                                 curPair=[temp[0],index]
#             index+=1
        
#         if len(curPair)==0:
#             return ""
#         else:
#             return s[curPair[0]:curPair[1]+1] 

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        def trans(cc):
            if 'a'<=cc<='z':
                return ord(cc)-ord('a')
            else:
                return ord(cc)-ord('A')+ord('z')-ord('a')+1
            
        remain=[0]*(26+26)
        for c in t:
            trs=trans(c)
            remain[trs]+=1
                
        left=0
        right=0
        minAns=float('inf')  
        add=0 
        pair=[]
        
        while 1:
            if add == len(t) and left<right:
                left+=1
                remain[trans(s[left-1])]+=1
                if remain[trans(s[left-1])]>0:
                    add-=1
                if add==len(t) and minAns>-left+right:
                    minAns=-left+right
                    pair=[left,right]
            elif (not add == len(t)) and right<len(s):
                while right<len(s) and (not add==len(t)):
                    if remain[trans(s[right])]>0:
                        add+=1
                    remain[trans(s[right])]-=1
                    right+=1
                if add==len(t) and minAns>-left+right:
                    minAns=-left+right
                    pair=[left,right]
            else:
                break
                    
        if len(pair)==0:
            return ""
        return s[pair[0]:pair[1]]
