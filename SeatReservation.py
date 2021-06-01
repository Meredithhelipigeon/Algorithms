class SeatManager:

    def __init__(self, n: int):
        self.seats=[i for i in range(n)]
        heapify(self.seats)
        

    def reserve(self) -> int:
        return heappop(self.seats)+1
        

    def unreserve(self, seatNumber: int) -> None:
        heappush(self.seats,seatNumber-1)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
