# Advent of Code 2019

## Day 20: [Donut Maze](https://adventofcode.com/2019/day/20)
This was a shortest path problem.\
Part one was mainly building the graph and finding the shortest path using Dijkstra's algorithm.\
Part two was a bit more tricky, since the depth of the recursive spaces is unlimited.\
Fortunately the shortest path didn't go that deep.
### Optimizations:
* Simplifying the graph by removing the corridors (vertices connecting two other vertices) and connecting their neighbors directly with weighted edges.
* Using a priority queue (with `heapq`) to store the distances and vertices to process in Dijkstra's algorithm.
* For part two, in the customized Dijsktra's algorithm, we need to check the new distances against the current shortest distance to the destination, and avoid processing vertices that are too far away.
### Bugs and issues:
* Reading the portal labels was not so trivial. It took me a while to figure out all the labels are right-to-left or top-to-bottom.

## Day X: [Title](https://adventofcode.com/2019/day/X)
desc
### Optimizations:
### Bugs and issues:
