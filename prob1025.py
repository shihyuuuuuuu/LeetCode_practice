class Solution:
    def divisorGame(self, N: int) -> bool:
        # 偶數永遠有個 1 可以減，而奇數只能減另一個奇數把對方變成偶數
        # 結論是偶數贏、奇數輸
        return not N & 1
