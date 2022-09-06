""" Implement Inorder, Preorder and Postorder Traversals of a Binary Tree """

# Tree Traversal Algorithms


class TreeNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.val = data

    # Inorder traversal
    # In this (left-->root-->right)
    # Algorithm - recursively traverse the left -> print root-> recursively traverse the right
    # TC: O(n) SC: O(n) where n is the number of nodes in the tree
    def inorder(root):
        if root:
            TreeNode.inorder(root.left)  # (class.method(root.left))
            print(root.val)  # (root.val)
            TreeNode.inorder(root.right)  # (class.method(root.right))
        else:
            return []

    # Preorder traversal
    # In this (root-->left-->right)
    # Algorithm - recursively traverse the root -> recursively traverse the left -> recursively traverse the right
    # TC: O(n) SC: O(n) where n is the number of nodes in the tree
    def preorder(root):
        if root:
            print(root.val)
            TreeNode.preorder(root.left)
            TreeNode.preorder(root.right)
        else:
            return []

    # Postorder traversal
    # In this (left-->right-->root)
    # Algorithm - recursively traverse the left -> recursively traverse the right -> print root
    # TC: O(n) SC: O(n) where n is the number of nodes in the tree
    def postorder(root):
        if root:
            TreeNode.postorder(root.left)
            TreeNode.postorder(root.right)
            print(root.val)
        else:
            return []


root = TreeNode(1)
root.left = TreeNode(3)
root.left.left = TreeNode(5)
root.right = TreeNode(4)
root.right.left = TreeNode(2)
root.left.right = TreeNode(6)
root.right.right = TreeNode(7)
print("Inorder traversal: ")
TreeNode.inorder(root)
print("\n")
print("Preorder traversal: ")
TreeNode.preorder(root)
print("\n")
print("Postorder traversal: ")
TreeNode.postorder(root)
