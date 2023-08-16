class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinarySearchTree:
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

    def search(self, root, key):
        if not root or root.val == key:
            return root
        if key < root.val:
            return self.search(root.left, key)
        return self.search(root.right, key)

    def find_min(self, root):
        while root.left:
            root = root.left
        return root

    def delete(self, root, key):
        if not root:
            return root
        if key < root.val:
            root.left = self.delete(root.left, key)
        elif key > root.val:
            root.right = self.delete(root.right, key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            temp = self.find_min(root.right)
            root.val = temp.val
            root.right = self.delete(root.right, temp.val)
        return root

    def inorder_traversal(self, root):
        if root:
            self.inorder_traversal(root.left)
            print(root.val, end=" ")
            self.inorder_traversal(root.right)

# Example usage
bst = BinarySearchTree()
keys = [10, 5, 15, 3, 7, 12, 20]
for key in keys:
    bst.root = bst.insert(bst.root, key)

print("Inorder Traversal:")
bst.inorder_traversal(bst.root)

search_key = 12
search_result = bst.search(bst.root, search_key)
if search_result:
    print(f"\nFound {search_key} in the BST")
else:
    print(f"\n{search_key} not found in the BST")

delete_key = 15
bst.root = bst.delete(bst.root, delete_key)
print("\nBST after deleting", delete_key)
bst.inorder_traversal(bst.root)


#####################################
