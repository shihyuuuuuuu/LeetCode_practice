class Solution:
    def toLowerCase(self, str: str) -> str:
        ans = ""
        for i in str:
            ans += chr(ord(i)+32) if ord(i) >= 65 and ord(i) <= 90 else i
        return ans
    
        # return str.lower()
