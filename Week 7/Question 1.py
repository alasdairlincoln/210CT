class Graph(object):
    '''Class for the graph'''
    def __init__(self):
        self.verticies = [] #creates an empty list for all the vertices to be stored in

    def insert(self, n):
        '''takes a vertex and appends the value of the vertex to the list verticies'''
        self.verticies.append(n.value)

    def createEdge(self, V1, V2):
        if V2.value not in V1.connectedTo:
            V1.connectedTo.append(V2.value)
            V2.connectedTo.append(V1.value)
        else:
            print("There is already an edge there")

    def displayNodes(self):
        print("The current nodes in the graph are", self.verticies)

    def displayConnected(self, V1):
        V1.connected()



class Vertex(object):
    def __init__(self, value):
        self.value = value
        self.connectedTo = []

    def connected(self):
        self.connectedTo.sort()
        print(self.value, "is connected to",self.connectedTo)


g = Graph()# Creates an instance of class graph called 'g'
vertice = {} #Creates a dictionary to store all verice variable names and values
for i in range(1,11):#a for loop to populate the dictionary with class instances
    vertice[i] = Vertex(i)

for i in range(1,11):#for loop to insert the nodes into the graph
    g.insert(vertice[i])

#creates an edge on the graph between the 2 specified verticies
g.createEdge(vertice[1],vertice[2])
g.createEdge(vertice[1],vertice[6])
g.createEdge(vertice[1],vertice[7])
g.createEdge(vertice[2],vertice[7])
g.createEdge(vertice[2],vertice[4])
g.createEdge(vertice[2],vertice[3])
g.createEdge(vertice[3],vertice[5])
g.createEdge(vertice[3],vertice[8])
g.createEdge(vertice[3],vertice[9])
g.createEdge(vertice[4],vertice[5])
g.createEdge(vertice[4],vertice[6])
g.createEdge(vertice[4],vertice[10])
g.createEdge(vertice[5],vertice[8])
g.createEdge(vertice[5],vertice[10])
g.createEdge(vertice[6],vertice[10])
g.createEdge(vertice[6],vertice[7])

g.displayNodes() #displays the nodes in the graph

for i in range(1,11):
    g.displayConnected(vertice[i]) #itterates over all nodes displaying what they're connected to
