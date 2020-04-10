class Solution:
    def romanToInt(self, s: str) -> int:
        num_dict = { 'A':0, 'I':1, 'V':5 , 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000 }
        s += 'A'
        ans = 0
        for index, c in enumerate(s[:-1]):
            if(num_dict[c] < num_dict[s[index+1]]):
                ans -= num_dict[c]
            else:
                ans += num_dict[c]
        return ans
