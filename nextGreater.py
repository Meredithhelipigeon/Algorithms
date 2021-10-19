class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nextDict, stack={},[]
        
        for nn in nums2:
            while stack and stack[-1]<nn:
                nextDict[stack.pop()]=nn
            stack.append(nn)
            
        return [nextDict.get(nn,-1) for nn in nums1]
