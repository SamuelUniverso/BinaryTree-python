from BinaryTree import BinaryTree

tree = BinaryTree()

tree.insertKV(50, 'samuel')
tree.insertKV(55, 'lucas')
tree.insertKV(60, 'mateus')

print(tree.search('samuel').key)
print(tree.search('samuel').value)
