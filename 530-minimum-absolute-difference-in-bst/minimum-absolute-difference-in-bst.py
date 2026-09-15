class Solution:
    def getMinimumDifference(self, root):
        a = []
        def dfs(node):
            if node:
                dfs(node.left)
                a.append(node.val)
                dfs(node.right)
        dfs(root)
        return min(b-a for a,b in zip(a,a[1:]))