#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def dft(node, current_path, result):
    
    if node is None:
        return
    
    current_path.append(f'{node.value}')
    if is_leaf(node):
        result.append('->'.join(current_path[:]))
        
    dft(node.left, current_path, result)
    dft(node.right, current_path, result)
    current_path.pop()
    
    
def is_leaf(node):
    return node.left is None and node.right is None
    
def treePaths(root):
    result = []
    dft(root, [], result)
    return result