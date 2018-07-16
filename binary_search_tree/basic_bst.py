'''
https://www.youtube.com/watch?v=f5dU3xoE6ms&list=PLEJyjB1oGzx3iTZvOVedkT8nZ2cG105U7&index=5
https://www.youtube.com/watch?v=Zaf8EOVa72I&list=PLEJyjB1oGzx3iTZvOVedkT8nZ2cG105U7&index=6
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.parent = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, current_node):
        if value < current_node.value:
            if current_node.left_child is None:
                current_node.left_child = Node(value)
                current_node.parent = current_node
            else:
                self._insert(value, current_node.left_child)
        elif value > current_node.value:
            if current_node.right_child is Node:
                current_node.right_child = Node(value)
                current_node.parent = current_node
            else:
                self._insert(value, current_node.right_child)
        else:
            print(" Duplicate value")

    # Prints inorder traversal of the tree
    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root)

    def _print_tree(self, current_node):
        if current_node is not None:
            self._print_tree(current_node.left_child)
            print(str(current_node.value))
            self._print_tree(current_node.right_child)

    # Returns the height of the tree
    def height(self):
        if self.root is not None:
            return self._height(self.root, 0)
        else:
            return 0

    def _height(self, current_node, current_height):
        if current_node is None:
            return current_height
        left_height = self._height(current_node.left_child, current_height + 1)
        right_height = self._height(current_node.right_child, current_height + 1)
        return max(left_height, right_height)

    # Returns the actual node
    def find(self, value):
        if self.root is not None:
            return self._find(value, self.root)
        else:
            return None

    def _find(self, value, current_node):
        if current_node.value == value:
            return current_node
        elif current_node.value < value and current_node.right_child:
            return self._find(value, current_node.right_child)
        elif current_node.value > value and current_node.left_child:
            return self._find(value, current_node.left_child)
        return None

    # Returns true false value
    def search(self, value):
        if self.root is not None:
            return self._search(value, self.root)
        else:
            return False

    def _search(self, value, current_node):
        if current_node.value == value:
            return True
        elif current_node.value < value and current_node.right_child:
            return self._search(value, current_node.right_child)
        elif current_node.value > value and current_node.left_child:
            return self._search(value, current_node.left_child)
        return False

    def delete_value(self, value):
        return self.delete_node(self.find(value))

    def delete_node(self, node):

        # Return the node with min value in tree rooted at input node
        def min_value_node(n):
            current = n
            while current.left_child is not None:
                current = current.left_child
            return current

        # Return the total no. of child that value has, 0 if it is at leaf, 1 if it is has only left or right child, 2 if it has both
        def num_children(n):
            total_child = 0
            if n.left_child is not None:
                total_child += 1
            if n.right_child is not None:
                total_child += 1
            return total_child

        # Get the parent of the node to be deleted
        node_parent = node.parent

        # get the no. of child of the node to be deleted
        total_child_node = num_children(node)

        # If there is no child
        if total_child_node == 0:
            # Remove reference to the node from the parent
            if node_parent.left_child == node:
                node_parent.left_child = None
            else:
                node_parent.right_child = None

        # Node has single child
        elif total_child_node == 1:

            # get the child node
            if node.left_child is not None:
                child = node.left_child
            else:
                child = node.right_child

            # replace the node to be deleted with its child node
            if node_parent.left_child == node:
                node_parent.left_child = child
            else:
                node_parent.right_child = child
            child.parent_node = node_parent

        else:
            # Get the inorder successor of delete node
            successor = min_value_node(node.right_child)

            # Copy the inorder successor's value to the node formerly holding the value we wished to delete
            node.value = successor.value

            # Delete the inorder successor since its value is now copied into the other node
            self.delete_node(successor)