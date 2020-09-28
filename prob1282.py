class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = {}
        for uid, i in enumerate(groupSizes):
            groups[i] = groups.get(i, [])
            groups[i].append(uid)
        return [groups[i][j:j+i] for i in groups for j in range(0, len(groups[i]), i)]
