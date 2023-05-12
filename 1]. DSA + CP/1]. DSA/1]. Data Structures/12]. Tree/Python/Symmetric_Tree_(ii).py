# Symmetric Tree - Iteration
# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

import queue


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root) -> bool:

        if root.left is None and root.right is None:
            return True
        elif root.left is None:
            return False
        elif root.right is None:
            return False

        q = queue.Queue()
        q.put(root.left)
        q.put(root.right)
        while not q.empty():
            right_root = q.get()
            left_root = q.get()
            # print(left_root, right_root)

            if right_root is None and left_root is None:
                continue
            elif (
                right_root is None
                or left_root is None
                or (right_root.val != left_root.val)
            ):
                return False
            q.put(left_root.left)
            q.put(right_root.right)
            q.put(left_root.right)
            q.put(right_root.left)
        return True

# Time Complexity: O(N)
# Space Complexity: O(N)
