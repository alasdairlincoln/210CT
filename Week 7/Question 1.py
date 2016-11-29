class List(object):
    def __init__(self):
        self.array = []

    def insert(self, n):
        self.array.append(n)

    def display(self):
        print(self.array)


l = List()
l.insert(5)
l.display()
