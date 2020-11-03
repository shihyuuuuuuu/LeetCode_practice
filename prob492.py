class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        sqrt = math.ceil(area ** 0.5)
        while True:
            if area % sqrt == 0:
                return [sqrt, area // sqrt]
            sqrt += 1
