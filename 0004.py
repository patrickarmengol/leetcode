class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        a, b = (nums1, nums2) if len(nums1) < len(nums2) else (nums2, nums1)
        total_length = len(a) + len(b)
        half = total_length // 2

        lo_a, hi_a = 0, len(a) - 1
        while True:
            mid_a = (lo_a + hi_a) // 2
            mid_b = half - mid_a - 2

            left_a = a[mid_a] if mid_a >= 0 else float("-infinity")
            right_a = a[mid_a + 1] if mid_a + 1 < len(a) else float("infinity")
            left_b = b[mid_b] if mid_b >= 0 else float("-infinity")
            right_b = b[mid_b + 1] if mid_b + 1 < len(b) else float("infinity")

            if left_a <= right_b and left_b <= right_a:  # found sol
                if total_length % 2 != 0:  # odd - median is lowest of right side
                    return min(right_a, right_b)
                else:  # even - median is avg of highest of left and lowest of right
                    return (max(left_a, left_b) + min(right_a, right_b)) / 2
            elif left_a > right_b:  # adjust part of small array to left
                hi_a = mid_a - 1
            else:  # adjust part of small array to right
                lo_a = mid_a + 1
