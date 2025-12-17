# Advent of Code 2025

## Day 1: [Secret Entrance](https://adventofcode.com/2025/day/1) &rarr; [Solution](./day01/d01.py)
We are provided with a set of instructions to increase/decrease the value of a dial (starting at 50)
each line starts with either a "L" to decrease or "R" to increase followed by a number of steps.\
The values are wrapped around between and including 0 and 99.\
In part 1, we need to count the number of times we end up at value `0` after each step.\
In part 2, we need to find all the times we pass or end up at value `0`.\
Both parts can be solved in a brute-force manner by simulating each step one by one.

## Optimizations
To optimize part 2, instead of simulating each step one by one, we can:
* Find the number of steps needed to reach `0` from the current dial value in the given direction,
* If the number of steps is less than to-zero steps, we only update the dial value and continue,
* Otherwise, we count one pass to `0`, reduce the number of steps by to-zero steps, and then count
  the number of full cycles (each cycle has 100 steps) in the remaining steps.
* The only remaining tricky part is when we start at `0`, in which case we shouldn't count a pass
  at the beginning.

## Day 2: [Gift Shop](https://adventofcode.com/2025/day/2) &rarr; [Solution](./day02/d02.py)
In this puzzle, we are given a list of ranges of gift IDs available in a shop, and we need to
find all the invalid gift IDs within the given ranges, find their sum.\
An invalid gift ID is:
* In part 1: a gift ID that has an exactly two repetition of the same number, e.g. `123123`.
* In part 2: a gift ID that has any number of repetition of the same number, e.g. `121212`.

To solve this, one can iterate over all the given ranges and check if:
* The gift ID's string can be broken down into two or more equal sized parts,
* Each part is identical to the others.

### Optimizations
To optimize the solution, we can try to generate all the possible invalid IDs and check if they
fall within the given ranges, instead of checking each ID in the ranges.\
This improves the performance two orders of magnitude and leads to a simpler implementation.\
The only tricky part here will be to eliminate duplicates when generating the invalid IDs.

For this solution my utility `ExRange` class was helpful.\
It also made me optimize the `contains` method in `ExRange` to use binary search for better
performance.

## Day 3: [Lobby](https://adventofcode.com/2025/day/3) &rarr; [Solution](./day03/d03.py)
We have sequences of digits (a.k.a. banks of batteries) and we want to find the maximum possible
n-digit "joltage" number (n is 2 and 12 in parts 1 and 2 respectively) by picking n digits from
each sequence keeping their relative order.\
One can think of some ad-hoc solutions for n=2 (part 1), but for n=12 (part 2) such
solutions will not be tractable.

My solution was to pick the maximum digit considering the number of other needed digits:
* Split the sequence into two parts: the first `len(sequence)-n` digits (current) and the
  last `n` digits (upcoming),
* Move the first digit of the upcoming part to the end of the current part,
* Find the first digit as the maximum digit in the current part,
* Trim the current sequence to start just after the found digit,
* Repeat n times (technically till there is no more upcoming digits).

## Day 4: [Printing Department](https://adventofcode.com/2025/day/4) &rarr; [Solution](./day04/d04.py)
In this puzzle, we have a 2D map of points showing the location of paper rolls.\
In part 1, we need to count the number of removable rolls that have less than 4 neighboring rolls
(considering 8-neighborhood).\
In part 2, we need to iteratively remove the removable rolls and count the total number of removed
rolls.

## Optimizations
To solve this efficiently, we can represent the current state as a set of points containing rolls.\
Then, for each point in the set, we can count its neighboring points that are also in the set.\
This way we can iteratively find removable rolls and remove them from the set until no more
removable rolls are found.\
At the end, we can simply compare the size of the original set with the final set to get the
number of removed rolls.

## Day 5: [Cafetaria](https://adventofcode.com/2025/day/5) &rarr; [Solution](./day05/d05.py)
A puzzle of handling long ranges and checking membership of numbers in those ranges.\
We are provided a list of long and overlapping ranges, and a list of IDs.\

In part 1, we need to count how many IDs fall within any of the given ranges.\
This can simply be done by cross-checking each ID with all the ranges.

In part 2, we need to find the total size of the union of the given ranges.\
This part due to the sizes of the ranges provided is not doable in a brute-force manner.\
We need to merge the overlapping ranges first, and then sum up the sizes of the merged ranges.\
Good news for me here was that I had already implemented such functionality in my `ExRange` utility
class, which made the implementation very straightforward.

## Day 6: [Trash Compactor](https://adventofcode.com/2025/day/6) &rarr; [Solution](./day06/d06.py)
In this puzzle, we are provided groups of sets of numbers and a math operator (`+` or `*`).\
We need to apply each operator between all the numbers in the same column and sum up the results.\
In part 1, numbers are simply space-separated in rows.\
In part 2, numbers are written in columns (top to bottom).

For both of these, we need to use the `transpose` operation to get the columns:
* In part 1, we can first read a 2D list of numbers and then transpose it.
* In part 2, we need to first transpose the 2D array of characters in the input string and then cast
  them to a 2D list of numbers.

For both parts, my pre-implemented `transpose` utility function was very helpful.

### Bugs and Issues:
* My code editor's auto-formatting removed some trailing spaces in the input text made part 2
  harder to handle.\
  I had to disable `trimTrailingWhitespace` for plaintext files to fix this.\
  This problem made my initial implementation of part 2 kind of complicated!

## Day 7: [Laboratories](https://adventofcode.com/2025/day/7) &rarr; [Solution](./day07/d07.py)
The first Dynamic Programming puzzle of the year!\
We have a 2D map of points representing beam splitters (`^`).\
A beam of light starts to travel down from the `S` point on the top row, and each time it hits a splitter, it splits into two beams to the right and left of the splitter.\
The beams continue to travel down until they reach the bottom row.\
In part 1, we need to count the total number of times the beam splits.\
In part 2, we need to count the total number of possible paths from the start point to the bottom row.\
This is typical `dynamic programming` problem where we can process the points in the map from top
to bottom, and for each point, we can calculate:
* If a split happens here,
* The number of ways to reach this point from the starting point.

Both of these values directly depend on the values of the points in the previous row and if each
point is next to a splitter or not.

### Optimizations
* We can optimize the implementation using `sets` and `dicts` to efficiently track and update the state of the beams and splitters.
* It's easier to look at the current row values and build the next row values by implementing the
  split logic, rather than trying to calculate each value by looking at the previous row!

## Day 8: [Playground](https://adventofcode.com/2025/day/8) &rarr; [Solution](./day08/d08.py)
A Minimum Spanning Tree (MST) puzzle!\
We are provided with a list of 3D coordinates of boxes in a playground.\
And we need to connect them step by step in the order of ascending Euclidean distances of pairs.\
This is actually the Kruskal's algorithm for finding the MST of a graph.\
In part 1, we need to find the number of connected components after a given number of steps.\
In part 2, we need to find the connection which makes all boxes connected.

The only tricky point for part 1 is to count the skipped connections when two boxes are already
connected.

### Optimizations
* Using a `dict` of `set` to track connected boxes to each box made it easy to merge connected
  components.

## Day 9: [Movie Theater](https://adventofcode.com/2025/day/9) &rarr; [Solution](./day09/d09.py)
We have a list of 2D corner points, each consecutive pair of corners represent the start and end of
a vertical or horizontal line, which all together form a closed shape.\
In part 1, we need to find the maximum area of the rectangles drawn between any two corner points.
In part 2, we need to only consider rectangles that fully lie within the closed shape (including the
border).\
The ad-hoc solution for part 2 is intractable, because the distance between the 2D points are very
large; so we need a more efficient approach.

## Optimizations
The enclosed shape inside the border can be shrunk to a smaller grid.\
We can find all the cutting lines in both x and y directions, and then map the original 2D
rectangles to 1x1 cells in the new miniature grid.\
Then a flood-fill algorithm can be used to find the outer area, and any cell not reachable from
outside is considered inside the shape.\
Finally, we can check all pairs of corner points in the miniature grid to check if they are fully
inside the shape or not.

## Further Improvements
* Reading others solutions, I found that using the `Polygon` class from `shapely` library can make
  the implementation much simpler by leveraging its geometric operations to check if a rectangle is fully inside the shape or not (`Polygon.contains` method).

## Day 10: [Factory](https://adventofcode.com/2025/day/10) &rarr; [Solution](./day10/d10.py)
In this puzzle, we have a number of machines, each with:
* An expected indicator light values (list of booleans),
* A list of button combinations (list of list of booleans),
* An expected list of joltage values (list of integers).

In part 1, each press of "button combination" toggles the corresponding indicator lights, and we
need to find the minimum number of presses to reach the expected indicator light values.

In part 2, each press of "button combination" adds the corresponding joltage value to the current
joltage, and we need to find the minimum number of presses to reach the expected joltage values.

In both of the parts, the starting state is all lights off (False) and all joltage levels 0.

The out of the box solution for part 1 is to use BFS to explore all possible states of the
indicator lights until we reach the expected state, which gets to the answer very quickly.

But Part 2, though theoretically possible, cannot be solved by BFS in a reasonable time due to the
large state space.

### Optimizations
The Part 2 of this puzzle is is actually an Integer Linear Programming (ILP) problem.\
For each machine, we solve for:

$$
\begin{aligned}
	{minimize}\quad & \sum_{i=1}^{m} x_i \\
	{subject\,to}\quad & A x = b \\
& x_i \in \mathbb{Z}_{\ge 0}
\end{aligned}
$$

Where:
* $A$ is a matrix where each row represents a button combination and each column tracks how it
  affects a joltage position,
* $x$ is a vector of unknowns representing how many times each button combination is pressed,
* $b$ is the target joltage vector for the machine.
* The objective $\sum x_i$ is the total number of button presses we want to minimize.

We can use the `pulp` library to model and solve this problem efficiently.

## Day 11: [Reactor](https://adventofcode.com/2025/day/11) &rarr; [Solution](./day11/d11.py)
We have a directional graph and we need to find the number of possible paths from a start node to
an end node.\
In part 1, we simply need to count paths from `you` to `out`.\
In part 2, we need to count paths from `svr` to `out` that pass through both `dac` and `fft`.

Part 1 can be solved using variety of different search algorithms, but part 2 is not tractable for
a search algorithm.

### Optimizations
**Whenever we want to find the number of possible ways, we should think of Dynamic Programming!**\
And in Python, we can implement the "number of ways" with a function and use `cache` decorator to
easily memoize our recursive function.

In part 2, we can extend the function to consider "avoid" nodes that we should not pass through.\
Then we can call the multiple times to find ways.

First we need to find the number of paths the go: `svr->dac->fft->out` by calling the function three
times:
* From `svr` to `dac` avoiding `fft`, `out`,
* from `dac` to `fft` avoiding `svr`, `out`,
* from `fft` to `out` avoiding `svr`, `dac`,

and multiply the results together.

There is a second group of paths that go: `svr->fft->dac->out`, which can be found similarly by
calling:
* From `svr` to `fft` avoiding `dac`, `out`,
* from `fft` to `dac` avoiding `svr`, `out`,
* from `dac` to `out` avoiding `svr`, `fft`,

and multiplying the results together.

Finally, we can add the two groups of paths to get the final result.

## Day 12: [Christmas Tree Farm](https://adventofcode.com/2025/day/12) &rarr; [Solution](./day12/d12.py)
In this puzzle, we have a list of presents, each with a width and height and a 2D pattern.\
We also have a list of regions, each with a width and height and a count of each type of present.\
We need to count the number of regions all the regions that can fit all the presents in them.\
Alright, it's not a problem one can solve efficiently, at least nothing I could think of.\
But, it's the last day, so there should be some trick to it!\
The trick is, unlike the provided sample, for the actual input, presents can always fit if the sum
of their areas is less than or equal to the area of the region!\
So the solution simplifies to a simple math problem :sweet_smile:.
