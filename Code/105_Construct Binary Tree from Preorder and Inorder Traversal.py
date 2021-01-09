'''
Find the root using preorder.
Then by finding the root in inorder determine the left and right 
subtree and using that recursively build the left and right subtrees of the root.
'''
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
            if not preorder or not inorder:
                return None
            root = TreeNode(preorder[0])
            i = inorder.index(preorder[0])
            root.left = self.buildTree(preorder[1:1+i], inorder[:i])
            root.right = self.buildTree(preorder[1+i:], inorder[i+1:])
            return root