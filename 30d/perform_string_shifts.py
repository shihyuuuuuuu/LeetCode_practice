# https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/529/week-2/3299/
class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        all_shift = 0
        for i in shift:
            if i[0]:
                all_shift += i[1]
            else:
                all_shift -= i[1]
        if all_shift < 0:
            all_shift = len(s) + all_shift
        return s[-all_shift % len(s):] + s[:-all_shift % len(s)]
