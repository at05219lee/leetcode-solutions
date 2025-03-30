#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        leaf_depth = []

        stack = []
        stack.append((root, 1))

        while len(stack):
            top_node, depth = stack.pop()

            if top_node.right is None and top_node.left is None:
                leaf_depth.append(depth)

            if top_node.right:
                stack.append((top_node.right, depth + 1))
            if top_node.left:
                stack.append((top_node.left, depth + 1))

        return min(leaf_depth)



            

        
# @lc code=end

