class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        even = [sum(x if not x & 1 else 0 for x in A)]
        for i in queries:
            if A[i[1]] & 1:
                even.append(even[-1] + A[i[1]] + i[0] if i[0] & 1 else even[-1])
            else:
                even.append(even[-1] - A[i[1]] if i[0] & 1 else even[-1] + i[0])
            A[i[1]] += i[0]
        return even[1:]
