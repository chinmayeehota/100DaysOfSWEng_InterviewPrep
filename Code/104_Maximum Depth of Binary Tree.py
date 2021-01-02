class Solution:
    def maxDepth(self, root: TreeNode, depth = 1) -> int:
        if not root:
            return 0
        depth += max(self.maxDepth(root.left, depth), self.maxDepth(root.right, depth))
        return depth