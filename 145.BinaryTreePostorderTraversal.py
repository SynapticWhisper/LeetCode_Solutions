from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def get_postorder(node: Optional[TreeNode]) -> None:
            nonlocal result
            if node is None:
                return
            get_postorder(node.left)
            get_postorder(node.right)
            result.append(node.val)
            return
        
        get_postorder(root)
        return result
