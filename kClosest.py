# class Solution(object):
#     def kClosest(self, points, k):
#         """
#         :type points: List[List[int]]
#         :type k: int
#         :rtype: List[List[int]]
#         """
#         h=[]
#         capacity=k
#         for p in points:
#             c=p[0]**2+p[1]**2
#             if len(h) < k:
#                 heapq.heappush(h, [-c,p])
#             else:
#                 heapq.heappushpop(h, [-c,p])
#         ret=[]
#         for i in range(capacity):
#             ret.append(heapq.heappop(h)[1])
#         return ret

class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        h=[]
        for p in points:
            c=p[0]**2+p[1]**2
            heapq.heappush(h, [c,p])
                
        ret=[]
        for i in range(k):
            ret.append(heapq.heappop(h)[1])
        return ret
