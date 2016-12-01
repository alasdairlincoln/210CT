import os

class Graph(object):
    '''Class for the graph'''
    def __init__(self):
        '''Creates an empty list for verticies to be stored in'''
        self.verticies = []

    def insert(self, n):
        '''takes a vertex and appends the value of the vertex to the list verticies'''
        self.verticies.append(n.value)

    def createEdge(self, V1, V2):
        '''Takes 2 verticies and adds them to each others list of connected verticies'''
        if V2.value not in V1.connectedTo:
            V1.connectedTo.append(V2.value)
            V2.connectedTo.append(V1.value)
        else:
            print("There is already an edge there")

    def displayNodes(self):
        '''Prints the list of all nodes in the graph'''
        print("The current nodes in the graph are", self.verticies)

    def displayConnected(self, V1):
        '''Takes a vertex and calls the list of connected verticies'''
        V1.connected()

    def DFS(self, v):
        '''Takes a vertex and completes a depth first search
        starting at the given vertex'''
        stack = []
        visited = []
        vertex = v.value
        stack.append(vertex)
        while stack != []:
            temp = stack.pop()#removes the last item from the stack because its LIFO
            if temp not in visited:#makes sure the node hasnt already been visited
                visited.append(temp)#appends the node to list of visited
                for edges in vertice[temp].connectedTo:#itterates through the connected nodes
                    stack.append(edges)#appends all the connected nodes to the stack
        return visited

    def BFS(self, v):
        '''Takes a vertex and completes a breadth first search
        starting at the given vertex'''
        Queue = []
        visited = []
        vertex = v.value
        Queue.append(vertex)
        while Queue != []:
            temp = Queue.pop(0)#removes the first item from the Queue because its FIFO
            if temp not in visited:#makes sure the node hasnt already been visited
                visited.append(temp)#appends the node to list of visited
                for edges in vertice[temp].connectedTo:#itterates through the connected nodes
                    Queue.append(edges)#appends all the connected nodes to the Queue
        return visited

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

for i in range(1,11): #itterates over all nodes displaying what they're connected to
    g.displayConnected(vertice[i])

'''--- Week 7 Question 2 ---'''

#asks the user if they want to run the searches
run = input("Do you want to run the dfs and bfs on your graph? y/n ")
if run == "y":
    '''Runs the depth first search and breadth first search and saves the results to
    a text file called "Search Results.txt" it then opens the txt file in notepad'''
    dfs = str(g.DFS(vertice[5]))
    bfs = str(g.BFS(vertice[5]))
    File = open('Search Results.txt','w+')
    File.write("The results of the dfs were:"+ dfs + "\n")
    File.write("The results of the bds were:"+ bfs + "\n")
    os.startfile('Search Results.txt')
    File.close()

else:
    '''Please enter any new code after this point'''
