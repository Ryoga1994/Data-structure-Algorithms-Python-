
from vertex import Vertex
import random

class Edge:
    def __init__(self,verA,verB,weight_type):
        """generate edge from vertex A to B"""
        self.v = verA
        self.w = verB
        if weight_type == 'Euclidean':
            self.weight = Vertex.Euclidean_distance(verA,verB)
        else:
            # assign weight by choosing uniformly at random inside [0,1]

            self.weight = random.uniform(0,1)

    def other(self,idx):
        """given index of a vertex from one side of edge, return index of another"""

        if idx == self.v.index:
            return self.w.index
        elif idx == self.w.index:
            return self.v.index
        else:
            print("Inconsistent edge vertex.")

    def either(self):
        """return index of a point from either side of edge"""
        return self.v.index

    def toString(self):
        """print undirected edge"""
        print('%s - %s, weight = %f'%(str(self.v.index),str(self.w.index),self.weight))


def main():
    # test
    pA = Vertex(2,1)
    pB = Vertex(2,2)
    e = Edge(pA,pB)

    e.either() ==pA.index
    e.other(1)==pB.index
    e.toString()
