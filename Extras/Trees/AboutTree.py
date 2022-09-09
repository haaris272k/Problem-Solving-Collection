"""
Types Of Tree
1) Binary Tree - Every node can have at most 2 children (left and right)
2) Binary Search Tree - has max 2 children where left child is less than parent and right child is greater than parent
   Ex- 5,2,9 here 5 is parent, 2 is left child and 9 is right child
3) AVL Tree
4) Red Black Tree
5) Splay Tree
6) B Tree
7) B+ Tree
Out of these, Binary Tree, Binary Search Tree are most commonly used. (important)
"""

"""
Main operations in tree are as follows:

1. Create a tree
2. Insert a node
3. Search a node (BFS, DFS)
4. Delete a node
5. Print/Display
6. Find height of tree
7. Traverse a tree (Inorder, Preorder, Postorder)
                
"""

"""Implementation of tree in Python"""
# initialize a class
# Take 3 variables in the class one will be the root node and
# the other two will be the left and right nodes
# val/data will be the value of the node
# to connect with the root
# (a) first assign some value to the root node
# (b) then connect like this: root.left = classname(some value)
# (c) then connect like this: root.right = classname(some value)
# we can keep on connecting like this: root.left.left = classname(some value) means
# connect the left node of the left node of the root node
# to access the value of the node
# (a) first assign some value to the root node
# (b) then access like this: root.val (Roots value)
# (c) then access like this: root.left.val (value of left node of the root node)

# ---------------------------Implementation---------------------------:

"""
class TreeNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.val = data


root = TreeNode(4) # root node
root.left = TreeNode(2) # left node of the root node
root.right = TreeNode(3) # right node of the root node
print(root.val)# 4  
print(root.left.val)# 2
print(root.right.val)

"""

# --------------------------------------------------------------------:
