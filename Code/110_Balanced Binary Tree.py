class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        leftDepth = self.depth(root.left)
        rightDepth = self.depth(root.right)
        if abs(leftDepth - rightDepth) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
    
    def depth(self, root, height = 1):
        if not root:
            return 0
        height += max(self.depth(root.right, height), self.depth(root.left, height))
        return height