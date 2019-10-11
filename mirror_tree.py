class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def mirror_tree(node: Node):
    if node:
        mirror_tree(node.left)
        mirror_tree(node.right)
        node.left, node.right = node.right, node.left


def height(node: Node):
    if not node:
        return 0
    return 1 + max(height(node.left), height(node.right))


def print_level(node, lev):
    if node:
        if lev == 1:
            print(node.data, end=' ')
        else:
            print_level(node.left, lev - 1)
            print_level(node.right, lev - 1)


def level_order_traversal(node):
    h = height(node)
    for i in range(1, h + 1):
        print_level(node, i)
        print()


if __name__ == '__main__':
    root = Node('a')
    root.left = Node('b')
    root.right = Node('c')
    root.left.left = Node('d')
    root.left.right = Node('e')
    root.right.left = Node('f')
    root.right.right = Node('g')

    level_order_traversal(root)
    mirror_tree(root)
    level_order_traversal(root)
