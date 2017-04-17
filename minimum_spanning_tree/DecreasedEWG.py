from vertex import Vertex
from Edge import Edge

class D_EdgeWeightedGraph:
    """randomly generate complete weighted undirected graph with given dimension"""

    def __init__(self,numpoints,dimension,k_n):

        self.Dimension = dimension # dimension of vertex

        self.V = [Vertex(dimension,i) for i in range(numpoints)] # index range {0,1,2,...,V-1}

        self.num_V = numpoints
        self.num_E = 0  # number of edges in graph

        self.adj = {}   # adjacent list

        # initialize adjacent dictionary
        for i in range(self.num_V):
            self.adj[i]=[]

        # if dimension = 0 -> assign weights randomly
        if self.Dimension == 0:
            for i in range(numpoints - 1):
                for j in range(i + 1, numpoints):
                    new_edge = Edge(self.V[i], self.V[j],'random')
                    if new_edge.weight <= k_n:
                        self.adj[i].append(new_edge)
                        self.adj[j].append(new_edge)
                        self.num_E += 1

        else:
            # initialize edge for complete undirected graph
            for i in range(numpoints-1):
                for j in range(i+1,numpoints):
                    if Vertex.Euclidean_distance(self.V[i],self.V[j]) < k_n:
                        new_edge = Edge(self.V[i],self.V[j],'Euclidean')
                        self.adj[i].append(new_edge)
                        self.adj[j].append(new_edge)
                        self.num_E += 1


def main():

    # test

    numpoints = 10
    dimension = 1

    ewg = D_EdgeWeightedGraph(10,1,0.3)
    for v in ewg.V:
        print(v._point)

    ewg.num_E

    ewg.adj[9].append(Edge)

    for e in ewg.adj[9]:
        e.toString()

