#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : Kruskal_MST_BinarySort.py
# @Author: MoonKuma
# @Date  : 2019/6/12
# @Desc  : Another MST problem, see https://www.hackerrank.com/challenges/kruskalmstrsub/problem, with kruskal solution
# Kruskal solution is a combination with find-union(to decide the cycle) and binary heap sort(pick minimal weights)
# Kruskal has a complexity of O(ElogE), while eager Prim's method is O(ElogV)
# BTW, The Prim method works as fine


def kruskals(g_nodes, g_from, g_to, g_weight):

    edges = []
    for i in range(0,len(g_from)):
        edges.append([g_from[i], g_to[i], g_weight[i]])
    start = 1
    n = g_nodes

    # the Prim's method works here
    """
    For self-educated purpose. Here we use a standard solution with 5 classes include
    a. Edge
    b. Graph
    c. MinBinaryHeap
    d. FindUnion
    e. KruskalsMST
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
            self.edges = list()
            for v in range(0,V):
                bag = list()
                self.adj.append(bag)

        def addEdge(self, e):
            if isinstance(e, Edge):
                v = e.either()
                w = e.other(v)
                self.adj[v].append(e)
                self.adj[w].append(e)
                self.edges.append(e)
            else:
                raise RuntimeError

        def adjEdge(self, v):
            return self.adj[v]

    class MinBinaryHeap():
        """
        The binary heap with no index is such neat and easy (sigh)
        """
        def __init__(self):
            self.array = list()
            self.size = 0

        def isEmpty(self):
            return self.size==0

        def insert(self, key):
            self.size += 1
            self.array.append(key)
            self._swim(self.size-1)

        def delMin(self):
            if self.isEmpty() == True:
                return
            root = self.array[0]
            self._exch(0,self.size-1)
            self.size = self.size -1
            self._sink(0)
            return root

        # private
        def _swim(self, idx):
            while idx > 0 and self._less(idx, int((idx-1)/2)):
                self._exch(idx, int((idx-1)/2))
                idx = int((idx-1)/2)

        def _sink(self, idx):
            while 2*idx+1 < self.size:
                j = 2*idx+1
                if j +1 <self.size and self._less(j+1, j):
                    j +=1
                if self._less(j,idx):
                    self._exch(idx, j)
                    idx = j
                else:
                    break

        def _exch(self, idx1, idx2):
            p1 = self.array[idx1]
            p2 = self.array[idx2]
            self.array[idx1] = p2
            self.array[idx2] = p1

        def _less(self, idx1, idx2):
            if self.array[idx1].compareTo(self.array[idx2])<0:
                return True
            else:
                return False

    class FindUnion():
        def __init__(self, N):
            self.id_list = list()
            self.sz_list = list()
            for i in range(0, N):
                self.id_list.append(i)
                self.sz_list.append(1)

        def root(self, i):
            while i != self.id_list[i]:
                # Path compression, this is not necessary, but it helps flatting the structure
                self.id_list[i] = self.id_list[self.id_list[i]]
                # original find func
                i = self.id_list[i]
            return i

        def union(self, p, q):
            i = self.root(p)
            j = self.root(q)
            if i == j:
                return
            # the size list help to balance each tree (the smaller branch get attached to the larger )
            if self.sz_list[i] < self.sz_list[j]:
                self.id_list[i] = j
                self.sz_list[j] += self.sz_list[i]
            else:
                self.id_list[j] = i
                self.sz_list[i] += self.sz_list[j]

        def is_connected(self, p, q):
            return self.root(p) == self.root(q)

    class KruskalMST():
        def __init__(self, G):
            if isinstance(G, Graph):
                self.total_weight = 0
                self.node_finalized = list()
                pq = MinBinaryHeap()
                fu = FindUnion(G.V)
                for edge in G.edges:
                    pq.insert(edge)
                while pq.isEmpty()==False and len(self.node_finalized)<G.V -1:
                    edge = pq.delMin()
                    if isinstance(edge, Edge):
                        v = edge.either()
                        w = edge.other(v)
                        weight = edge.weight
                        if not fu.is_connected(v, w):
                            self.total_weight += weight
                            self.node_finalized.append(edge)
                            fu.union(v, w)

        def get_total_weight(self):
            return self.total_weight

        def report_connection(self):
            for edge in self.node_finalized:
                print([edge.either(), edge.other(edge.either()), edge.weight])


    def main(n, edges):
        graph = Graph(n)
        for e in edges:
            edge_e = Edge(e[0]-1,e[1]-1,e[2])
            graph.addEdge(edge_e)
        mst = KruskalMST(graph)
        mst.report_connection()
        return mst.get_total_weight()

    return main(n=n,edges=edges)


