from EdgeWeightedGraph import EdgeWeightedGraph
import math
from IndexMinPQ import IndexedMinPQ


class PrimMST:
    """create Minimum Spaning Tree by Prim's Algorithm(eager version)"""

    def __init__(self, G):

        self.num_V = G.num_V # number of vertex
        # self.num_E = 0 # number of edges in MST for complete undirected graph is always |V|-1

        self.edgeTo =[0]*G.num_V # shortest edge from tree vertex, record index of vertex (feasible for primitive type)
        self.distTo = [math.inf]*G.num_V # distTo[w] = edgeTo[w].weight() ???

        self.marked = [False]*G.num_V # true if vertex already in MST (feasible for primitive type)

        # Priority queue records eligible crossing edges sorted by their distance to tree
        # <key,value> = <index of vertex, current min distance to tree)>
        self.pq = IndexedMinPQ()
        self.pq.insert(0,0) # initialize pq with vertex indexed 0 , weight 0

        while self.pq._heap:
            self.visit(G,self.pq.deleteMin()[0])

        self.sum_weight = sum(self.distTo[1:])
        self.max_weight = max(self.distTo[1:]) # max weight of edges in this graph

    def visit(self,G,v):
        """add vertex[v] to MST and update pq by vertex[v]'s adjacent edge"""

        # v is index of vertex
        self.marked[v] = True

        for e in G.adj[v]:
            w = e.other(v)
            if self.marked[w]: # w is already in MST
                continue
            if e.weight < self.distTo[w]:
                # edge e is a better connection from current MST to w
                # update e as current best connect to MST
                self.edgeTo[w] = v
                self.distTo[w] = e.weight

                # update MinPQ
                # self.pq[w] = self.distTo[w]
                self.pq.insert(w,self.distTo[w])

    def toString(self):
        """print MST"""
        print("Generated MST...")
        for i in range(1,len(self.edgeTo)):
            print('%d-%d,weight = %f'%(i,self.edgeTo[i],self.distTo[i]))

def main():

    G = EdgeWeightedGraph(16384,0)
    mst = PrimMST(G)

    mst.toString()

    mst.sum_weight



