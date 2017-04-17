import random
import math

class Vertex:

    def __init__(self,dimension,index):
        """given dimension of point, random generate vertex point"""
        self.Dimension = dimension

        self.index = index # index of vertex

        self._point = [random.uniform(0,1) for i in range(dimension)]

    @staticmethod
    def Euclidean_distance(_pointA,_pointB):
        """calculate Euclidean distance between point A and B"""

        if(len(_pointA._point)!=len(_pointB._point)):
            print( "Points in different dimension!")
        else:
            return sum([(_pointA._point[i]-_pointB._point[i])**2 for i in range(len(_pointA._point))])**(0.5)


def main():
    # test
    pA = Vertex(1,1)
    pB = Vertex(1,2)

    Vertex.Euclidean_distance(pA,pB)

