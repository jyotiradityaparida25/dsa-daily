# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        self.postorder_idx = len(postorder) - 1

        def build(left: int, right: int) -> TreeNode:
            if left > right:
                return None
            
            root_val = postorder[self.postorder_idx]
            root = TreeNode(root_val)
            self.postorder_idx -= 1
            
            mid = inorder_map[root_val]
            
            root.right = build(mid + 1, right)
            root.left = build(left, mid - 1)
            
            return root

        return build(0, len(inorder) - 1)
        