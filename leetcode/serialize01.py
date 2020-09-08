class TreeNode(object):
    def __init__(self, value):
        self.val = value
        self.right = None
        self.left = None

    def insertLeft(self, value):
        self.left = TreeNode(value)
        return self.left

    def insertRight(self, value):
        self.right = TreeNode(value)
        return self.right


class Codec(object):
    # 序列化
    def serialize(self, root):
        # 二叉树转换为字符串
        def str_tree(node):
            # 判断
            if node:
                vals.append(str(node.val))
                # 递归，深度优先，遍历二叉树左分支
                str_tree(node.left)
                # 递归，深度优先，遍历二叉树右分支
                str_tree(node.right)
            else:
                vals.append("#")
        vals = []
        str_tree(root)
        return ",".join(vals)

    # 反序列化
    def deserialize(self, data):
        # 开始反序列化
        def str_des_tree():
            # 配合迭代器使用
            v = next(val_tree)
            # 判断
            if v == "#":
                return None
            # 二叉树节点
            node = TreeNode(int(v))
            # 二叉树左右分支
            node.left = str_des_tree()
            node.right = str_des_tree()
            return node

        # 迭代器，循环val_tree，从“，”处分割
        val_tree = iter(data.split(","))
        return str_des_tree()

