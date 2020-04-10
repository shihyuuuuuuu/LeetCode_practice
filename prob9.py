class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        for i, j in zip(x[:len(x)//2], x[::-1][:len(x)//2]):
            if i != j:
                return False
        return True
