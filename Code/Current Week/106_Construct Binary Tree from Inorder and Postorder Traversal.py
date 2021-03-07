# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
Approach:
- hashmap mapping value in order list to its index
- last ele in postorder is root
- find the index of root in order list
- all elements to left of root is left subtree, use it to build left subtree
- all elements to right of root is right subtree, us it to build right subtree
'''
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        self.postorder = postorder
        self.inorder_idx = {val:idx for idx,val in enumerate(inorder)}
        return self.helper(0, len(inorder) - 1)
    
    def helper(self, left_idx, right_idx):
        if left_idx > right_idx:
            return None
        val = self.postorder.pop()
        root = TreeNode(val)
        
        index = self.inorder_idx[val]
        
        root.right = self.helper(index+1, right_idx)
        root.left = self.helper(left_idx, index-1)
        return root