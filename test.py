class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def insert(root, val):

    if root is None:
        return TreeNode(val)

    if val < root.val:
        root.left = insert(root.left, val)

    else:
        root.right = insert(root.right, val)

    return root


nums = [5, 3, 8, 1, 4]

root = None

for i in nums:
    root = insert(root, i)


print(root)