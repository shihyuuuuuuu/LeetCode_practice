class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        up = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'u', 'i', 'o', 'p']
        mid = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
        down = ['z', 'x', 'c', 'v', 'b', 'n', 'm']
        ans = []
        
        for word in words:
            c = word[0].lower()
            row = up if c in up else mid if c in mid else down
            samerow = True
            for i in word:
                if i.lower() not in row:
                    samerow = False
                    break
            if samerow:
                ans.append(word)
        return ans
