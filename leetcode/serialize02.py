# Definition for a binary tree node.
"""
先序方法
"""
class TreeNode(object):
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

    def insertLeft(self, value):
        self.left = TreeNode(value)
        return self.left

    def insertRight(self, value):
        self.right = TreeNode(value)
        return self.right


class Codec:
    flag = -1

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        s = ""
        s = self.recursionSerialize(root, s)
        print(s)
        return s

    def recursionSerialize(self, root, s):
        if (root is None):
            s = '$,'
            return s
        s = str(root.val) + ','
        left = self.recursionSerialize(root.left, s)
        right = self.recursionSerialize(root.right, s)
        s += left + right
        return s

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        self.flag += 1
        l = data.split(',')
        if (self.flag >= len(data)):
            return None
        root = None
        if (l[self.flag] != '$'):
            root = TreeNode(int(l[self.flag]))
            root.left = self.deserialize(data)
            root.right = self.deserialize(data)
        return root


# Your Codec object will be instantiated and called as such:
if __name__ == '__main__':
    root = TreeNode('1')
    A = root.insertLeft('2')
    B = root.insertRight('3')
    C = B.insertLeft('4')
    D = B.insertRight('5')

    codec = Codec()
    # codec.serialize(root)
    codec.deserialize(codec.serialize(root))



