"""
You are given the values from a preorder and an inorder tree traversal. Write a
function that can take those inputs and outputs a binary tree that follows the given ordering.

*Note: assume that there will not be any duplicates in the tree.*

Example:
Inputs:
preorder = [5,7,22,13,9]
inorder = [7,5,13,22,9]

Output:
    5
   / \
  7  22
    /  \
   13   9
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(preorder: List[int], inorder: List[int]) -> TreeNode:
  # Your code here
  # given preorder and inorder outputs, re-construct the tree that these traversal outputs came from
  # 
  '''
  Input: two lists where the preorder list represents the output from running a preorder traversal over a tree and the inorder list represents the output from running an inorder traversal tree

  '''

  # base case(s)
  # we want to get through these arrays
  # when we iterate through the entire inorder list
  # we've considered every element and we've built the entire tree

  # how do we move closer to a base case?
  # 1. take the first element in the preorder list
  # 2. locate that element in the order list
  # 3. figure out the size of teh two subtrees