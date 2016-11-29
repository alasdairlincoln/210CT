class Node(object):
  def __init__(self, value):
      self.value=value
      self.next=None
      self.prev=None

class List(object):
  def __init__(self):
      self.head=None
      self.tail=None

  def insert(self,n,x):
      #Not actually perfect: how do we prepend to an existing list?
      if n!=None:
          x.next=n.next
          n.next=x
          x.prev=n
          if x.next!=None:
              x.next.prev=x
      if self.head==None:
          self.head=self.tail=x
          x.prev=x.next=None
      elif self.tail==n:
          self.tail=x

  def display(self):
      values=[]
      n=self.head
      while n!=None:
          values.append(str(n.value))
          n=n.next
      print("List:"," "," " .join(values))

  def delete(self, ndelete):
      '''Method to delete a node from the list, '''
      if self.head == None:
          print("The list is empty, please add nodes to the list first")
          return

      n = self.head
      found = False

      while found == False:
          if n.value == ndelete:

              if n.prev == None:
                  l.head = n.next

              else:
                  n.prev.next = n.next

              if n.next == None:
                  l.tail = n.prev

              else:
                  n.next.prev = n.prev
              del(n)
              found = True


          elif n.next == None:
              print("The node you are trying to delete doesnt exist")
              return

          else:
              n = n.next

def inputNumber():
    '''Simple function to get the user to input an integer, it wont accept any other
    data other than an integer and wont let the user continue until they do so.
    Returns the users inputted number'''

    userinput = False
    while userinput == False:
        try:
            number = int(input("Please enter an  integer: "))
            userinput = True
        except ValueError:
            print("Please enter a number (It must be an integer)")
    return number

if __name__ == '__main__':
  l=List()
  #l.insert(None, Node(4))
  #l.insert(l.head,Node(6))
  #l.insert(l.head,Node(8))
  l.display()
  number = inputNumber()
  l.delete(number)
  l.display()
