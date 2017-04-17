
class _Node(object):

    def __init__(self, key, value):
        self.key = key # index of node
        self.value = value # comparable value in node(weight in this case)

class IndexedMinPQ:

    # invariant: parent node <= child node

    def __init__(self):
        self.size = 0  # number of items in PQ
        self._heap = [] # with node as element
        self._position = {} # dictionary {key:position_index in heap}

    def insert(self,key, value):
        """insert value and associate it with key, if exist updated correspondent value"""
        if key in self._position:
            # reset value for this node
            node_pos = self._position[key]
            node = self._heap[node_pos]
            node.value = value
            self._sink(node_pos)
            self._swim(node_pos)
        else:
            # insert a new node
            new_node = _Node(key,value)
            node_pos = len(self._heap)
            self._heap.append(new_node)
            self._position[key] = node_pos

            # repair priority
            self._swim(node_pos)

    def deleteMin(self):
        """remove k and its associated item from PQ and return (key,value)"""
        heap = self._heap
        position = self._position

        try:
            end = heap.pop(-1)
        except IndexError:
            raise KeyError('pqdict is empty')

        if heap:
            node = heap[0]
            # grab last node in PQ to root and sink it down appropriately
            heap[0] = end
            position[end.key] = 0
            self._sink(0)
        else:
            node = end
        del position[node.key] # delete index from position dict
        return node.key, node.value

    def _sink(self, top=0):
        # "Sink-to-the-bottom-then-swim" algorithm (Floyd, 1964)
        # Tends to reduce the number of comparisons when inserting "heavy"
        # items at the top, e.g. during a heap pop. See heapq for more details.
        heap = self._heap
        position = self._position

        endpos = len(heap)

        # Grab the top node
        pos = top
        node = heap[pos]

        # Sink a chain of child nodes
        child_pos = 2 * pos + 1
        while child_pos < endpos:
            # Choose the smaller child.
            other_pos = child_pos + 1
            if other_pos < endpos and heap[child_pos].value > heap[other_pos].value:
                child_pos = other_pos

            child_node = heap[child_pos]
            # Move it up one level.
            heap[pos] = child_node
            position[child_node.key] = pos
            # Next level (down to leaf)
            pos = child_pos
            child_pos = 2 * pos + 1

        # We are left with a "vacant" leaf. Put our node there and let it swim
        # until it reaches its new resting place.
        heap[pos] = node
        position[node.key] = pos
        self._swim(pos, top)

    def _swim(self, pos, top=0):
        heap = self._heap
        position = self._position

        # Grab the node from its place
        node = heap[pos]
        # Swim parents up to root until we find a place where the node fits.
        while pos > top:
            parent_pos = (pos - 1) >> 1
            parent_node = heap[parent_pos]
            if node.value < parent_node.value:
                heap[pos] = parent_node
                position[parent_node.key] = pos
                pos = parent_pos
                continue
            break
        # Put node in its new place
        heap[pos] = node
        position[node.key] = pos

    def toString(self):
        for node in self._heap:
            print(node.key,node.value)
        print(self._position)


def main():
    minPQ = IndexedMinPQ()
    minPQ.insert(3,5)
    minPQ.insert(4,1)
    minPQ.insert(2,8)
    minPQ.insert(1,4)
    minPQ.insert(10,2)
    minPQ.insert(-10,-1)
    minPQ.deleteMin()
    minPQ.change(4,2)

    minPQ.toString()





