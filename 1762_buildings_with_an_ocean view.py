"""
Building has an ocean view if all the buildings to its right have a smaller height.
Input: heights = [4,2,3,1]
Output: [0,2,3]
Explanation: Building 1 (0-indexed) does not have an ocean view because building 2 is taller.
"""
from typing import List
def findBuildings(heights: List[int]) -> List[int]:
    # 8 6 4 7 2 1
    # maintain a monotonic decreasing stack
    stack = []
    for i in range(len(heights)):
        # case to pop
        while stack and heights[stack[-1]] <= heights[i]:
            stack.pop()
        # push to stack
        stack.append(i)

    return stack


