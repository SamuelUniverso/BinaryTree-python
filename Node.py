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

        def print_1d(self):
                if self.left:
                        self.left.printTree()
                print(self.data)
                if self.right:
                        self.right.printTree()

        def print_2d(self, root):
            if not root:
                return []

            height = self.get_height(root)
            width = 2 ** height - 1

            # Initialize the result array
            res = [[' ' for _ in range(width)] for _ in range(height)]

            # Fill the result array
            self.fill_res(root, res, 0, 0, width - 1)

            # Print the result
            for row in res:
                print(''.join(row))

        def fill_res(self, root, res, depth, left, right):
            if not root:
                return

            mid = (left + right) // 2
            res[depth][mid] = str(root.data)
            self.fill_res(root.left, res, depth + 1, left, mid - 1)
            self.fill_res(root.right, res, depth + 1, mid + 1, right)

        def get_height(self, root):
            if not root:
                return 0

            left_height = self.get_height(root.left)
            right_height = self.get_height(root.right)
            return max(left_height, right_height) + 1
