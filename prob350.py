class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        a = b = 0
        ans = []
        while a < len(nums1) and b < len(nums2):
            if nums1[a] == nums2[b]:
                ans.append(nums1[a])
                a += 1
                b += 1
            elif nums1[a] < nums2[b]:
                a += 1
            else:
                b += 1
        return ans
