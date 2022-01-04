import heapq as hq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        h = []
        for i in range(k-1):
            hq.heappush(h,[-nums[i],i])
        
        ret = []
        for j in range(k-1,len(nums)):
            hq.heappush(h,[-nums[j],j])
            cur,curPos = hq.heappop(h)
            while curPos <= j-k:
                cur,curPos = hq.heappop(h)
            hq.heappush(h,[cur,curPos])
            ret.append(-cur)
        
        return ret
