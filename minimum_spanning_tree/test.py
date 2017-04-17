

if __name__ == "__main__":
    import sys
    from PrimMST import PrimMST
    from DecreasedEWG import D_EdgeWeightedGraph
    from EdgeWeightedGraph import EdgeWeightedGraph


    flag = int(sys.argv[1])
    numpoints = int(sys.argv[2])
    numtrials = int(sys.argv[3])
    dimension = int(sys.argv[4])

    ave_weight = []
    max_weight = []

    # set threshold of weights
    k_n = 10 * numpoints**(-0.9) # for dimension = 0
    # k_n = 0.2
    # simulate trials
    for i in range(numtrials):
        # generate random complete undirected graph

        # math.pow(0.0001,1/(numpoints-1))

        G = D_EdgeWeightedGraph(numpoints,dimension,k_n)

        # G = EdgeWeightedGraph(numpoints,dimension)
        mst = PrimMST(G)

        # debug
        if flag == 0:
            mst.toString()

        ave_weight.append(mst.sum_weight)
        max_weight.append(mst.max_weight)

    print("%f %d %s %s"%(sum(ave_weight)/numtrials,numpoints,numtrials,dimension))
    print("max weight in %d trials: %f"%(numtrials,max(max_weight)))
    print(ave_weight)
