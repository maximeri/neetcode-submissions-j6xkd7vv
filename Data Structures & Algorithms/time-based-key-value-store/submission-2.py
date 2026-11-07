class TimeMap:
    # { alice: [(1, "happy"), (2, "yes")] }
    def __init__(self):
        self.hashMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashMap:
            return ""

        res = self.binarySearch(self.hashMap[key], timestamp)
        if self.hashMap[key][res][0] <= timestamp:
            return self.hashMap[key][res][1]
        else:
            return ""


    def binarySearch(self, arr: list, target) -> mix:
        l, r = 0, len(arr) - 1
        res = -1

        while l <= r:
            m = (l + r) // 2
            if arr[m][0] == target:
                return m
           
            if arr[m][0] < target:
                res = m
                l = m + 1
            else:
                r = m - 1

        return res
        



