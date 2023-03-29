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
                return current
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
