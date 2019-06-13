#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : BFS_BinarySort.py
# @Author: MoonKuma
# @Date  : 2019/6/13
# @Desc  : the Dijkstra solution with binary sort optimization
# See https://www.hackerrank.com/challenges/dijkstrashortreach/problem
# The binary heap method is such useful

import sys

def shortestReach(n, edges, s):

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
                # use dict bag instead of list bag for the duplicated issue (this will cause a memory leak)
                bag = dict()
                self.adj.append(bag)

        def addEdge(self, e):
            if isinstance(e, Edge):
                v = e.either()
                w = e.other(v)
                # only adding the edges with smaller weight
                if self.adj[v].setdefault(w, Edge(v,w,sys.maxsize)).weight > e.weight:
                    self.adj[v][w] = e
                    self.adj[w][v] = e
            else:
                raise RuntimeError

        def adjEdge(self, v):
            return self.adj[v].values()

    # Here we need a indexed version though, for we need the decreaseKey method
    class IndexedMinBinaryHeap():
        def __init__(self):
            self.pairs = []
            self.pos = []
            self.size = 0

        def insert(self, i, key):
            # caution with order
            self.size += 1
            self.pairs.append([i, key])
            self.pos.append(self.size-1)
            self._swim(self.size-1)

        def delMin(self):
            # caution with the empty testify
            if self.isEmpty() == True:
                return
            root = self.pairs[0]
            self._swap(0,self.size-1)
            self.pairs[self.size-1] = None
            self.size -= 1
            self._sink(0)
            return root

        def isEmpty(self):
            return self.size == 0

        def contains(self, i):
            return self.pos[i]<self.size

        def decreaseKey(self, i, key):
            i_pos = self.pos[i]
            self.pairs[i_pos] = [i, key]
            self._swim(i_pos)

        # private
        def _swap(self,i,j):
            pair_i = self.pairs[i]
            pair_j = self.pairs[j]
            self.pairs[i] = pair_j
            self.pairs[j] = pair_i
            self.pos[pair_i[0]] = j
            self.pos[pair_j[0]] = i


        def _less(self,i,j):
            key_i = self.pairs[i][1]
            key_j = self.pairs[j][1]
            if isinstance(key_i,Edge) and isinstance(key_j, Edge):
                if key_i.compareTo(key_j)<0:
                    return True
                else:
                    return False

        def _swim(self, i):
            while i>0 and self._less(i,int((i-1)/2)):
                self._swap(i, int((i-1)/2))
                i = int((i-1)/2)

        def _sink(self, i):
            while 2*i+1<self.size:
                j = 2*i+1
                if j+1<self.size and self._less(j+1,j):
                    j = j+1
                if self._less(j,i):
                    self._swap(i,j)
                    i = j
                else:
                    break

    class Dijkstra():
        def __init__(self, G, start):
            if isinstance(G, Graph):
                MAX_INT = sys.maxsize
                self.result_array = list()
                for i in range(0,G.V):
                    self.result_array.append(MAX_INT)
                self.result_array[start] = 0
                self.visited = list()
                pq_graph = IndexedMinBinaryHeap()
                for v in range(0, G.V):
                    pq_graph.insert(v, Edge(start,v,MAX_INT))
                pq_graph.decreaseKey(start,Edge(start,start,0))
                while len(self.visited)<G.V:
                    current_min = pq_graph.delMin()[1]
                    if isinstance(current_min, Edge):
                        v = current_min.other(start)
                        self.visited.append(current_min)
                        for edge in G.adjEdge(v):
                            if isinstance(edge,Edge):
                                w = edge.other(v)
                                if self.result_array[w]>self.result_array[v] + edge.weight:
                                    self.result_array[w] = self.result_array[v] + edge.weight
                                    pq_graph.decreaseKey(w, Edge(start,w,self.result_array[w]))

        def get_result_array(self):
            return self.result_array

        def report_trace(self):
            print('Trace Below')
            for edge in self.visited:
                if isinstance(edge, Edge):
                    print([edge.either(),edge.other(edge.either()),edge.weight])

    def main(n, edges, s):
        start = s -1
        graph = Graph(n)
        for edge in edges:
            graph.addEdge(Edge(edge[0]-1, edge[1]-1, edge[2]))
        dij = Dijkstra(graph,start)
        dij.report_trace()
        result =  dij.get_result_array()
        print_result = list()
        for i in range(0,n):
            if result[i] == sys.maxsize:
                print_result.append(-1)
            elif i==start:
                continue
            else:
                print_result.append(result[i])

        return print_result

    return main(n=n,edges=edges,s=s)


test_edges = [[1,2,24],[1,4,20],[3,1,3],[4,3,12]]
test_s = 1
test_n = 4
print('Result:',shortestReach(test_n,test_edges,test_s))