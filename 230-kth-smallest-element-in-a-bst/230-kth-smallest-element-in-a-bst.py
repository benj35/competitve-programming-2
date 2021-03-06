# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        heap = []
        
        def dfs(node):
            if not node: return
            if len(heap) < k:
                heapq.heappush(heap, -node.val)
            else:
                heapq.heappushpop(heap, -node.val)
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return -heap[0]

        