class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        steps = 0
        for i in range(len(points)-1):
            x = abs(points[i+1][0]-points[i][0])
            y = abs(points[i+1][1]-points[i][1])
            steps += min(x, y) + abs(x-y)
        return steps
