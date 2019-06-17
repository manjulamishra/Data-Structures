class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if value == self.value:
      return "Value found"
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
    if target == self.value:
      return "Value found"
    if target < self.value:
      if self.left is None:
        return False
      return self.left.contains(target)
    elif target > self.value:
      if self.right is None:
        return False
      return self.right.contains(target)
    
    

  def get_max(self):
    if self.left is None and self.right is None:
      return self.value
    elif self.left is None:
      rvalue = self.right.get_max()
      if self.value > rvalue:
        return self.value
      else:
        return rvalue
    elif self.right is None:
      lvalue = self.left.get_max()
      if self.value > lvalue:
        return self.value
      else:
        return lvalue
    else:
      lres = self.left.get_max()
      rres = self.right.get_max()
      res = self.value
      if (lres > res):
        res = lres
      if (rres > res):
        res = rres
      return res

  def for_each(self, cb):
    print (self.value)
    cb(self.value)
    if self.left:
      self.left.for_each(cb)
    if self.right:
      self.right.for_each(cb)