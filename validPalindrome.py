# Left and right pointer
# class Solution(object):
#     def validPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
        
#         left=False
#         index=0
#         ret=True
#         for i in range((len(s)-1)/2):
#             if not s[i+index]==s[len(s)-1-i]:
#                 if left==False and s[i+1]==s[len(s)-1-i]:
#                     left=True
#                     index=1
#                 else:
#                     ret=False
#                     break
        
#         if ret:
#             return True
        
#         right=False
#         index=0
#         ret=True
#         for i in range((len(s)-1)/2):
#             if not s[i]==s[len(s)-1-i-index]:
#                 if right==False and s[i]==s[len(s)-1-i-1]:
#                     right=True
#                     index=1
#                 else:
#                     ret=False
#                     break
        
#         return ret

# Use Recursion to solve this problem
# class Solution(object):
#     def validPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
        
#         left=0
#         right=len(s)-1
        
#         def valid(left,right,cur):
#             if left==right:
#                 return True
#             if s[left]==s[right]:
#                 if left-right==1:
#                     return True
#                 else:
#                     return valid(left+1,right-1,cur) 
#             elif cur==True:
#                 if left-right==1:
#                     return False
#                 return valid(left+1,right,False) or valid(left,right-1,False)
#             return False
#         return valid(left,right,True)

class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        for i in range(len(s)/2):
            if not s[i]==s[len(s)-1-i]:
                left=s[:i]+s[i+1:]
                right=s[:len(s)-1-i]+s[len(s)-i:]
                return left==left[::-1] or right==right[::-1]
        return True