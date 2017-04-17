

if __name__ == "__main__":
    import sys
    from PrimMST import PrimMST
    from EdgeWeightedGraph import EdgeWeightedGraph

    flag = int(sys.argv[1])
    numpoints = int(sys.argv[2])
    numtrials = int(sys.argv[3])
    dimension = int(sys.argv[4])

    ave_weight = []

    # simulate trials
    for i in range(numtrials):
        # generate random complete undirected graph
        G = EdgeWeightedGraph(numpoints,dimension)
        mst = PrimMST(G)

        # debug
        if flag==1:
            mst.toString()

        ave_weight.append(mst.sum_weight)

    print("%f %d %s %s"%(sum(ave_weight)/numtrials,numpoints,numtrials,dimension))








