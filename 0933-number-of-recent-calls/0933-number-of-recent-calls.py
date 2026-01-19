class RecentCounter:

    def __init__(self):
        self.requests = []

    def ping(self, t: int) -> int:
        self.requests.append(t)
        frame = [t-3000,t]
        res = []
        for c in self.requests:
            if c>= frame[0] and c<=frame[1]:
                res.append(c)
        
        return len(res)

        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)