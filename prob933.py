class RecentCounter:

    def __init__(self):
        self.pings = []

    def ping(self, t: int) -> int:
        self.pings.append(t)
        while True:
            if self.pings[0] < self.pings[-1]-3000:
                self.pings.pop(0)
            else:
                break
        return len(self.pings)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
