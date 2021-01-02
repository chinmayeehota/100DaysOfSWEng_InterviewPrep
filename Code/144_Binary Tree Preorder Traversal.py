'''
Link To Ques
https://leetcode.com/problems/binary-tree-preorder-traversal/
'''

#Recursive

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def preorderTraversal(self, root: TreeNode):
        res = []
        self.preorderTraversal_Helper(root, res)
        return res
    
    def preorderTraversal_Helper(self, root, res):
        if root:
            res.append(root.val)
            if root.left:
                self.preorderTraversal_Helper(root.left, res)
            if root.right:
                self.preorderTraversal_Helper(root.right, res)