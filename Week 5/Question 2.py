class Node(object):
  def __init__(self, value):
      self.value=value
      self.next=None
      self.prev=None

class List(object):
  def __init__(self):
      '''When the list class is first called the head and tail are set to None'''
      self.head=None
      self.tail=None

  def insert(self,n,x):

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
      '''Method to delete a node from the list, makes sure the list isnt empty and alerts
      the user if it is, also alerts the user if the node they are trying to delete doesnt exist'''
      if self.head == None:
          print("The list is empty, please add nodes to the list first")
          return

      n = self.head
      found = False

      while found == False:
          if n.value == ndelete:#checks to see if the current node is the one that is to be deleted

              if n.prev == None: #checks to see if the node to be deleted is the head
                  l.head = n.next #asigns the new head

              else:
                  n.prev.next = n.next#if it isnt the head then it points to the next node

              if n.next == None:#checks to see if the node is the tail
                  l.tail = n.prev#asigns the new tail

              else:
                  n.next.prev = n.prev#if it isnt the tail then it points to the previous node

              del(n)#the node is then deleted
              found = True


          elif n.next == None:#the current node is at the end of the list and the node to be deleted hasnt been found hence it doesnt exist
              print("The node you are trying to delete doesnt exist")
              return

          else:
              n = n.next #moves onto the next node

def inputNumber():
    '''Simple function to get the user to input an integer, it wont accept any other
    data other than an integer and wont let the user continue until they do so.
    Returns the users inputted number'''

    userinput = False
    while userinput == False:
        try:
            number = int(input("Please enter a node to delete: "))
            userinput = True
        except ValueError:
            print("Please enter a node to be deleted (It must be an integer)")
    return number

if __name__ == '__main__':
  l=List()
  l.insert(None, Node(4))
  l.insert(l.head,Node(6))
  l.insert(l.head,Node(8))
  l.display()
  number = inputNumber()
  l.delete(number)
  l.display()
