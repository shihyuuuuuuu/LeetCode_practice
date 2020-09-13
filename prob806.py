class Solution:
    def numberOfLines(self, widths: List[int], S: str) -> List[int]:
        line_cnt = 1
        units = 0
        for i in S:
            new_added = widths[ord(i)-97]
            if units + new_added <= 100:
                units += new_added
            else:
                line_cnt += 1
                units = new_added
        return [line_cnt, units]
