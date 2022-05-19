# https://www.codecademy.com/code-challenges/code-challenge-balanced-binary-search-tree-python

class TreeNode():

  def __init__(self, value):
    self.right = None
    self.left = None
    self.value = value
  
  def __str__(self):
    return f"{self.value}->{self.left}\n{self.value}->{self.right}"


class SubNodeLeft(TreeNode):

  def __init__(self, value):
    self.value = self.left

  def __str__(self):
    return f"{self.value}->{self.left}\n{self.value}->{self.right}"


class SubNodeRight(TreeNode):

  def __init__(self, value):
    self.value = self.right
    
  def __str__(self):
    return f"{self.value}->{self.left}\n{self.value}->{self.right}"

def balanced_bst(a):
  
  core_value = a[0]
  core_node = TreeNode(core_value)

  return a
  # Write your code here


a = [1,2,3,4,5,6,7,8]
balanced_node = balanced_bst(a)
print(balanced_node)
