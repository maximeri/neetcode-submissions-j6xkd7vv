class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals

        # sort by interval[0] and then interval[1]
        intervals.sort(key=lambda x: (x[0], x[1]))

        res = []
        newInterval = intervals[0]
        for i in range(1, len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                newInterval = intervals[i]
            else:
                ns, ne = min(newInterval[0], intervals[i][0]), max(intervals[i][1], newInterval[1])
                newInterval = [ns, ne]

        if newInterval not in res:
            res.append(newInterval)

        return res