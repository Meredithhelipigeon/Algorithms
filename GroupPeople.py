class Solution(object):
    def groupThePeople(self, groupSizes):
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """
        lst = [[] for i in range(len(groupSizes))] 
        ans = []
        i = 0
        for x in groupSizes:
            (lst[x-1]).append(i)
            if(len(lst[x-1]) == x):
                ans.append(lst[x-1])
                lst[x-1]=[]
            i+=1
        return ans
