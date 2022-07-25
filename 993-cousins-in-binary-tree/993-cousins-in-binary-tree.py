# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def find(self, root, parent, value, depth=0):
            # Find node with the request value and return its parent node
            if not root:
                return None, depth

            if root.val == value:
                return parent, depth

            lparent, ldepth = self.find(root.left, root, value, depth+1)

            if lparent:
                return lparent, ldepth

            return self.find(root.right, root, value, depth+1)

    def isCousins(self, root, x, y):
        xparent, xdepth = self.find(root, None, x)
        yparent, ydepth = self.find(root, None, y)

        return xdepth == ydepth and xparent != yparent        