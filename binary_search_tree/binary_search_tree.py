class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if self.value:
      if value < self.value:
        if self.left is None:
          self.left = BinarySearchTree(value)
        else:
          self.left.insert(value)
      elif value > self.value:
        if self.right is None:
          self.right = BinarySearchTree(value)
        else:
          self.right.insert(value)
    else:
      self.value = value

  def contains(self, target):
    if target < self.value:
      if self.left is None:
        return None, None
      return self.left.contains(target, self)
    elif target > self.value:
      if self.right is None:
        return None, None
      return self.right.contains(target, self)
    
    

  def get_max(self):
    if self.value == None:
      return "Not found"
    res = self.value
    lres = self.left
    rres = self.right
    if lres > res:
      res = lres
    if rres > res:
      res = rres
    return res


  def for_each(self, cb):
    pass