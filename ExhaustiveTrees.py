
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
from itertools import combinations

class TreeNode:
    def __init__(self, id):
        self.id = id
        self.children = []

    def __repr__(self):
        if not self.children:
            return f"({self.id})"
        return f"({self.id} -> {', '.join(map(str, self.children))})"

# todo: I will focus on these:
""" 
1. use a recursive function to generate the trees
2. I will make sure that during generation the number of leaves dont go beyond m
3. I will avoid creating redundant or duplicate trees
"""
def generate_trees(n, m):
    def helper(remaining_nodes, max_leaves):
        if remaining_nodes == 1:
            yield TreeNode(0)
            return

        for split in range(1, remaining_nodes):
            for combo in combinations(range(1, remaining_nodes), split):
                child_sizes = [combo[0]] + [combo[i] - combo[i-1] for i in range(1, len(combo))] + [remaining_nodes - combo[-1]]

                subtrees = []
                for size in child_sizes:
                    subtrees.append(list(helper(size, max_leaves - 1)))

                for subtree_combination in combinations(subtrees, len(subtrees)):
                    root = TreeNode(0)
                    root.children = [st[0] for st in subtree_combination]
                    yield root

    count = 0
    for tree in helper(n, m):
        count += 1
        print(tree)

    print(f"Total number of trees: {count}")


# Example usage:
print("For N = 8, M = 5:")
generate_trees(8, 5)

# For larger cases like N=30, M=3, you can uncomment the following lines:
# print("For N = 30, M = 3:")
# generate_trees(30, 3)



        











