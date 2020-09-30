class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        letter = ""
        start_end = []
        for cnt, i in enumerate(S):
            if i not in letter:
                letter += i
                start_end.append([cnt, cnt])
            else:
                start_end[letter.index(i)][1] = cnt
        last = [-1, -1]
        ans = []
        for i in start_end:
            if i[0] > last[1]:
                ans.append(i[1]-i[0]+1)
                last = i
            else:
                if i[1] > last[1]:
                    ans[-1] = i[1] - last[0] + 1
                    last[1] = i[1]
        return ans
    
        # Greater solution:
        # https://leetcode.com/problems/partition-labels/discuss/298474/Python-two-pointer-solution-with-explanation
