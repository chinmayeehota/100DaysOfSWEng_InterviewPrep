'''
Problem can be broken into 2 parts
1). Finding deepest nodes
2). Finding LCA of deepest nodes
'''
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode', ans = False) -> 'TreeNode':