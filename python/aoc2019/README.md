# Advent of Code 2019

## Day 1: [The Tyranny of the Rocket Equation](https://adventofcode.com/2019/day/1) &rarr; [Solution](./day01/d01.py)
## Day 2: [1202 Program Alarm](https://adventofcode.com/2019/day/2) &rarr; [Solution](./day02/d02.py)
## Day 3: [Crossed Wires](https://adventofcode.com/2019/day/3) &rarr; [Solution](./day03/d03.py)
## Day 4: [Secure Container](https://adventofcode.com/2019/day/4) &rarr; [Solution](./day04/d04.py)
## Day 5: [Sunny with a Chance of Asteroids](https://adventofcode.com/2019/day/5) &rarr; [Solution](./day05/d05.py)
## Day 6: [Universal Orbit Map](https://adventofcode.com/2019/day/6) &rarr; [Solution](./day06/d06.py)
## Day 7: [Amplification Circuit](https://adventofcode.com/2019/day/7) &rarr; [Solution](./day07/d07.py)
## Day 8: [Space Image Format](https://adventofcode.com/2019/day/8) &rarr; [Solution](./day08/d08.py)
## Day 9: [Sensor Boost](https://adventofcode.com/2019/day/9) &rarr; [Solution](./day09/d09.py)
## Day 10: [Monitoring Station](https://adventofcode.com/2019/day/10) &rarr; [Solution](./day10/d10.py)
## Day 11: [Space Police](https://adventofcode.com/2019/day/11) &rarr; [Solution](./day11/d11.py)
## Day 12: [The N-Body Problem](https://adventofcode.com/2019/day/12) &rarr; [Solution](./day12/d12.py)
## Day 13: [Care Package](https://adventofcode.com/2019/day/13) &rarr; [Solution](./day13/d13.py)
## Day 14: [Space Stoichiometry](https://adventofcode.com/2019/day/14) &rarr; [Solution](./day14/d14.py)
## Day 15: [Oxygen System](https://adventofcode.com/2019/day/15) &rarr; [Solution](./day15/d15.py)
## Day 16: [Flawed Frequency Transmission](https://adventofcode.com/2019/day/16) &rarr; [Solution](./day16/d16.py)
## Day 17: [Set and Forget](https://adventofcode.com/2019/day/17) &rarr; [Solution](./day17/d17.py)
## Day 18: [Many-Worlds Interpretation](https://adventofcode.com/2019/day/18) &rarr; [Solution](./day18/d18.py)
## Day 19: [Tractor Beam](https://adventofcode.com/2019/day/19) &rarr; [Solution](./day19/d19.py)

## Day 20: [Donut Maze](https://adventofcode.com/2019/day/20) &rarr; [Solution](./day20/d20.py)
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

## Day 21: [Springdroid Adventure](https://adventofcode.com/2019/day/21) &rarr; [Solution](./day21/d21.py)
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

## Day 22: [Slam Shuffle](https://adventofcode.com/2019/day/22) &rarr; [Solution](./day22/d22.py)
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

## Day 23: [Category Six](https://adventofcode.com/2019/day/23) &rarr; [Solution](./day23/d23.py)
Another Intcode computer puzzle.\
This time 50 Intcode computers are communicating to each other via a network.\
Nothing challenging here, just simulating the network and adding a new running mode to Intcode computer implementation to operate when input is fed.

## Day 24: [Planet of Discord](https://adventofcode.com/2019/day/24) &rarr; [Solution](./day24/d24.py)
A cellular automaton puzzle.\
The state of each cell (in a 5x5 grid) is a function of its neighbors at the previous step.\
Not much of a challenge, just simulating the automaton and:
* finding the first repeated state in part one,
* extend the automaton to a recursive 3D space and run for some iterations in part two.
### Optimizations:
* Using a `set` to store the bugged cells can make it more efficient.

## Day 25: [Cryostasis](https://adventofcode.com/2019/day/25) &rarr; [Solution](./day25/d25.py)
And the final puzzle of 2019, a text based game running on our IntCode computer.\
The game is a maze with some items to collect and some doors to open.\
Here I tried to implement a simple algorithm to explore the map, collect the items, and open the doors.\
And when done exploring and collecting, go to the security checkpoint and try to find the proper set of items to pass the security check.\
This year's advent of code finishes with a message from Santa:

```A loud, robotic voice says "Analysis complete! You may proceed." and you enter the cockpit.
Santa notices your small droid, looks puzzled for a moment, realizes what has happened, and radios your ship directly.
"Oh, hello! You should be able to get in by typing xxxxxx on the keypad at the main airlock."
```