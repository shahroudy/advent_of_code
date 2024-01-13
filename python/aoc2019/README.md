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

## Day 22: [Slam Shuffle](https://adventofcode.com/2019/day/22)
Simulating 3 different ways of shuffling cards.\
Part one was easy, just follow the instructions.\
Part two was a real challenge and maybe the beast of 2019; since the number of cards and the iterations are both very large.\
These made any brute force approach impossible.\
I had to find the pattern of the shuffling, and then calculate the final position of the card I was interested in.\
After some analysis I found all three shuffling operations and all of their possible combinations are actually a combination of `modular multiplication` and `modular addition`.\
This makes the operations requested in part two reduced to a single modular multiplication and a single modular addition.\
It's also good to know, `pow(n, p, m)` is a fast way to calculate `n^p % m`, and if you set `p=-1` it calculates the modular inverse of `n` with respect to `m` (with a condition of `n` and `m` being co-prime).

**One very important point to note in all AoC challenges is that there is always a super efficient way to solve all. This hint will help to avoid brute-force long-running solutions and think about a way to simplify or relax the problem; it's always either the input which can be simplified, or the algorithm that can be optimized.**\
**I believe this puzzle deserves to be recalled each year, since "Modular Arithmatic" can be a good topic for future years' puzzles.**

## Day 23: [Category Six](https://adventofcode.com/2019/day/23)
Another Intcode computer puzzle.\
This time 50 Intcode computers are communicating to each other via a network.\
Nothing challenging here, just simulating the network and adding a new running mode to Intcode computer implementation to operate when input is fed.

## Day X: [Title](https://adventofcode.com/2019/day/X)
desc
### Optimizations:
### Bugs and issues:
