# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


from idlelib.tree import TreeNode
from typing import List


# 迭代方法
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []
        # 用p当做指针
        p = root
        while p or stack:
            # 把左子树压入栈中
            while p:
                stack.append(p)
                p = p.left
            # 输出 栈顶元素
            p = stack.pop()
            res.append(p.val)
            # 看右子树
            p = p.right
        return res




# 递归方法
# class Solution:
#     def inorderTraversal(self, root):
#         res = []
#         def helper(root):
#             if not root:
#                 return 
#             helper(root.left)
#             res.append(root.val)
#             helper(root.right)
#         helper(root)
#         return res
