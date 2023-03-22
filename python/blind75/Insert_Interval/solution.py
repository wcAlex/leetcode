from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        cur, end, res = 0, len(intervals), []

        while cur < end and newInterval[0] > intervals[cur][1]:
            res.append(intervals[cur])
            cur += 1
        if cur == end:
            res.append(newInterval)
            return res

        b = min(newInterval[0], intervals[cur][0])
        
        while cur < end and newInterval[1] > intervals[cur][1]:
            cur += 1

        if cur == end:
            res.append([b, newInterval[1]])
            return res
        
        if newInterval[1] >= intervals[cur][0]:
            res.append([b, intervals[cur][1]])
            cur += 1
        else:
            res.append([b, newInterval[1]])
        
        if cur < end:
            res.extend(intervals[cur:])

        return res
    
    # More compact version
    def insert2(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n, res = newInterval, []

        for idx, val in enumerate(intervals):
            if val[1] < n[0]:
                res.append(val)
            elif n[1] < val[0]:
                res.append(n)
                res.extend(intervals[idx:])
                return res
            else:
                n[0] = min(n[0], val[0])
                n[1] = max(n[1], val[1])
        
        res.append(n)
        return res
    
    # another interesting idea, work on index. 
    # Collect the intervals strictly left or right of the new interval, 
    # then merge the new one with the middle ones (if any) before inserting it between left and right ones.
    # def insert(self, intervals, newInterval):
    #     s, e = newInterval.start, newInterval.end
    #     left, right = [], []
    #     for i in intervals:
    #         if i.end < s:
    #             left += i,
    #         elif i.start > e:
    #             right += i,
    #         else:
    #             s = min(s, i.start)
    #             e = max(e, i.end)
    #     return left + [Interval(s, e)] + right

    # def insert2(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    #     res, n = [], newInterval
    #     for index, i in enumerate(intervals):
    #         if i.end < n.start:
    #             res.append(i)
    #         elif n.end < i.start:
    #             res.append(n)
    #             return res+intervals[index:]  # can return earlier
    #         else:  # overlap case
    #             n.start = min(n.start, i.start)
    #             n.end = max(n.end, i.end)
    #     res.append(n)
    #     return res