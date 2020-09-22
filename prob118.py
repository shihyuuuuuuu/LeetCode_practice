class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        def pascal(n, l):
            if n == 0:
                pass
            elif n <= 2:
                l.append([1] * n)
            else:
                l.append([1] + [l[-1][i] + l[-1][i+1] for i in range(len(l[-1])-1)] + [1])
            if n + 1 <= numRows:
                pascal(n+1, l)
            return l
        return pascal(0, [])

        # Another solution
        # Consider that we can get the next row by shifting the previous row
        # Example:
        #   1 3 3 1 0
        # + 0 1 3 3 1
        #   1 4 6 4 1
