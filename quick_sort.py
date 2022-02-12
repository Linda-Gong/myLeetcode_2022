def quick_sort(nums):
    if len(nums)<=1:
        return nums

    pivot = nums.pop()
    greater, smaller = [], []
    for num in nums:
        if num > pivot:
            greater.append(num)
        else:
            smaller.append(num)

    return quick_sort(smaller) + [pivot] + quick_sort(greater)


# [5,6,8,2,3,5,9,4,6]

a = quick_sort([5,6,8,2,3,5,9,4,6])
print(a)