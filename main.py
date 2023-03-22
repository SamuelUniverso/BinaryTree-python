from Node import Node

root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
print(root.findval(7))
print(root.findval(14))
print(root.inorderTraversal(root))
root.print_1d()
root.print_2d(root);