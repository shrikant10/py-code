# A binary tree node
class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    # To print the value of the node
    def __str__(self):
        return self.data


# Insert new element in binary search tree
def insert(node, new):
    if node.data:
        if new < node.data:
            if node.left is None:
                node.left = Node(new)
            else:
                node.left.insert(new)
        else:
            if node.right is None:
                node.right = Node(new)
            else:
                node.right.insert(new)
    else:
        node.data = new


# Print in-order traversal of tree
def in_order(node):
    if node:
        in_order(node.left)
        print(node.data, end=' ')
        in_order(node.right)


# Print pre-order traversal of tree
def pre_order(node):
    if node:
        print(node.data, end=' ')
        pre_order(node.left)
        pre_order(node.right)


# Print post-order traversal of tree
def post_order(node):
    if node:
        post_order(node.left)
        post_order(node.right)
        print(node.data, end=' ')


# Function to return height of binary tree
def height(node):
    if node is None:
        return 0
    return max(height(node.left), height(node.right)) + 1


def level_order_traversal(node):
    ht = height(node)
    for i in range(1, ht + 1):
        print("Level {}".format(i))
        print_given_level(node, i)


def print_given_level(node, level):
    if not node:
        return
    if level == 1:
        print(node.data)
    elif level > 1:
        print_given_level(node.left, level - 1)
        print_given_level(node.right, level - 1)


if __name__ == '__main__':
    root = Node(1)

    root.left = Node(2)
    root.right = Node(3)

    root.left.left = Node(4)
    root.left.right = Node(5)

    root.right.right = Node(6)

    print('Height: ', height(root))
    print('\n In-order: ')
    in_order(root)
    print('\n Pre-order: ')
    pre_order(root)
    print('\n Post-order: ')
    post_order(root)
    print('\n Level-order: ')
    level_order_traversal(root)


