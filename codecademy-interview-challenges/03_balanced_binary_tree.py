# https://www.codecademy.com/code-challenges/code-challenge-balanced-binary-search-tree-python

class TreeNode():

  def __init__(self, value):
    self.right = None
    self.left = None
    self.value = value
  
  def __str__(self):
    return f"{self.value}->{self.left}\n{self.value}->{self.right}"

class SubNode(TreeNode):
  def __init__(self, value):
    self.right = None
    self.left = None
    self.value = value

    def put_into_position(self, position):
      if position == 'right':
        self.right = self.value
        
def balanced_bst(a):
  return a
  # Write your code here


a = [1,2,3,4,5,6,7,8]
balanced_node = balanced_bst(a)
print(balanced_node)
