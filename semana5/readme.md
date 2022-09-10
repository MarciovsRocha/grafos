# Day 5

## Graph planarity

A planar graph is a graph that can be drawn on 
the plane in such a way that its no edges cross 
each other. Otherwise, it is called non-planar

An complete bipartite graph $K_{3,3}$ isn't planar

Leonard Euler finds that all planar graph has some 
interesting properties related to the number of 
edges, nodes, and faces/region

*face is a region bounded by a set of edges and nodes*

### Euler Theorem 1 - Number of Regions

A simple, connected and planar graph with $v$ nodes and 
$a$ edges, *when drawn in its planar representation*, 
shows the following relation

$r=a-v+2$

*in which $r$ is the number of regions*

### Euler Theorem 2 - Number of Edges

if *G* is planar, then the following relation is true:

$$a \leq 3 * v - 6$$

if *G* is planar and bipartite, then the following relation is true:

$$a \leq 2 * v - 4$$

### Kuratowski's Theorem

How to determine if a graph is planar?

*G* is planar if and only if *G* has no $K_{5}$ subgraph 
and no $K_{3,3}$ subgraph 

to find a $K_{5}$ or a $K_{3,3}$ as subgraph into a graph, 
we can do some procedures of graph reduction:

* Edges Removing
* Nodes Removing
* Series reduction 

## Shortest Path Problem

### Dijkstra Algorithm

For a given source node in the graph, the algorithm finds the 
shortest path between that node and every other nodes

It can also be used for finding the shortest path from a node 
to a single destination by stopping the search when find the shortest path

It works on directed/undirected weighted graphs, since the
weights are positive

*For graphs with negative wights, we can use Bellman-Ford's Algorithm*

For each non-visited adjacent node of the current node:

* Compute the accumulated cost (current -> adjacent)
* Update the pair (accumulated cost, predecessor node) if the costs is lower
* If all adjacent nodes of the current node were verified mark the current node as *visited*
* Move the *pointer* of the current node to the **non-visited** node with the **lower accumulation cost**

```
def Dijkstra(self, source_node):
    visited = []
    cost = [ [np.inf,0] for i in range(self.order)]
    cost[source_node][0] = 0
    while len(visited) < self.order:
        for adj in adjacent_nodes:
            if adj not in visited:
                # compute the accumulated cost from current_node to adj
                # update the cost of adj if the value is lower than previous one
        visited.append(current_node)
        current_node = ajd_non_visited # non visited node with the minimun cost 
    return cost[source_node][0]
```

If the node of interest is close to the source node, BFS will find it fast
