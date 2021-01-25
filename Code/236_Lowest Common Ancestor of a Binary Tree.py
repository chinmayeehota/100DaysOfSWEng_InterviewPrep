'''
Approach

'''
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode', ans = False) -> 'TreeNode':
        if not root:
            return None
        if root == p or root == q:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if (left != None and right != None):
            return root
        elif left and not right:
            return left
        elif not left and right:
            return right