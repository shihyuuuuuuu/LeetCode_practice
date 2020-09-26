class Solution:
    def rotatedDigits(self, N: int) -> int:
        mapping = {'0':'0', '1':'1', '2':'5', '3':'a', '4':'a', '5':'2', '6':'9', '7':'a', '8':'8', '9':'6'}
        
        def isgood(s):
            if '3' in s or '4' in s or '7' in s:
                return False
            rotate = ''.join(mapping[i] for i in s)
            return s != rotate
        
        return sum(isgood(str(n)) for n in range(1, N+1))
