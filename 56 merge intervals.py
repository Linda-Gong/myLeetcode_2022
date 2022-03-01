def merge(intervals):
    intervals.sort()
    merge = []

    for item in intervals:
        if not merge or merge[-1][1] < item[0]:
            merge.append(item)
        else:
            merge[-1][1] = max(merge[-1][1], item[1])

    return res