# class StockPrice(object):

#     def __init__(self):
#         self.dict=dict()
#         self.last="-inf"
#         self.maxT=-1
#         self.maxV=float('-inf')
#         self.minV=float('inf')
        
#     def update(self, timestamp, price):
#         """
#         :type timestamp: int
#         :type price: int
#         :rtype: None
#         """
#         if price > self.maxV:
#             self.maxV=price
#         if price < self.minV:
#             self.minV=price
#         if self.dict.get(timestamp):
#             if self.dict[timestamp] == self.maxV or self.dict[timestamp] == self.minV:
#                 self.dict[timestamp]=price
#                 pp=list(self.dict.values())
#                 self.maxV=pp[0]
#                 self.minV=pp[0]
#                 for i in pp:
#                     if i>self.maxV:
#                         self.maxV=i
#                     if i<self.minV:
#                         self.minV=i
#         self.dict[timestamp]=price
#         if self.maxT<=timestamp:
#             self.last=price
#             self.maxT=timestamp
        

#     def current(self):
#         """
#         :rtype: int
#         """
#         return self.last

#     def maximum(self):
#         """
#         :rtype: int
#         """
#         return self.maxV
        

#     def minimum(self):
#         """
#         :rtype: int
#         """
#         return self.minV


# # Your StockPrice object will be instantiated and called as such:
# # obj = StockPrice()
# # obj.update(timestamp,price)
# # param_2 = obj.current()
# # param_3 = obj.maximum()
# # param_4 = obj.minimum()

class StockPrice(object):

    def __init__(self):
        self.dict=dict()
        self.last=float('-inf')
        self.maxT=-1
        self.maxHeap=[]
        self.minHeap=[]
        
    def update(self, timestamp, price):
        """
        :type timestamp: int
        :type price: int
        :rtype: None
        """
        
        heapq.heappush(self.maxHeap, [-price,timestamp])
        heapq.heappush(self.minHeap, [price,timestamp])
        self.dict[timestamp]=price
        if self.maxT<=timestamp:
            self.last=price
            self.maxT=timestamp
        

    def current(self):
        """
        :rtype: int
        """
        return self.last

    def maximum(self):
        """
        :rtype: int
        """
        l=heapq.heappop(self.maxHeap)
        price=l[0]
        timestamp=l[1] 
        
        while not -price==self.dict[timestamp]:
            l=heapq.heappop(self.maxHeap)
            price=l[0]
            timestamp=l[1] 
        
        heapq.heappush(self.maxHeap, [price,timestamp])
        return -price
        

    def minimum(self):
        """
        :rtype: int
        """
        l=heapq.heappop(self.minHeap)
        price=l[0]
        timestamp=l[1] 
        while not price==self.dict[timestamp]:
            l=heapq.heappop(self.minHeap)
            price=l[0]
            timestamp=l[1] 
        
        heapq.heappush(self.minHeap, [price,timestamp])
        return price


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
