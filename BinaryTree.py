class BinaryTree:
    class Node:

        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert(self, value):
        node = self.Node(value)
        if self.root is None:
            self.root = node
        else:
            current = self.root
            while True:
                if value < current.value:
                    if current.left is None:
                        current.left = node
                        break
                    else:
                        current = current.left
                else:
                    if current.right is None:
                        current.right = node
                        break
                    else:
                        current = current.right

    def search(self, value):
        current = self.root
        while current is not None:
            if value == current.value:
                return current.value
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return None

    def traverse_inorder(self, node):
        if node is not None:
            self.traverse_inorder(node.left)
            print(node.value)
            self.traverse_inorder(node.right)

    def traverse_preorder(self, node):
        if node is not None:
            print(node.value)
            self.traverse_preorder(node.left)
            self.traverse_preorder(node.right)

    def traverse_postorder(self, node):
        if node is not None:
            self.traverse_postorder(node.left)
            self.traverse_postorder(node.right)
            print(node.value)

    def print_tree(self):
        self._print_tree_recursive(self.root, 0)

    def _print_tree_recursive(self, node, level):
        if node is not None:
            self._print_tree_recursive(node.right, level + 1)
            print('    ' * level + str(node.value))
            self._print_tree_recursive(node.left, level + 1)

    def delete(self, value):
        parent = None
        current = self.root

        # Find the node to delete and its parent
        while current is not None:
            if value == current.value:
                break
            elif value < current.value:
                parent = current
                current = current.left
            else:
                parent = current
                current = current.right

        # If the node was not found, return
        if current is None:
            return

        # If the node has no children, simply delete it
        if current.left is None and current.right is None:
            if parent is None:
                self.root = None
            elif parent.left == current:
                parent.left = None
            else:
                parent.right = None

        # If the node has one child, replace it with the child
        elif current.left is None or current.right is None:
            child = current.left or current.right
            if parent is None:
                self.root = child
            elif parent.left == current:
                parent.left = child
            else:
                parent.right = child

        # If the node has two children, replace it with its inorder successor
        else:
            successor_parent = current
            successor = current.right
            while successor.left is not None:
                successor_parent = successor
                successor = successor.left
            current.value = successor.value
            if successor_parent.left == successor:
                successor_parent.left = successor.right
            else:
                successor_parent.right = successor.right

    def _height(self, node):
        if node is None:
            return -1
        else:
            left_height = self._height(node.left)
            right_height = self._height(node.right)
            return 1 + max(left_height, right_height)

    def tree_height(self):
        return self._height(self.root)
