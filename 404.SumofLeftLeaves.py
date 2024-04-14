from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.result = 0
        self.get_values(root)
        return self.result

    def get_values(self, node: Optional[TreeNode]) -> tuple:
        
        if node:
            if node.left:
                if node.left.left is None and node.left.right is None:
                    self.result += node.left.val
            self.get_values(node.left)
            self.get_values(node.right)


if __name__ == "__main__":
    node = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    Solution().sumOfLeftLeaves(node)
