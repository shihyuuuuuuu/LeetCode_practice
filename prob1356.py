class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]: 
        # Write a merge sort sorting by two keys
        def mySort(ones, origin):
            if len(ones) == 1:
                return ones, origin
            mid = len(ones)//2
            left, lorg = mySort(ones[:mid], origin[:mid])
            right, rorg = mySort(ones[mid:], origin[mid:])
            lp, rp = 0, 0
            merged = []
            morg = []
            while lp != len(left) and rp != len(right):
                if left[lp] < right[rp]:
                    merged.append(left[lp])
                    morg.append(lorg[lp])
                    lp += 1
                elif left[lp] > right[rp]:
                    merged.append(right[rp])
                    morg.append(rorg[rp])
                    rp += 1
                elif lorg[lp] <= rorg[rp]:
                    merged.append(left[lp])
                    morg.append(lorg[lp])
                    lp += 1
                else:
                    merged.append(right[rp])
                    morg.append(rorg[rp])
                    rp += 1
            if lp < len(left):
                merged += left[lp:]
                morg += lorg[lp:]
            if rp < len(right):
                merged += right[rp:]
                morg += rorg[rp:]
            return merged, morg
        
        return mySort([bin(i)[2:].count('1') for i in arr], arr)[1]
    
        # Another solution using "sorted" by two keys
        return sorted(arr, key=lambda x: (bin(x)[2:].count('1'), x))
