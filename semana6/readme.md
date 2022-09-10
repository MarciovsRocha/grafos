# Graph Search 

Simple Questions:

How to implement an algorithm to systematically traversal 
all the nodes of a graph enumerating the order that nodes 
are discovered?

we learned Dijkstra's algorithm to find the *shortest path*
between two nodes in terms of costs in a weighted graph.

This kind of algorithm is also used for the general tasks of 
search and traversal.

What is a Graph Search?

Refers to process of visiting each node of a graph in a systematic 
fashion starting from a source node and saving the order of nodes 
are visited. We can have the interest to find a given node (search) 
or not (traversal).

In general, the traversal does not solve a specific problem, but 
is an essential step for many tasks:

* Verify if a node of interest or which node are reachable from a starting node
* Finds a path between two nodes (not necessarily the shortest one)
* Verify is a graph is connected of ir the graph has cycles

## Depth-First Search

Strategy: it starts with the source node and first visits all nodes of one branch
as deep as possible. Then, after exploring all adjacent adges of the deeper node,
it performs *backtracking* and visits all other branches in a similar fashion.

* Stops when all nodes were explored or if a node of interest is found
* Can be implemented using a stack or recursion

```
- Push the starting node into the stack
- While stack is not empty
    - Pop an item from the stack
    - include it into the Visited-Nodes list (if not visited)
    - if the item is the node of interest
        - stop the algorithm and return Visited-nodes
    - else 
        - push the non-visited adjacent nodes into the stack
```

Depending on the graph structure, can be slow to find a solution.

But if your node of interest is located deeper in the graph, 
Depth-First Search will be a good option.

## Breadth-First Search

Strategy: it starts with the node and visits all nodes

```
- add the starting node into the Queue
- While the queue is not empty:
    - delete an item from the queue
    - include it into the Visited-nodes list (if not visited)
- if the item is the node of interest;
    - stop the algorithm and return Visited-Nodes
- else:
    - add the non-visited adjacent nodes into the queue
```
