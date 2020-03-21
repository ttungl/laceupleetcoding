# 1382. Balance a Binary Search Tree

# Given a binary search tree, return a balanced binary search tree with the same node values.

# A binary search tree is balanced if and only if the depth of the two subtrees of every node never differ by more than 1.

# If there is more than one answer, return any of them.

# ```
# 1
#  \
#   2 
#    \
#     3
#      \
#       4
# ```

# ```
#       2
#      / \
#     1   3
#     	 \
#     	  4
# ```
# or
# ```
#        3
#       / \
#      1   4
#       \
#        2
# ```

# Input: root = [1,null,2,null,3,null,4,null,null]
# Output: [2,1,3,null,null,null,4]
# Explanation: This is not the only correct answer, [3,1,4,null,2,null,null] is also correct.

# Constraints:

# The number of nodes in the tree is between 1 and 10^4.
# The tree nodes will have distinct values between 1 and 10^5.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution: # sol 1 DFS
    def __init__(self):
        self.res = []
        
    def _sortedBST(self, start : int, end : int):
        if start > end: return None
        mid = (start + end)//2
        root = self.res[mid]
        root.left = self._sortedBST(start, mid-1)
        root.right = self._sortedBST(mid+1, end)
        return root
    
    def _inorder_dfs(self, root : TreeNode):
        if root.left:
            self._inorder_dfs(root.left)
        self.res.append(root)
        if root.right:
            self._inorder_dfs(root.right)
        
    
    def balanceBST(self, root: TreeNode) -> TreeNode:
        self._inorder_dfs(root)
        return self._sortedBST(0, len(self.res)-1)
                
        
 class Solution: # sol 2 BFS
    def __init__(self):
        self.res = []
    
    def _inorder_BFS(self, root : TreeNode):
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            self.res.append(root)
            root = root.right
    
    def _buildBalanceBST(self, root: List[TreeNode]) -> TreeNode:
        if not root: 
            return None
        mid = len(root)//2
        node = root[mid]
        node.left = self._buildBalanceBST(root[:mid])
        node.right = self._buildBalanceBST(root[mid+1:])
        return node
    
    def balanceBST(self, root : TreeNode) -> TreeNode:
        self._inorder_BFS(root)
        return self._buildBalanceBST(self.res)       
        





