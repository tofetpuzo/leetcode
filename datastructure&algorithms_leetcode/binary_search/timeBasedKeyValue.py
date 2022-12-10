class TimeMap:
    def __init__(self) -> None:
        self.store = {} #key: list of [val, timestamp]
    
    
    def set(self, key: str, value: str, timemap: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timemap])
     
    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.store.get(key, [])
        
        # binary search
        l , r = 0 , len(values) - 1
        while l <= r:
            mid = (l+r) // 2
            if values[mid][1] <= timestamp:
                res = values[mid][0]
                l = mid + 1
            else:
                r =  mid - 1
        return res
                
                

# has = ["TimeMap", "set", "get", "get", "set", "get", "get"]

# [[], ["foo", "bar", 1],["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5] ]

# output = [null, null, "bar", "bar", "null", "bar2", "bar2"]

obj = TimeMap()
obj.set("foo", "bar", 1)
obj.set("foo", "bar2", 4)
print(obj.get("foo", 5))