class Solution:
    def toGoatLatin(self, S: str) -> str:
        ans = ""
        for cnt, i in enumerate(S.split()):
            if i[0].lower() in ['a', 'e', 'i', 'o', 'u', ]:
                i += 'ma'
            else:
                i = (i + i[0])[1:]
                i += 'ma'
            ans += i + 'a'*(cnt+1) + ' '
        return ans[:-1]
