class graph:
    def __init__(self, graphData=None):
        if graphData is None:
            graphData = {}
        self.graphData = graphData

    # Get the vertices of the graph.
    def getVertices(self):
        return set(self.graphData.keys())

    # Get the edges of the graph.
    def getEdges(self):
        edgeList = []

        for vertex in self.graphData:
            for nextVertex in self.graphData[vertex]:
                if {nextVertex, vertex} not in edgeList:
                    edgeList.append({vertex, nextVertex})

        return edgeList

    # Add a vertex to the graph.
    def addVertex(self, vertex):
        if vertex not in self.graphData:
            self.graphData[vertex] = {}

    # Add an edge.
    def addEdge(self, edge):
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)

        if vertex1 in self.graphData:
            self.graphData[vertex1].append(vertex2)
        else:
            self.graphData[vertex1] = [vertex2]

data = {
    "a": ["b", "c"],
    "b": ["a", "d"],
    "c": ["a", "d"],
    "d": ["e"],
    "e": ["d"]
}

theGraph = graph(data)
print(theGraph.getVertices())
print(theGraph.getEdges())

theGraph.addVertex("f")
print(theGraph.getVertices())

theGraph.addEdge({"a","e"})
theGraph.addEdge({"a","c"})
print(theGraph.getEdges())
