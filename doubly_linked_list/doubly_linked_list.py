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
    if self.head is None:
      # allocate the Node and put in teh data
      new_node = ListNode(value = value)

      new_node.next = self.head
      new_node.prev = None
      if self.head is not None:
        self.head.prev = new_node
      self.head = new_node

    
  def remove_from_head(self):
    if self.head == None:
      return
    else:
      if self.head != self.tail:
        self.head = self.head.next
        self.head.prev = None
      else:
        self.head = self.tail=None

  def add_to_tail(self, value):
    new_node = ListNode(value=value)
    new_node.next = None
    if self.head is None:
      new_node.prev = None
      self.head = new_node
      return
    last = self.head
    while (last.next is not None):
      last = last.next
      last.next = new_node
      new_node.prev = last
      return

   
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
    pass

  def move_to_end(self, node):
    pass

  def delete(self, node):
    pass
    
  def get_max(self):
    pass
