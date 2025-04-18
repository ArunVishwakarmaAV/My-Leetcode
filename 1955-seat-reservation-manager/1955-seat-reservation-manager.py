class SeatManager:

    def __init__(self, n: int):
        self.d=[]
        for i in range(1,n+1):
            heapq.heappush(self.d,i)

    def reserve(self) -> int:
        return heapq.heappop(self.d) 

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.d,seatNumber)
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)