# Problem Set 4a
# Name:
# Collaborators:
# Time spent:

from tree import Node  # Imports the Node object used to construct trees

# Part A0: Data representation
# Fill out the following variables correctly.
# If correct, the tests named data_representation should pass.
tree_1 = Node(9, Node(6), Node(3, Node(7), Node(8)))
tree_2 = Node(7, Node(13, Node(15, Node(4), Node(6)), Node(5)), Node(2, Node(9), Node(11)))
tree_3 = Node(4, Node(9, Node(14), Node(25)), Node(17, Node(1), Node(8, Node(11), Node(6))))

def find_tree_height(tree):
    '''
    Find the height of the given tree
    Input:
        tree: An element of type Node constructing a tree
    Output:
        The integer depth of the tree
    '''
    # If there's no tree, we can think of the height as being -1
    if tree is None:
        return -1

    # Begin height count
    height = 0

    # Use recursion to find the height of the tree
    h_left = find_tree_height(tree.get_left_child())
    h_right = find_tree_height(tree.get_right_child())
    return max(h_left, h_right) + 1

def is_heap(tree, compare_func):
    '''
    Determines if the tree is a max or min heap depending on compare_func
    Inputs:
        tree: An element of type Node constructing a tree compare_func:
              a function that compares the child node value to the parent node value

            i.e. compare_func(child_value,parent_value) for a max heap would return False
                 if child_value > parent_value and True otherwise

                 compare_func(child_value,parent_value) for a min meap would return False
                 if child_value < parent_value and True otherwise
    Output:
        True if the entire tree satisfies the compare_func function; False otherwise
    '''
    # A tree wich is a single node satisfies the conditions to be a heap (both max and min)
    if tree is None or (tree.get_left_child() is None and tree.get_right_child() is None):
        return True

    left_child = tree.get_left_child()
    right_child = tree.get_right_child()

    # Check if the node's left and right subtrees are heaps
    left_heap = is_heap(left_child, compare_func) if left_child else True
    right_heap = is_heap(right_child, compare_func) if right_child else True

    # Check if node is the max or min element of its subtree using the compare_func
    if left_child and not compare_func(left_child.get_value(), tree.get_value()):
        return False
    if right_child and not compare_func(right_child.get_value(), tree.get_value()):
        return False

    return left_heap and right_heap

if __name__ == '__main__':
    # # You can use this part for your own testing and debugging purposes.
    # # IMPORTANT: Do not erase the pass statement below if you do not add your own code
    pass
