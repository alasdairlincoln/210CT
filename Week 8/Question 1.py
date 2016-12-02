class Graph(object):
    '''Class for the graph'''
    def __init__(self):
        '''Creates an empty list for verticies to be stored in'''
        self.verticies = []
        self.edges = {}

    def insert(self, n):
        '''takes a vertex and appends the value of the vertex to the list verticies'''
        self.verticies.append(n.value)

    def createEdge(self, V1, V2, Weight):
        '''Takes 2 verticies and adds them to each others list of connected verticies'''
        self.edges[V1.value,V2.value] = Weight
        self.edges[V2.value,V1.value] = Weight

        if V2.value not in V1.connectedTo:
            V1.connectedTo.append(V2.value)
            V2.connectedTo.append(V1.value)
        else:
            print("There is already an edge there")

    def displayNodes(self):
        '''Prints the list of all nodes in the graph'''
        print("The current nodes in the graph are", self.verticies,"\n")

    def displayConnected(self, V1):
        '''Takes a vertex and calls the list of connected verticies'''
        V1.connected()

    def dijkstra(self, start, end):
        '''Takes a start node and end node and works out the
        shortest path between them'''
        node = start
        visited = []

        for n in self.verticies:
            vertice[n].tWeight = float('inf') # sets n.tWeight to infinty

        node.tWeight = 0 #sets the tentative weight of the first node to 0
        while node != end:
            for V in node.connectedTo: #runs throgugh all the nodes which are connected to the current node
                v = vertice[V] #sets v to a vertex as V is just an integer

                if node.tWeight + self.edges[node.value,v.value] < v.tWeight: #compares the weight to the current node to the old tentative
                    v.tWeight = node.tWeight + int(self.edges[v.value,node.value]) #if the weight to the current node is less than the old weight then its saved
                    v.pre = node #sets the nodes previous so that it can be used to backtrack the path

            visited.append(node)
            minimum = float('inf')
            for n in self.verticies: #checks over every vertex in the graph
                if vertice[n] not in visited and vertice[n].tWeight < minimum:#checks to see if the remaining verticies are better paths than the current one
                    node = vertice[n]
                    minimum = vertice[n].tWeight

        #calculates and prints the path from the end node to the start node
        n = end
        path = []
        path.append(n.value)
        while n != start:
            n = n.pre
            path.append(n.value)

        print("The path from",end.value, "to",start.value, "is" ,path)


class Vertex(object):
    '''Class for Vertex'''
    def __init__(self, value):
        '''Takes the value for the vertex and saves it to the instances value.
        Also creates an empty list to store all the vertices connected to the
        vetex called'''
        self.value = value
        self.connectedTo = []

    def connected(self):
        '''Prints the vertex and which nodes is connected to it'''
        print(self.value, "is connected to",self.connectedTo, "\n")

g = Graph()# Creates an instance of class graph called 'g'
vertice = {} #Creates a dictionary to store all verice variable names and values
for i in range(1,11):#a for loop to populate the dictionary with class instances
    vertice[i] = Vertex(i)

for i in range(1,11):#for loop to insert the nodes into the graph
    g.insert(vertice[i])

#creates an edge on the graph between the 2 specified verticies with the specified weight
g.createEdge(vertice[1],vertice[2], 5)
g.createEdge(vertice[1],vertice[6], 4)
g.createEdge(vertice[1],vertice[7], 1)
g.createEdge(vertice[1],vertice[9], 9)
g.createEdge(vertice[2],vertice[7], 3)
g.createEdge(vertice[2],vertice[4], 5)
g.createEdge(vertice[2],vertice[3], 12)
g.createEdge(vertice[3],vertice[5], 5)
g.createEdge(vertice[3],vertice[8], 4)
g.createEdge(vertice[3],vertice[9], 10)
g.createEdge(vertice[4],vertice[5], 10)
g.createEdge(vertice[4],vertice[6], 3)
g.createEdge(vertice[4],vertice[10], 1)
g.createEdge(vertice[5],vertice[8], 6)
g.createEdge(vertice[5],vertice[10], 7)
g.createEdge(vertice[6],vertice[10], 2)
g.createEdge(vertice[6],vertice[7], 2)

g.displayNodes() #displays the nodes in the graph

for i in range(1,11): #itterates over all nodes displaying what they're connected to
    g.displayConnected(vertice[i])

g.dijkstra(vertice[6],vertice[8]) #runs dijkstra algorith from the first vertex to the second
