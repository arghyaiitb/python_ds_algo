'''
https://www.youtube.com/watch?v=azupT01iC78&index=7&list=PLEJyjB1oGzx3iTZvOVedkT8nZ2cG105U7

'''

import sys


class Node:
    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None



def validate_bst(root, min_val=-sys.maxsize, max_val=sys.maxsize):
    if root is None:
        return True
    if root.value > min_val and root.value < max_val and\
            validate_bst(root.left_child, min_val, root.value) and\
            validate_bst(root.right_child, root.value, max_val):
        return True
    else:
        return False

