class Node:
        def __init__(self, data):
                self.left = None
                self.right = None
                self.data = data

        def insert(self, data):
                if data < self.data:
                        if self.left is None:
                                self.left = Node(data)
                        else:
                                self.left.insert(data)
                elif data > self.data:
                        if self.right is None:
                                self.right = Node(data)
                        else:
                                self.right.insert(data)
                else:
                        self.data = data

        def findval(self, lkpval):
                if lkpval < self.data:
                        if self.left is None:
                                return str(lkpval) + " Not Found"
                        return self.left.findval(lkpval)
                elif lkpval > self.data:
                        if self.right is None:
                                return str(lkpval) + " Not Found"
                        return self.right.findval(lkpval)
                else:
                        print(str(self.data) + ' is found')

        def inorderTraversal(self, root):
                res = []
                if root:
                        res = self.inorderTraversal(root.left)
                        res.append(root.data)
                        res = res + self.inorderTraversal(root.right)
                return res

        def printTree(self):
                if self.left:
                        self.left.printTree()
                print(self.data)
                if self.right:
                        self.right.printTree()
