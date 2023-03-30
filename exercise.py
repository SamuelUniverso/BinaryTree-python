from BinaryTree import BinaryTree

tree = BinaryTree()

tree.insertKV(53,'anitta')
tree.insertKV(30,'ana')
tree.insertKV(14,'pedro')
tree.insertKV(39,'maria')
tree.insertKV(9,'bete')
tree.insertKV(23,'joao')
tree.insertKV(34,'carlos')
tree.insertKV(49,'joana')
tree.insertKV(72,'alice')
tree.insertKV(61,'antonio')
tree.insertKV(84,'laura')
tree.insertKV(79,'claudia')

tree.delete(9)
tree.delete(61)
tree.delete(84)
tree.delete(30)

tree.traverse_preorder(tree.root)
