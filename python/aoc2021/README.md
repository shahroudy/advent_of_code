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
## Day 14: [Extended Polymerization](https://adventofcode.com/2021/day/14) &rarr; [Solution](./day14/d14.py)
## Day 15: [Chiton](https://adventofcode.com/2021/day/15) &rarr; [Solution](./day15/d15.py)
## Day 16: [Packet Decoder](https://adventofcode.com/2021/day/16) &rarr; [Solution](./day16/d16.py)
## Day 17: [Trick Shot](https://adventofcode.com/2021/day/17) &rarr; [Solution](./day17/d17.py)
## Day 18: [Snailfish](https://adventofcode.com/2021/day/18) &rarr; [Solution](./day18/d18.py)
## Day 19: [Beacon Scanner](https://adventofcode.com/2021/day/19) &rarr; [Solution](./day19/d19.py)
## Day 20: [Trench Map](https://adventofcode.com/2021/day/20) &rarr; [Solution](./day20/d20.py)
## Day 21: [Dirac Dice](https://adventofcode.com/2021/day/21) &rarr; [Solution](./day21/d21.py)
## Day 22: [Reactor Reboot](https://adventofcode.com/2021/day/22) &rarr; [Solution](./day22/d22.py)
## Day 23: [Amphipod](https://adventofcode.com/2021/day/23) &rarr; [Solution](./day23/d23.py)
## Day 24: [Arithmetic Logic Unit](https://adventofcode.com/2021/day/24) &rarr; [Solution](./day24/d24.py)
## Day 25: [Sea Cucumber](https://adventofcode.com/2021/day/25) &rarr; [Solution](./day25/d25.py)
