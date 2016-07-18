"""
Must be careful about vertical lines and same point

"""


class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if (len(points) == 1):
            return 1

        points = sorted(points, key=lambda k : k.x)

        slopes = {}
        maxPoints = 0
        for x in range(len(points)):
            for j in range(x + 1, len(points)):
                #if (points[x].x == points[j].x and points[x].y == points[j].y):

                slope = self.findSlope(points[x], points[j])

                if slope in slopes:
                    slopes[slope] += 1
                else:
                    slopes[slope] = 1

        for k, v in slopes.items():
            maxPoints = max(v, maxPoints)

        return maxPoints

    def findSlope(self, a, b):
        if (b.x - a.x) == 0:
            return 0
        return (b.y - a.y) / (b.x - a.x)



print(Solution().maxPoints([Point(0,0), Point(1,1), Point(0,0)]))