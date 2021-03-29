# import copy
class Solution(object):
    def reinitializePermutation(self, n):
        """
        :type n: int
        :rtype: int
        """
        initial = [i for i in range(n)]
        arr = [i for i in range(n)]
        num = 0
        while 1 :
            i = 0
            newarr = [0] * len(arr)
            
            for x in arr:
                if i % 2 == 0:
                    newarr[i] = arr[i/2]
                    # print(i/2)
                else:
                    newarr[i] = arr[n/2+(i-1)/2]
                i += 1
                
            arr=copy.copy(newarr)
            num+=1
            if arr==initial:
                break
        
        return num
