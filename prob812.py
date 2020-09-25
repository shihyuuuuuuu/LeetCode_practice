class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        # Brute force by ekron formula(海龍公式)
        def triangleArea(A, B, C):
            a, b, c = list(map(lambda x, y: ((x[0]-y[0])**2 + (x[1]-y[1])**2)**0.5, [A, B, C], [B, C, A]))
            s = (a + b + c) / 2
            return (s*(s-a)*(s-b)*(s-c))**0.5
        biggest = 0
        for i in points:
            for j in points[1:]:
                for k in points[2:]:
                    area = triangleArea(i, j, k)
                    if type(area) is complex:
                        continue
                    biggest = max(biggest, area)
        return biggest
