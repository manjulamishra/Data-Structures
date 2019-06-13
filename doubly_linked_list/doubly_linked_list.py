"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""
  def insert_after(self, value):
    current_next = self.next
    self.next = ListNode(value, self, current_next)
    if current_next:
      current_next.prev = self.next

  """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""
  def insert_before(self, value):
    current_prev = self.prev
    self.prev = ListNode(value, current_prev, self)
    if current_prev:
      current_prev.next = self.prev

  """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""
  def delete(self):
    if self.prev:
      self.prev.next = self.next
    if self.next:
      self.next.prev = self.prev

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node
    self.length = 1 if node is not None else 0

  def __len__(self):
    return self.length

  def add_to_head(self, value):
    self.length +=1
    new_node = ListNode(value = value)
    new_node.next = None
    new_node.prev = None
    if self.head is None:
      self.head = new_node
      self.tail = new_node
    else:
      self.head.prev = new_node
      new_node.next = self.head
      self.head = new_node
    
  def remove_from_head(self):
    if self.head == None:
      return
    else:
      self.length -=1
      if self.head != self.tail:
        self.head = self.head.next
        self.head.prev = None
      else:
        self.head = self.tail=None

  def add_to_tail(self, value):
    self.length +=1
    new_node = ListNode(value=value)
    new_node.next = None
    new_node.prev = None
    if self.tail is None:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next = new_node
      new_node.prev = self.tail
      self.tail = new_node

   
  def remove_from_tail(self):
    if self.head is None:
      return
    if self.head.next is None:
      self.head = None
      return
    n = self.head
    while n.next is not None:
      n = n.next
    n.prev.next = None

    

  def move_to_front(self, node):
    # get to the front node (there won't be a previous node)
    curr_node = self
    while curr_node.prev is not None:
      print("moving to the prev node")
      curr_node = curr_node.prev
    # then add the node to its head
    curr_node.add_to_head(node)
   

  def move_to_end(self, node):
    curr_node = self
    while curr_node.next is not None:
      print("moving to the next node")
      curr_node = curr_node.next
    curr_node.add_to_tail(node)
    

  def delete(self, node):
    if node.next is None and node.prev is None:
      print("deleting the only node left")
      self.head = None
      self.tail = None
      self.length = 0
    elif node.next is None:
      print("deleting the tail node")
      self.tail = node.prev
      self.length -= 1
    elif node.prev is None:
      print("deleting the head node")
      self.head = node.next
      self.length -= 1
    else:
      print("deleting a middle node")
      node.prev.next = node.next
      node.next.prev = node.prev

    
  def get_max(self):
    current = self.head
    if (self.head == None):
      return 0
    else:
      max = current.value
      while (current.next != None):
        current = current.next
        if (current.value>max):
          max = current.value
    return max
