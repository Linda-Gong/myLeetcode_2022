# 102. Binary tree level order traversal
from collections import deque

def levelOrder(root):
    if not root:
        return []
    queue = deque([root])
    res = []
    while queue:

        level = []
        for i in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        res.append(level)

    return res