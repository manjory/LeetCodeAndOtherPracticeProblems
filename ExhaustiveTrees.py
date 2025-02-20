class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
"""
In this question we will be writing an exhaustive generator to
generate trees. Trees are allowed to have any number of children
nodes. (I.e. we are not restricting ourselves to binary trees.)
Please write a program to generate all possible trees with N nodes
that have less than or equal to M leaf nodes.
Do not redundantly generate topologically equivalent trees. A tree is
topologically equivalent to another tree if we can reorder its
children (or the children of its children, etc ...) to arrive at the
second tree. I.e. trees are not distinguished by the order of its
children.
Efficiency Goal: Please print out the trees as they are generated, and
try to minimize the time required to generate each successive tree.
Show us the generated trees, and count the total number of trees for:
  1) N = 8, M = 5. 
  2) N = 30, M = 3. 
"""
class ExhaustiveBinaryTreeList:
    def generateBinaryTreeList(self,n,m):









