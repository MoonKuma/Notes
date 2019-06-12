#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : Prim_MST_BinaryHeap.py
# @Author: MoonKuma
# @Date  : 2019/6/10
# @Desc  : indexed binary heap priority queue version of prim MST (eager solution)
# as a reference, see
# you may also want to check its simplified version in
# https://www.geeksforgeeks.org/prims-mst-for-adjacency-list-representation-greedy-algo-6/

import sys

def prims(n, edges, start):
    """
    This method includes 4 classes,
    a.Edge : the edge of graph, as well as key of heap
    b.Graph : the original graph
    c.IndexMinPQ : the indexed binary heap minimum priority queue
    d. EagerPrimMST : the MST class for compute(when initialized) and storing the finalized graph and sum of weights

    This is the standard implementation. It doesn't have to be this complicated to solve current problem
    For example, edge and graph could be simplified into lists

    :param n: number of nodes
    :param edges: edge list
    :param start: start position
    :return: total weight
    """

    class Edge():
        """
        Edge of graph, which also works as the key of binary heap pq
        The function either, other is clever for they are undirected for calling
        As key of heap, it has to implements compareTo()
        """
        def __init__(self, v, w, weight):
            self.v = v
            self.w = w
            self.weight = weight

        def either(self):
            return self.v

        def other(self, v):
            if v==self.v:
                return self.w
            else:
                return self.v

        def compareTo(self,u):
            if isinstance(u,Edge):
                if self.weight>u.weight:
                    return 1
                elif self.weight<u.weight:
                    return -1
                else:
                    return 0
            else:
                raise RuntimeError

    class Graph():
        """
        Use a adjacent list to store edges of the graph
        """
        def __init__(self, V):
            self.V = V
            self.adj = list()
            for v in range(0,V):
                bag = list()
                self.adj.append(bag)

        def addEdge(self, e):
            if isinstance(e, Edge):
                v = e.either()
                w = e.other(v)
                self.adj[v].append(e)
                self.adj[w].append(e)
            else:
                raise RuntimeError

        def adjEdge(self, v):
            return self.adj[v]

    class IndexMinPQ():
        def __init__(self):
            """
            pairs[i] is the pair of index and priority of heap position i, as [[index1, priority1], [index2, priority2],...]
            List of pair may be a more optimized structure for its easier to express the connection
            Also, actually you don't need to check the current edge selected of a given node

            pos[i] is the heap position of the key with index i
            """
            self.pairs = list()
            self.pos = list()
            self.size = 0

        def insert(self, i, key):
            self.size += 1
            pair = [i, key]
            self.pairs.append(pair)
            self.pos.append(self.size -1)
            self._swim(self.size-1)

        def delMin(self):
            if self.isEmpty() == True:
                return
            root = self.pairs[0]
            idx = root[0]
            self._exch(0,self.size-1)
            self.size = self.size -1
            self._sink(0)
            # self.pos[self.size] = None # this is not correct, its the heap become shallow not the position map
            # instead you could set he pos map for the node popped out to be None
            # self.pos[idx] = None
            return root

        def decreaseKey(self, i, key):
            """
            # Function decreaseKey is a special method for indexed binary heap which is used to change the priority
              connected to certain heap position
            # The calling of such function is decided by user, who has the responsibility to check
              1. whether the index exists inside heap
              2. whether the new priority is smaller
            # Since the new priority is smaller, _swim is needed after the modifying.
            :param i: index of priority (this may exist in the paris already)
            :param key: the priority (could be a new priority)
            """
            heap_idx = self.pos[i]
            self.pairs[heap_idx][1] = key
            self._swim(heap_idx)

        def contains(self, i):
            return self.pos[i]!=None and self.pos[i] < self.size

        def isEmpty(self):
            return self.size==0

        def size(self):
            return self.size

        # private methods
        def _swim(self, idx):
            while idx > 0 and self._less(idx, int((idx-1)/2)):
                self._exch(idx, int((idx-1)/2))
                idx = int((idx-1)/2)

        def _sink(self, idx):
            # 2*idx+1 < self.size, for the index of self.size is illegal
            while 2*idx+1 < self.size:
                j = 2*idx+1
                # j +1 < self.size is the bound for j++
                if j +1 <self.size and self._less(j+1, j):
                    j +=1
                if self._less(j,idx):
                    self._exch(idx, j)
                    idx = j
                else:
                    break



        def _exch(self, idx1, idx2):
            p1 = self.pairs[idx1]
            p2 = self.pairs[idx2]
            self.pairs[idx1] = p2
            self.pairs[idx2] = p1
            self.pos[p1[0]] = idx2
            self.pos[p2[0]] = idx1

        def _less(self, idx1, idx2):
            # caution with this
            if self.pairs[idx1][1].compareTo(self.pairs[idx2][1])<0:
                return True
            else:
                return False

    class EagerPrimMST():
        def __init__(self, G, start):
            if isinstance(G, Graph):
                max_int = sys.maxsize
                self.total_weight = 0
                self.node_finalized = list()
                indexMinPQ = IndexMinPQ()
                weights = list()
                for node in range(0, G.V):
                    indexMinPQ.insert(node, Edge(node,node,max_int))
                    weights.append(max_int)

                weights[start] = Edge(start,start,0).weight
                indexMinPQ.decreaseKey(start,  Edge(start,start,0))
                while not indexMinPQ.isEmpty():
                    top_pair = indexMinPQ.delMin()
                    self.node_finalized.append(top_pair[1])
                    self.total_weight += top_pair[1].weight
                    top_pair_idx = top_pair[0]
                    for edge in G.adjEdge(top_pair_idx):
                        v = edge.other(top_pair_idx)
                        if indexMinPQ.contains(v) and edge.weight<weights[v]:
                            weights[v] = edge.weight
                            indexMinPQ.decreaseKey(v, edge)

        def get_total_weight(self):
            return self.total_weight

        def report_connection(self):
            for edge in self.node_finalized:
                print([edge.either(), edge.other(edge.either()), edge.weight])


    def main(n, edges, start):
        start = start-1
        graph = Graph(n)
        for e in edges:
            edge_e = Edge(e[0]-1,e[1]-1,e[2])
            graph.addEdge(edge_e)
        mst = EagerPrimMST(graph, start)
        # mst.report_connection()
        return mst.get_total_weight()


    return main(n=n,edges=edges,start=start)


test_edges = [[1,2,3],[1,3,4],[4,2,6],[5,2,2],[2,3,5],[3,5,7]]
test_start = 1
n =5
print(prims(n=n, edges=test_edges,start=test_start))