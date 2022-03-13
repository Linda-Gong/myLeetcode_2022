"""
https://leetcode.com/problems/binary-tree-vertical-order-traversal/
Example 1:
see figure in leetcode 314. Binary Tree Vertical Order Traversal

Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]

"""
from collections import defaultdict
from collections import deque
def verticalOrder(root):
    if not root:
        return []
    columns = defaultdict(list)
    queue = deque([(root, 0)])
    max_col, min_col = 0, 0
    while queue:
        node, col = queue.pop()
        if node:
            columns[col].append(node.val)
            queue.append((node.left, col-1))
            queue.append((node.right, col+1))
            max_col = max(max_col, col)
            min_col = min(min_col, col)

    res = []
    for i in range(min_col, max_col+1):
        res.append(columns[i])

    return res
