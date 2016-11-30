class BinTreeNode(object):

    def __init__(self, value):
        '''When the class is called the value that is passed into it is
        saved as an instance of the class, left and right are also set to none'''
        self.value=value
        self.left=None
        self.right=None

def tree_insert( tree, item):
    if tree==None:
        tree=BinTreeNode(item)
    else:
        if(item < tree.value):
            if(tree.left==None):
                tree.left=BinTreeNode(item)
            else:
                tree_insert(tree.left,item)
        else:
            if(tree.right==None):
                tree.right=BinTreeNode(item)
            else:
                tree_insert(tree.right,item)
    return tree

def postorder(tree):
    if(tree.left!=None):
        postorder(tree.left)
    if(tree.right!=None):
        postorder(tree.right)
    else:
        print(tree.value)


def in_order(tree):
    '''Method to print the tree in order'''
    top = tree #asigns the paramater to a variable called top
    List = []#creates an empty list
    treeprinted = False
    while treeprinted == False:
        if top != None: #makes sure the tree hasnt been traversed
            List.append(top)
            top = top.left #traverses down the left branch of the tree

        else:
            if len(List) > 0:
                top = List.pop()
                print(top.value)
                top = top.right #traverses down the right branch of the tree

            else:
                treeprinted = True

if __name__ == '__main__':

  t=tree_insert(None,6);
  tree_insert(t,10)
  tree_insert(t,5)
  tree_insert(t,2)
  tree_insert(t,3)
  tree_insert(t,4)
  tree_insert(t,11)
  in_order(t)
