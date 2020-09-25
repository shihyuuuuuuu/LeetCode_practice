"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        d = {}
        for i in employees:
            d[i.id] = [i.importance, i.subordinates]
        subs = [id]
        def DFS(subs, imp):
            if not subs:
                return imp
            for i in subs:
                imp += d[i][0]
                imp = DFS(d[i][1], imp)
            return imp
        return DFS(subs, 0)

