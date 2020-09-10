class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greaters = {}
        for cnt, i in enumerate(nums2):
            if i in nums1:
                next_greaters[i] = -1
                for j in nums2[cnt+1:]:
                    if j > i:
                        next_greaters[i] = j
                        break
        return [next_greaters[i] for i in nums1]
