class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) == 0: return []
        if len(intervals) == 1: return intervals
        res = []
        intervals = sorted(intervals, key=lambda i: i.start)

        for x in range(len(intervals) - 1):
            interval = intervals[x]
            nexInt = intervals[x + 1]

            if (interval.start == nexInt.start):
                res.append(Interval(interval.start, max(nexInt.end, interval.end)))
            else:
                if (interval.end >= nexInt.start):
                    res.append(Interval(interval.start, max(nexInt.end, interval.end)))
                else:
                    res.append(Interval(interval.start, interval.end))
                    res.append(Interval(nexInt.start, nexInt.end))
        return res


    def mergeFast(self, intervals):
        res = []
        if (len(intervals) == 0):
            return res

        intervals = sorted(intervals, key=lambda i : i.start)
        res.append(intervals[0])

        for x in range(1, len(intervals)):
            cur = intervals[x]
            last = res[-1]
            # we either extend
            if last.end >= cur.start:
                last.end = max(last.end, cur.end)
            #append
            else:
                res.append(Interval(cur.start, cur.end))
        return res