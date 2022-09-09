class Treenode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def createnode(self, data):
        """this function creates a node and returns the node"""
        root = Treenode(data)
        return root

    def insert(self, root, data):
        """
        we cannot simply just insert a node in the Tree
        we should take care of the properties while inserting nodes in a tree i.e.,
        (a) a node can have atmost 2 children
        (b) the left child of a node should be less than the parent node
        and the right child should be greater than the parent node
            Example: [4,2,5,1,3]
            in the above example,
            4 is the root node, 2 is the left child of 4 and 5 is the right child of 4
        """

        # if the root is None, then we create a node and assign it to the root
        # after it's created, we return the root
        if root is None:
            root = self.createnode(data)
            return root

        # if the current node (current data) is less than the root node,
        # then we insert the node in the left subtree (i.e left child of the root)
        elif data < root.data:
            root.left = self.insert(root.left, data)

        # if the current node is greater than the root node,
        # then we insert the node in the right subtree (i.e right child of the root)
        elif data > root.data:
            root.right = self.insert(root.right, data)

        # head node/root node will be returned which will specify the root of the tree
        return root


obj = Tree()
root = None
nodesList = [0, 4, 2, 5, 7]
for i in nodesList:
    root = obj.insert(root, i)
print(root.data)
