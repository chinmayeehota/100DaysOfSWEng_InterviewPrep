class Solution:
    def rightSideView(self, root: TreeNode, res=[]) -> List[int]:
        if not root:
            print("no")
            return
        res.append(root.val)
        self.rightSideView(root.right, res)
        print(res)
        #res.append(root.right.val)
        return res