from typing import Optional

class Solution:
    def treeToDoublyList(self, root):
        if not root:
            return None

        self.first = None
        self.last = None
        
        self.inorder_link(root)
        
        self.first.left = self.last
        self.last.right = self.first
        
        return self.first

    def inorder_link(self, node):
        if node:
           self.inorder_link(node.left)
           
        #    if we have not seen an element then the first is first
           if not self.last:
               self.first = node
            # this is a smaller node   
           else:
               node.left = self.last
               self.last.right = node
               
           self.last = node
           
           self.inorder_link(node.right)
           
            
                 