class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, root, key):
        if not root:
            return TreeNode(key)
        if key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        return root

    def inorder_traversal(self, root):
        if root:
            self.inorder_traversal(root.left)
            print(root.val, end=" ")
            self.inorder_traversal(root.right)

    def preorder_traversal(self, root):
        if root:
            print(root.val, end=" ")
            self.preorder_traversal(root.left)
            self.preorder_traversal(root.right)

    def postorder_traversal(self, root):
        if root:
            self.postorder_traversal(root.left)
            self.postorder_traversal(root.right)
            print(root.val, end=" ")

    def level_order_traversal(self, root):
        if not root:
            return
        queue = [root]
        while queue:
            node = queue.pop(0)
            print(node.val, end=" ")
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

# Example usage
binary_tree = BinaryTree()
keys = [10, 5, 15, 3, 7, 12, 20]
for key in keys:
    binary_tree.root = binary_tree.insert(binary_tree.root, key)

print("Inorder Traversal:")
binary_tree.inorder_traversal(binary_tree.root)

print("\nPreorder Traversal:")
binary_tree.preorder_traversal(binary_tree.root)

print("\nPostorder Traversal:")
binary_tree.postorder_traversal(binary_tree.root)

print("\nLevel Order Traversal:")
binary_tree.level_order_traversal(binary_tree.root)
