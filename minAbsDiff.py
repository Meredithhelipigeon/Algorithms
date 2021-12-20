class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr = sorted(arr)
        minAbs = float('inf')
        last=arr[0]
        
        for i in range(1,len(arr)):
            if abs(arr[i] - last) < minAbs:
                minAbs = abs(arr[i] - last)
            last=arr[i]
        
        ret=[]
        last=arr[0]
        for i in range(1,len(arr)):
            if arr[i] - last == minAbs:
                ret.append([last,arr[i]])
            last=arr[i]
            
        return ret
        
