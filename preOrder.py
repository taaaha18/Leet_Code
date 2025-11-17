class treeNode:
    def _init(self, val):
        self.value=val
        self.left=None
        self.right=None

def preOrderTraversal(root):

    results=[]
    def dfs(node):
      if node is None:
         return[]
      results.append(node.value)
      dfs(node.left)
      dfs(node.right)

    dfs(root)
    return results

