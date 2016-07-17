class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        if self.IsAncestor(root.left, p) and self.IsAncestor(root.left, q):
            return self.lowestCommonAncestor(root.left, p, q)
        elif self.IsAncestor(root.right, p) and self.IsAncestor(root.right, q):
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root

    def IsAncestor(self, root, node):
        if root == None:
            return False
        else:
            return root == node or self.IsAncestor(root.left, node) or self.IsAncestor(root.right, node)