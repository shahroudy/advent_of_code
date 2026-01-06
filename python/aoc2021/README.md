# Advent of Code 2021

## Day 1: [Sonar Sweep](https://adventofcode.com/2021/day/1) &rarr; [Solution](./day01/d01.py)
We are provided with a list of integers (as depth levels) and we need to find:
* Part 1: How many times we have an increase in depth level.
* Part 2: How many times we have an increase in the sum of 3 consecutive depth levels.

### Optimizations:
* In part 2, one can simply find the number of times `depths[i+3] > depths[i]`.

## Day 2: [Dive](https://adventofcode.com/2021/day/2) &rarr; [Solution](./day02/d02.py)
We are provided with a list of pairs of directions and values.\
Directions are `forward`, `down`, and `up`.\
In part 1, we move in 2D based on the directions and values.\
In part 2, `up` and `down` only move an "aim" value, and `forward` moves based on the value
horizontally, and based on the value multiplied by the "aim" vertically.\
In both parts, we need to calculate the `x*y` of the final position.\
Use of the internal library classes of `Point2D` and `Point3D` helped here.\
In part 2, we can use the `Point3D` class to keep track of the position and the aim.

## Day 3: [Binary Diagnostic](https://adventofcode.com/2021/day/3) &rarr; [Solution](./day03/d03.py)
We are provided with a list of binary numbers.\
In part 1 we need to find the number consisting of most common bits at each position, multiplied by
the number consisting of least common bits.\
In part 2, we need to iteratively find the most common bit and filter the list and only keep the
numbers that have that bit at that position.\
We iterate until we have only one number left, and that would be the result.\
In the case of equal counts, `1` is picked.\
Similarly we find the result for least common bit (picking `0` on equal counts).\
And then multiply these two together to get the final answer.

One can use the `Counter` class from the `collections` module to find the most and
least common bits.\
I preferred to implement the logic myself, mainly using `str` values directly.

### Optimizations:
* In part 1, the least common bits are actually the complement of the most common bits, so we don't
* need to calculate them separately.

## Day 4: [Giant Squid](https://adventofcode.com/2021/day/4) &rarr; [Solution](./day04/d04.py)
Simulating a game of Bingo!.\
We are provided with a list of integers, and a set of 2D boards of numbers.\
The input numbers will be read in order, and we need to find the first winning board.\
A winning board is a board where all the numbers in a row or a column are already read.\
We need to find the first and last winning boards.\
This puzzle is mainly a warm-up on handling 2D arrays and lists.

## Day 5: [Hydrothermal Venture](https://adventofcode.com/2021/day/5) &rarr; [Solution](./day05/d05.py)
We are provided with the two ends of a number of line segments and need to find the number of
overlap points between them.\
Lines are either horizontal, vertical, or 45-degree diagonal.\
In part 1, we only consider horizontal and vertical lines.\
In part 2, we also consider diagonal lines.

### Optimizations:
* The fact that the diagonal lines are always at 45 degrees simplifies the calculations a lot.
* Data structures needed here are two sets of point-coordinates for visited and overlapping points.

### Bugs and Issues:
* For part 2, I implemented a very general solution that can handle any angle of diagonal lines,
which was not needed!

## Day 6: [Lanternfish](https://adventofcode.com/2021/day/6) &rarr; [Solution](./day06/d06.py)
We are provided with a list of numbers, representing the remaining days each lanternfish creates
another one.\
Each lanternfish, at each step (say a day) gets its timer value decreased by 1.\
If the timer value is `0`, it will reset to `6` and create a new lanternfish with
remaining `8` days.\
We need to find the number of lanternfish after a given number of days (`80` and `256` days in
parts 1 and 2 respectively).

### Optimizations:
* We don't care about any order or individual fish, so we can simply keep track of the number of
* lanternfish with each timer value at each time step!

## Day 7: [The Treachery of Whales](https://adventofcode.com/2021/day/7) &rarr; [Solution](./day07/d07.py)
We have a list of integers representing the horizontal positions of crabs.\
We need to find the horizontal position that minimizes the sum of distances to all crabs.\
In part 2, each step of a move will increase the needed fuel by one.

### Optimizations:
* For part 2, we can find the needed fuel analytically by using the formula for the sum of the
first n integers: `n * (n + 1) // 2`.

## Day 8: [Seven Segment Search](https://adventofcode.com/2021/day/8) &rarr; [Solution](./day08/d08.py)
Interesting puzzle of handling shuffled segments of a seven-segment display, like this:
```
 aaaa
b    c
b    c
 dddd
e    f
e    f
 gggg
```
For each line of the input file, we have a one-to-one mapping between the actual segments, and
the puzzle is to find that mapping.\
Each line of the input actually has two parts: input digits and output digits, separated by `|`.\

In part 1, we only need to count the number of times the digits `1`, `4`, `7`, or `8` appear in
the output.\
These four digits have a unique number of segments turned on: `2`, `4`, `3`, and `7` respectively.\
So we can simply count the number of words in the output part that have these lengths.\
This is actually a clue to solve part 2 as well.

In part 2, we need to find the actual mapping of segments for each line, and then decode the
output digits based on that mapping.\
The answer will be the sum of all the decoded output "numbers".

The brute-force search to find the mapping is tractable and maybe the quickest way to implement it.

### Optimizations:
Using the clues from part 1, we can find the segments `a`, `b`, `c`, `d`, `e`, `f`, and `g` by
analyzing the intersection and differences of the sets of characters in the words with
unique lengths.\
For each line, we can group the words by their lengths, and then find the common segment codes
for each length.\
Fortunately, all the input lines in the samples and the puzzle input include all the digits
from `0` to `9`, which makes this solution work.\
In the original (not shuffled) segments, we have these segments in common for each length:
* Length 2: segments `c` and `f` (digit `1`)
* Length 3: segments `a`, `c`, and `f` (digit `7`)
* Length 4: segments `b`, `c`, `d`, and `f` (digit `4`)
* Length 5: segments `a`, `d`, and `g` (digits `2`, `3`, and `5`)
* Length 6: segments `a`, `b`, `f`, and `g` (digits `0`, `6`, and `9`)
* Length 7: all the segments (digit `8`), like:
```
                 aaaa                  aaaa       aaaa       aaaa
          c          c     b    c                b          b    c
          c          c     b    c                b          b    c
  2:         3:         4:  dddd   5:  dddd   6:         7:  dddd
          f          f          f                     f     e    f
          f          f          f                     f     e    f
                                       gggg       gggg       gggg
```
Alright, now we can find the segments one by one:
* Segment `a` is in length 3 but not in length 2.
* Segment `b` is in length 6 but not in length 5 and not in 2
* Segment `c` is in length 2 but not in length 6.
* Segment `d` is in the only one in both length 4 and length 5.
* Segment `e` is in length 7 but not in lengths 6, 5, and 2.
* Segment `f` is the one in both lengths 2 and 6.
* Segment `g` is the one in length 5 and 6 but not in lengths 3.

This way one can easily find the segment mapping and then decode the output digits.

## Day 9: [Smoke Basin](https://adventofcode.com/2021/day/9) &rarr; [Solution](./day09/d09.py)
An easy puzzle of handling 2D array of digits to find local minima and their connected basins.\
In part 1, we need to find all the points which are lower than all of their adjacent points (in 4 directions).\
In part 2, we need to find the sizes of the basins connected to these low points.\
A basin is defined as all the points that are connected to a low point and are not `9`.\
For this puzzle, my library class `Point`, its `n4` method, and
the library function `connected_region` were very handy.

## Day 10: [Syntax Scoring](https://adventofcode.com/2021/day/10) &rarr; [Solution](./day10/d10.py)
Handling nested blocks of brackets of four different types: `()`, `[]`, `{}`, and `<>`.\
The input consists of multiple lines of these characters.\
In part 1, we need to find the invalid lines, where a closing bracket does not match the most recent
opening one.\
In part 2, we need to list the missing closing brackets for the incomplete lines and calculate
an score based on that.\
The solution for this puzzle is to keep the opening brackets in a stack and check the top of the
stack when we observe a closing bracket.

## Day 11: [Dumbo Octopus](https://adventofcode.com/2021/day/11) &rarr; [Solution](./day11/d11.py)
The first cellular automaton puzzle of the year!\
The input is a 2D grid of digits representing the energy levels of octopuses.\
At each step, the energy level of each octopus increases by 1.\
Octopuses with energy level above 9 flash and their energy level is reset to 0.\
Each flash also causes adjacent octopuses (in 8 directions) to get their energy levels increased
by 1 as well (only the ones which has not flashed in this step).\
In part 1, we need to find the total number of flashes after `100` steps.\
In part 2, we need to find the first step where all octopuses flash together.\
The Pythonic solution here is to use `dict` to represent the 2D grid, where keys are
`Point` objects and values are the energy levels.\
The library class `Point` and its `n8` method were very useful here.\
The brute-force simulation is straightforward and efficient enough for this puzzle.

## Day 12: [Passage Pathing](https://adventofcode.com/2021/day/12) &rarr; [Solution](./day12/d12.py)
This is a must-read-carefully puzzle about finding paths through a graph with specific rules.\
The input gives us the edges of an undirected graph, where nodes are named with
upper-case or lower-case strings.\
Upper-case nodes can be visited any number of times, while lower-case nodes can be visited
at most once (in part 1) or at most twice for only one of them (in part 2).\
We need to count all the paths from the `start` node to the `end` node (without revisiting
either of the two).\
To solve this puzzle, I added a new variant to my `Search` library named `Search_All_Goals` that
finds all the possible solutions.\
The rest for this puzzle is to override the `get_next_states` method to implement the specific rules
of this puzzle.

## Day 13: [Transparent Origami](https://adventofcode.com/2021/day/13) &rarr; [Solution](./day13/d13.py)
A puzzle of folding a transparent origami paper.\
We are provided with a set of points on a 2D grid, and a set of fold instructions
(along `x` or `y`).\
We need to simulate the folding of the paper and:
* find the number of points after the first fold (part 1)
* find the code formed by the points after all folds (part 2)

### Bugs and Issues:
* Note the difference between this fold operation and the 2D reflection.
In folding here, if the point is on the left/top side of the fold line, it remains unchanged.

## Day 14: [Extended Polymerization](https://adventofcode.com/2021/day/14) &rarr; [Solution](./day14/d14.py)
In this puzzle, we have to count the number of each element's quantity after a number of
polymerization steps.\
The input consists of a polymer template (string) and a set of polymerization rules
(pair insertion).\
At each step, every pair of elements may insert another element between them according to the
polymerization rules.\
In part 1, we need to run this for `10` steps, and in part 2 for `40` steps.\
The brute-force implementation of the polymerization process works for part 1, but is not tractable
for part 2.

### Optimizations:
* Instead of keeping track of the entire polymer string, we can keep track of the counts of each
pair of elements. At each step, we can update the counts of pairs based on the polymerization rules.
* There is still a tweak needed to calculate the quantity of each element from the counts of pairs:
  * Each element (except the first and the last ones) is counted twice, once in each pair.
  * So we need to divide the counts by 2, and add 1 to the counts of the first and last elements.

## Day 15: [Chiton](https://adventofcode.com/2021/day/15) &rarr; [Solution](./day15/d15.py)
A typical shortest-path puzzle on a 2D map of digits.\
Each digit represents a risk level and we need to find the minimum-risk path from the top-left to
the bottom-right corner.\
In part 2, the map is extended 5 times in each direction with a twist in the calculation of the
risk levels.\
Having `DijkstraSearch` class in my `Search` library made this puzzle very straightforward to
implement.\
And to read the input, I had the `read_map_of_digits` function in `myutils.utils` as well.

## Day 16: [Packet Decoder](https://adventofcode.com/2021/day/16) &rarr; [Solution](./day16/d16.py)
In this puzzle, we are provided with a hexadecimal string of digits (that must be converted to
binary) and need to parse it to a graph of numbers (packets) based on the given rules.\
Each packet has three parts:
* version (3 bits)
* type ID (3 bits)
* value or sub-packets (variable length)
In part 1, we need to fully parse the graph of packets and find the sum of all version numbers.\
In part 2, we need to evaluate the value of the root packet based on the given operation rules
(sum, product, min, max, etc.).\

The key idea to solve this puzzle is to implement a recursive function that receives the binary
string and the starting index, and returns the value of the parsed packet.

## Day 17: [Trick Shot](https://adventofcode.com/2021/day/17) &rarr; [Solution](./day17/d17.py)
This puzzle is about simulating a "Two-Dimensional Projectile Motion" with acceleration in both of
the axes.\
In the input, we are provided with a target area defined by a rectangle in 2D space.\
And we need to find all the possible initial velocity values that will cause the projectile to
land/pass the target area (starting at the origin).\
In part 1, we need to find the highest `y` position reached by any of these valid trajectories.\
In part 2, we need to find the number of all valid initial velocity values.

I implemented a brute-force simulation of all possible initial velocity values within a reasonable
range.\
Good news is that there are points that can relax the problem:
* The initial `x` velocity should always be positive (to reach the target area on the right side).
* The initial `y` velocity can be negative, but its absolute value cannot be more than the absolute
value of the lower `y` boundary of the target area (otherwise it will overshoot the target area on
the way down).
* The maximum initial `x` velocity can be the upper `x` boundary of the target area (otherwise it
will overshoot the target area in the first step).
* The minimum initial `x` velocity can be found by solving a quadratic equation based on the fact
  that `x` velocity decreases by `1` at each step until it reaches `0`. Then the `x` position
  remains constant.

### Possible Improvements:
* There is room to further optimize the solution by finding the `y=f(x)` trajectory equation and
  solve in a more analytical way. But I preferred to keep the brute-force simulation for simplicity.

## Day 18: [Snailfish](https://adventofcode.com/2021/day/18) &rarr; [Solution](./day18/d18.py)
We are provided with a list of snailfish.\
Each snailfish is either an integer or a pair of two other snailfish.\
There are two reduction operations defined on snailfish:
* Explosion: If any pair is nested inside four pairs, the leftmost such pair explodes.
* Split: If any regular number is 10 or greater, the leftmost such regular number splits.
More details on how to explode and split can be found in the puzzle description (linked above).\
In part 1, we need to sum all the snailfish in the input list, added one by one, by pairing to a new
snailfish and then reducing it.\
In part 2, we need to find the maximum magnitude (with defined recursive formula) of the sum of any
two snailfish from the input list.

The plain representation of snailfish as nested lists makes it easy to implement the operations
recursively, and is efficient enough for this puzzle (runs in less than a second).\
The key to implement the defined operations is to divide them into multiple recursive functions.

Since there are not much of repeating patterns, caching the results of operations is not helping
much; so we can keep the representation as lists instead of converting to tuples for caching.

### Possible Improvements:
* I think we can optimize the implementation by representing the snailfish as a tree structure
instead of nested lists. But I preferred to keep the simpler representation for now.

## Day 19: [Beacon Scanner](https://adventofcode.com/2021/day/19) &rarr; [Solution](./day19/d19.py)
We are provided with a list of 3D scanners, each with a list of detected beacons in 3D space.\
What we know is:
* Each scanner has its own coordinate system (unknown position and orientation).
* Scanners can overlap, if they do, they will have at least 12 beacons in common, but with different
coordinates.
* If we call two overlapping scanners as connected, all scanners will form a connected graph.

What we need to do, is to find the 3D position of all the scanners and their detected beacons in a
common coordinate system (e.g. in scanner 0's coordinate system).

In part 1, we need to find the total number of unique beacons.\
In part 2, we need to find the maximum Manhattan distance between any two scanners.

**The key idea to solve this puzzle is to find the 3D distances between all pairs of beacons for
each scanner.\
Then, for each pair of scanners, we can find the beacons that have at least 11 distances in
common.**

The number 12 (for overlapping beacons) gives us a clue: finding the 3D to 3D transformation is
possible with 12 pairs of points (beacons), because the transformation has 12 degrees of freedom
(3 for rotation, 3 for translation, and 6 for the choice of which axes map to which), which can be
represented with a 4x3 matrix.

I implemented a function in my `myutils.optimization` library named
`find_Nd_to_Nd_transformation` that finds the transformation matrix between two sets of N-D points,
which uses the least-squares solution to a linear matrix equation: `numpy.linalg.lstsq`.


## Day 20: [Trench Map](https://adventofcode.com/2021/day/20) &rarr; [Solution](./day20/d20.py)
A cellular automaton puzzle on an infinite 2D grid.\
We are provided with an enhancement algorithm (a string of 512 characters) and an initial image.\
At each step, we need to find the binary value from the 9-neighborhood of each pixel, and then look
up the corresponding value in the enhancement algorithm to get the new pixel value.\
In part 1, we need to run this for 2 steps, and in part 2 for 50 steps.

The key challenge in this puzzle is to handle the infinite grid for the puzzle input, for which the
first value in the algorithm is `#` (on) and the last value is `.` (off), unlike the sample input.\
This means that the infinite background will flip between `.` and `#` at each step.

To handle this, we can keep track of the current background value and update it at each step based
on the enhancement algorithm.\
Also, setting the borders of the current image at each step needs to be done carefully, bacuase the
image expands by one pixel in each direction at each step.

## Day 21: [Dirac Dice](https://adventofcode.com/2021/day/21) &rarr; [Solution](./day21/d21.py)
A puzzle of turn-based dice rolling game!\
We have two pawns on a circular board of 10 positions (1-10), and the initial positions of the
pawns are given in the input.\
Each player rolls a dice three times and moves their pawn forward by the sum of the rolls.

In part 1, the die is a 100-sided deterministic one i.e. it rolls 1,2,3,... \
and each pawn rolls three times and moves forward by the sum of the rolls, and adds the new position
to their score.\
The game ends when one of the players reaches a score of at least 1000.\
Implementing the simulation of this game is straightforward and efficient enough.

But in part 2, the die is a quantum die that splits the universe into 3 new universes for each roll
(with outcomes 1, 2, and 3).\
The game goes on similarly, but the end game criteria is now 21 (or more) points.\
And we need to find the number of universes where each player wins, and return the maximum of the
two.\
The brute-force simulation of all possible universes is not tractable here anymore!

### Optimizations:
* The "number of universes" gives us a clue, that Dynamic Programming can be used here.
* We can model each step of the game as a state consisting of:
  * positions of both players
  * scores of both players
  * whose turn it is, and
  * how many universes are in this state.
* Then, we can use a queue to process each state, and for each state, we can generate all the
  possible next states based on the possible outcomes of the x3 quantum die rolls (3, 4, ..., 9).
* One extra trick that improves the run-time in more than two orders of magnitude, is to keep the
  counts of scenarios out of the state itself, so that we can aggregate the counts for the same
  state together along the way!
  * I used a `counter` dictionary for this purpose.

## Day 22: [Reactor Reboot](https://adventofcode.com/2021/day/22) &rarr; [Solution](./day22/d22.py)
A puzzle of handling 3D ranges (cuboids) and their unions and intersections.\
We are provided with a list of commands to turn on or off cuboids in 3D space.\
And find the final number of "on" cubes after executing all the commands.\
In part 1, we only consider the cubes within the initialization region (`x,y,z` in `[-50, 50]`), and in part 2 we consider all cubes.\
The brute-force simulation of all cubes is tractable for part 1, but not for part 2, since the 3D ranges are very large.

### Optimizations:
* First of all, coordinate compression is needed to reduce the size of the 3D space.
* We cannot solve the whole part 2 problem in one step of coordinate compression, due to the computational complexity.
  * So we need further simplifications of the problem.
  * From top to bottom, we can process the "on" commands only, and for each command, we can find the overlapping cuboids on all the upcoming steps, and subtract them from the current
    region. The volume of the remaining cuboids can be added to the total "on" cubes.
  * To handle the subtraction of overlapping cuboids, I added a voxel3d class to my utility libraries.

## Day 23: [Amphipod](https://adventofcode.com/2021/day/23) &rarr; [Solution](./day23/d23.py)
## Day 24: [Arithmetic Logic Unit](https://adventofcode.com/2021/day/24) &rarr; [Solution](./day24/d24.py)
## Day 25: [Sea Cucumber](https://adventofcode.com/2021/day/25) &rarr; [Solution](./day25/d25.py)
