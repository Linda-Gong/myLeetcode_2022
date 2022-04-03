
def merge( nums1, m: int, nums2, n: int) :
    """
    Do not return anything, modify nums1 in-place instead.
    """

    # if m == 0:
    #     nums1[:n] = nums2[:n]

    while m > 0 and n > 0:
        if nums1[ m -1] > nums2[ n -1]:
            nums1[ m + n -1] = nums1[ m -1]
            m -= 1
        else:
            nums1[ m + n -1] = nums2[ n -1]
            n -= 1

    nums1[:n] = nums2[:n]
nums1 = [2, 4, 8, 0, 0,0,0,0]
m = 3
nums2 = [1, 6,0,0]
n = 2
merge(nums1, m, nums2, n)
print(nums1)