class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        subd = {}
        for i in cpdomains:
            s = i.split()
            v = int(s[0])
            d = s[1]
            if d not in subd:
                subd[d] = v
            else:
                subd[d] = subd[d] + v
            while '.' in d:
                d = d[d.find('.') + 1:]
                if d not in subd:
                    subd[d] = int(v)
                else:
                    subd[d] = subd[d] + v
        
        ans = []
        for i in subd:
            ans.append(str(subd[i]) + " " + i)
        return ans
