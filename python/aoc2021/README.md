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
In part 2, `up` and `down` only move an "aim" value, and `forward` moves based on the value horizontally, and based on the value multiplied by the "aim" vertically.\
In both parts, we need to calculate the `x*y` of the final position.\
Use of the internal library classes of `Point2D` and `Point3D` helped here.\
In part 2, we can use the `Point3D` class to keep track of the position and the aim.

## Day 3: [Binary Diagnostic](https://adventofcode.com/2021/day/3) &rarr; [Solution](./day03/d03.py)
We are provided with a list of binary numbers.\
In part 1 we need to find the number consisting of most common bits at each position, multiplied by the number consisting of least common bits.\
In part 2, we need to iteratively find the most common bit and filter the list and only keep the numbers that have that bit at that position.\
We iterate until we have only one number left, and that would be the result.\
In the case of equal counts, `1` is picked.\
Similarly we find the result for least common bit (picking `0` on equal counts).\
And then multiply these two together to get the final answer.

One can use the `Counter` class from the `collections` module to find the most and least common bits.\
I preferred to implement the logic myself, mainly using `str` values directly.

### Optimizations:
* In part 1, the least common bits are actually the complement of the most common bits, so we don't need to calculate them separately.

## Day 4: [Giant Squid](https://adventofcode.com/2021/day/4) &rarr; [Solution](./day04/d04.py)
Simulating a game of Bingo!.\
We are provided with a list of integers, and a set of 2D boards of numbers.\
The input numbers will be read in order, and we need to find the first winning board.\
A winning board is a board where all the numbers in a row or a column are already read.\
We need to find the first and last winning boards.\
This puzzle is mainly a warm-up on handing 2D arrays and lists.

## Day 5: [Hydrothermal Venture](https://adventofcode.com/2021/day/5) &rarr; [Solution](./day05/d05.py)
We are provided with the two ends of a number of line segments and need to find the number of overlap points between them.\
Lines are either horizontal, vertical, or 45-degree diagonal.\
In part 1, we only consider horizontal and vertical lines.\
In part 2, we also consider diagonal lines.

### Optimizations:
* The fact that the diagonal lines are always at 45 degrees simplifies the calculations a lot.
* Data structures needed here are two sets of point-coordinates for visited and overlapping points.

### Bugs and Issues:
* For part 2, I implemented a very general solution that can handle any angle of diagonal lines, which was not needed!

## Day 6: [Lanternfish](https://adventofcode.com/2021/day/6) &rarr; [Solution](./day06/d06.py)
We are provided with a list of numbers, representing the remaining days each lanternfish creates another one.\
Each lanternfish, at each step (say a day) gets its timer value decreased by 1.\
If the timer value is `0`, it will reset to `6` and create a new lanternfish with remaining `8` days.\
We need to find the number of lanternfish after a given number of days (`80` and `256` days in parts 1 and 2 respectively).

### Optimizations:
* We don't care about any order or individual fish, so we can simply keep track of the number of lanternfish with each timer value at each time step!

## Day 7: [The Treachery of Whales](https://adventofcode.com/2021/day/7) &rarr; [Solution](./day07/d07.py)
We have a list of integers representing the horizontal positions of crabs.\
We need to find the horizontal position that minimizes the sum of distances to all crabs.\
In part 2, each step of a move will increase the needed fuel by one.

### Optimizations:
* For part 2, we can pre-calculate the needed fuel for each distance value and store it in a list/dict.





## Day 8: [Seven Segment Search](https://adventofcode.com/2021/day/8) &rarr; [Solution](./day08/d08.py)
## Day 9: [Smoke Basin](https://adventofcode.com/2021/day/9) &rarr; [Solution](./day09/d09.py)
## Day 10: [Syntax Scoring](https://adventofcode.com/2021/day/10) &rarr; [Solution](./day10/d10.py)
## Day 11: [Dumbo Octopus](https://adventofcode.com/2021/day/11) &rarr; [Solution](./day11/d11.py)
## Day 12: [Passage Pathing](https://adventofcode.com/2021/day/12) &rarr; [Solution](./day12/d12.py)
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

