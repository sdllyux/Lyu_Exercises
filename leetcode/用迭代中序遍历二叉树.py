from idlelib.tree import TreeNode
from typing import List


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 创建一二叉树
def creatBTree(data, index):
    pNode = None
    if index < len(data):
        # if data[index] == None:
        #     return
        pNode = TreeNode(data[index])
        pNode.left = creatBTree(data, 2 * index + 1)
        pNode.right = creatBTree(data, 2 * index + 2)
    return pNode


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
        return print(res)


if __name__ == "__main__":
    data = [1, 2, 7, 3]
    pNode = creatBTree(data, 0)
    sl = Solution()
    sl.inorderTraversal(pNode)
