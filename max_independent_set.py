# assignment 3, problem 7


def MLS(G,u):
    """return size and max independent set in given tree graph rooted at u"""

    if len(G.adj(u)) == 0:  # leaf node does not have child
        return 1

    set_1 = []
    set_2 = []

    for w in G.adj(u): # child node of u
        set_1.join(MLS(G,w))

        for grad_c in G.adj(w): # grad children of u
            set_2.join(MLS(G,grad_c))


    if len(set_1) > len(set_2) + 1:
        return set_1

    return set_2

# dynamic programming to process in linear time

