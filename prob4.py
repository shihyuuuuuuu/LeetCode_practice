class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        cnt1 = 0
        cnt2 = 0
        arr = []
        
        while(True):
            if cnt1 == m:
                arr += nums2[cnt2:]
                break
            if cnt2 == n:
                arr += nums1[cnt1:]
                break
            if nums1[cnt1] <= nums2[cnt2]:
                arr.append(nums1[cnt1])
                cnt1 += 1
            else:
                arr.append(nums2[cnt2])
                cnt2 += 1
        return arr[int((m+n)/2)] if (m+n)&1 else (arr[int((m+n)/2)] + arr[int((m+n)/2 - 1)])/2
