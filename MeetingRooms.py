
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """



        # for i in lst:
        #     print i.start, i.end
        # res.append(lst[0])
        # minEnd = lst[0].end
        #
        # for n in lst[1:]:
        #     if res[-1].start == n.start:
        #         res.append(n)
        #         minEnd = min(minEnd, n.end)
        #     elif n.start >= minEnd:
        #         res[-1].end = n.end
        #         minEnd = n.end
        #     else:
        #         res.append(n)
        #         minEnd = min(minEnd, n.end)
        if len(intervals) == 0:
            return 0

        start = sorted(intervals, key=lambda x : x.start)
        end = sorted(intervals, key=lambda x:x.end)

        curActive = 0
        maxRooms = 0
        sIndx = 0
        eIndx = 0

        while sIndx < len(start) and eIndx < len(end):
            if start[sIndx].start <= end[eIndx].end:
                curActive+=1
                if curActive > maxRooms:
                    maxRooms = curActive

                sIndx += 1
            else:
                curActive -= 1
                eIndx+=1

        return maxRooms







print Solution().minMeetingRooms([Interval(5,8),Interval(6,8)])