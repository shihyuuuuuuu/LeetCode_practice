class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        return self.convert(self.countAndSay(n-1))
    
    def convert(self, s):
        s += 'a'
        now = ""
        cnt = 0
        ret = ""
        for i in s:
            if i == now:
                cnt += 1
            else:
                ret += str(cnt) + now
                now = i
                cnt = 1
        return ret[1:]
