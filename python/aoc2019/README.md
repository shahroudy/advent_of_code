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

## Day 21: [Springdroid Adventure](https://adventofcode.com/2019/day/21)
A simplifiled "Flappy Bird" game done in the Intcode computer.\
We only can jump from the ground, observing 4 (9 in part two) steps ahead of us.\
We have 4 (9 in part two) boolean registers (named `A, B, ..., I`) giving us the inputs, and one output register (`J`) to report the jump command to.\
In addition, we have one extra temporary register (`T`) for calculations.\
And we only have 3 commands: `AND`, `OR`, and `NOT`.\
The important point to jump is to ensure where you land is ground, which is 4 steps ahead.\
So if you see `A` is a hole and you want to jump, `D` must be ground.\
If not, it's too late to jump, and you need to look ahead to avoid such situation.\
My solution for part one was: 
$$
\bar A + D\bar B + D\bar C
$$ 

My solution for part one was: 
$$
\bar A + D \bar B (E+H) + D\bar C(E+H)
$$ 
Both needed to be implemented accordingly in springscript.

## Day X: [Title](https://adventofcode.com/2019/day/X)
desc
### Optimizations:
### Bugs and issues:
