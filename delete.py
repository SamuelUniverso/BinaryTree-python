from BinaryTree import BinaryTree

tree = BinaryTree()

tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(1)
tree.insert(4)
tree.insert(6)
tree.insert(8)

tree.print_tree()
print("##############")
tree.delete(8)
tree.print_tree()
print("##############")