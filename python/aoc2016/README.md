# Advent of Code 2016

## Day 1: [No Time for a Taxicab](https://adventofcode.com/2016/day/1) &rarr; [Solution](./day01/d01.py)
Simple rotation and moving implementation.\
Good to recall the rotation formula; 
when you rotate left: `dx, dy = dy, -dx`
and when you rotate right: `dx, dy = -dy, dx`
### Bugs and issues:
* The only tricky point in this puzzle was to consider all the positions on the way of each step in the visited positions and not only the final position (for part 2)

## Day 2: [Bathroom Security](https://adventofcode.com/2016/day/2) &rarr; [Solution](./day02/d02.py)
A simple moving on the map puzzle.\
Warming up on:
* `dict`
* reading input files

## Day 3: [Squares With Three Sides](https://adventofcode.com/2016/day/3) &rarr; [Solution](./day03/d03.py)
A simple checking of triangle rule puzzle.\
In the first part I need to check the values horizontally, and in the second part I need to check the values vertically.

### Bugs and issues:
* In my first try, I sorted the vertical values in-place and ruined the original order.

## Day 4: [Security Through Obscurity](https://adventofcode.com/2016/day/4) &rarr; [Solution](./day04/d04.py)
A simple puzzle of counting and shifting the characters in strings.
* `collections.Counter` to count the characters in the string.
* `ord()` and `chr()` to shift the characters.

## Day 5: [How About a Nice Game of Chess?](https://adventofcode.com/2016/day/5) &rarr; [Solution](./day05/d05.py)
MD5 hash mining.\
It's very similar to AoC 2015 Day 4.\
Nothing fun in looping over hash values.

## Day 6: [Signals and Noise](https://adventofcode.com/2016/day/6) &rarr; [Solution](./day06/d06.py)
Finding the most common and least common characters at each position in a list of strings.\
* `collections.Counter` to count the characters in each position.
* [`Counter.most_common()`](https://docs.python.org/3/library/collections.html#collections.Counter.most_common) to get the sorted tuples of characters and their counts.

## Day 7: [Internet Protocol Version 7](https://adventofcode.com/2016/day/7) &rarr; [Solution](./day07/d07.py)
Playing with patterns like `ABBA` and `ABA` in strings.\
This was a fun puzzle to solve with `re` (regular expressions) library tools.

Specifically, to find the `ABBA`s, I used:
`re.search(r"(?=(\w)(?!\1)(\w)\2\1)", s)`.
* `(?=...)` is a positive lookahead assertion, which matches the pattern but doesn't consume the string; which is needed to catch all the overlapping patterns.
* `(?!\1)` is a negative lookahead assertion, which matches if the next character is not the same as the first one.

And for the `ABA`s, I used:
* `re.findall(r"(?=(\w)(?!\1)(\w)\1)", s)`

## Day 8: [Two-Factor Authentication](https://adventofcode.com/2016/day/8) &rarr; [Solution](./day08/d08.py)
An easy puzzle of rotating values in a 2D grid.\
I used a dictionary to represent the grid and rotated the values in the grid by copying the values to a buffer list.

## Day 9: [Explosives in Cyberspace](https://adventofcode.com/2016/day/9) &rarr; [Solution](./day09/d09.py)
A puzzle of expanding strings based on two different versions (parts 1 and 2).\
The only mistake one can do here is to try to really expand the strings, which is not necessary.\
All we need to do is to implement a recursive function to calculate the length of the expanded strings, with two different versions.

## Day 10: [Balance Bots](https://adventofcode.com/2016/day/10) &rarr; [Solution](./day10/d10.py)
A simple cellular automaton puzzle.\
The input file provides a list of steps including:
* input single values to bots
* connection between bots (which bot/output bin receives the low/hight value from each bot)

At each step, every bot which holds two inputs (microchips) will compare its values and pass the low and high values to the connected bots or output bins.\
To solve this, I read the input lines using regular expressions and implemented the whole process using dictionaries.

## Day 11: [Radioisotope Thermoelectric Generators](https://adventofcode.com/2016/day/11) &rarr; [Solution](./day11/d11.py)
In this puzzle, we need to find the minimum number of steps to move all the items to the top floor.\
Provided items are microchips and their corresponding generators, and we can move at most two items at a time.\
The limitation we have in the moves is that we can't leave a microchip without its generator if there is another generator on the same floor.\
This looks like a suitable problem to be solved by BFS algorithm.\
But the number of possible states explodes after few iterations, so we need to prune and eliminate the redundant states.

### Optimizations:
* My first obvious optimization was to keep a history of the visited states to avoid visiting them again.\
This made the solution feasible within a few minutes.
* **The more effective optimization though was to adopt the fact that a lot of possible states are identical if we exchange the names of the microchips/generators.\
So, we can eliminate identical states with different chip/generator names.\
This change speeds up the solution more than a couple of orders in magnitude!**

## Day 12: [Leonardo's Monorail](https://adventofcode.com/2016/day/12) &rarr; [Solution](./day12/d12.py)
A simple assembly (assembunny) simulation puzzle.\
There is only four possible instructions and emulating it for the input file runs in a few seconds.\
Therefore, no need for further optimization, though the input program seems easy to be analyyzed and simplified.

## Day 13: [A Maze of Twisty Little Cubicles](https://adventofcode.com/2016/day/13) &rarr; [Solution](./day13/d13.py)
A simple maze exploration puzzle.\
A simple BFS algorithm can solve this puzzle.

### Optimizations:
* Keep track of the visited positions to avoid visiting them again.
* `@cache` the function which calculates if the neighbor position is a wall or not.
* Use A* algorithm instead of BFS to find the shortest path (not necessarily faster for this puzzle).

## Day 14: [One-Time Pad](https://adventofcode.com/2016/day/14) &rarr; [Solution](./day14/d14.py)
Interesting puzzle of finding the 64th key which passes two criteria in a list of hashes:\
* It contains three of the same character in a row, like 777. Only consider the first such triplet in a hash.
* One of the next 1000 hashes in the stream contains that same character five times in a row, like 77777.

To solve this, I used a `deque` to keep track of the indices that meet the first criteria, and a `dictionary` of `deque`s to keep track of the indices that meet the second criteria.\
Processing indices in batches of thousands and checking the second criteria for each index in the queue of the indices which passed the first.

### Optimizations:
* Using `multiprocessing.Pool` to parallelize the processing of the indices.

## Day 15: [Timing is Everything](https://adventofcode.com/2016/day/15) &rarr; [Solution](./day15/d15.py)
A capsule is dropping from the top and it should pass through the slots in the discs to reach the bottom.\
Each disc has one slot, at position zero, and the discs have different number of positions and are in different starting positions.\
The capsule meets the fist disc at start time + 1, the second at start time + 2, and so on.\
We need to find the minimum start time that the capsule can pass through all the discs.\
Analytically, for each disc we have: `i`: index of the disc, `n`: number of positions, `p`: starting position.\
And we need to find the minimum `t` such that `(p + i + t) % n == 0` for all discs.\
The ad-hoc looping over the possible start times can solve this puzzle in a fraction of a second.

### Optimizations:
We can improve the run time by a better algorithm.\
First we can sort the discs based on their number of positions, in descending order.\
Setting `t` as `0`, and the `step` as `1`, we can loop over the discs and increase the `t` by `step` until the capsule passes through the disc.\
Then we can update the `step` by the LCM of the previous step and the number of positions of the current disc.\
This improves the run time by orders of magnitude.

## Day 16: [Dragon Checksum](https://adventofcode.com/2016/day/16) &rarr; [Solution](./day16/d16.py)
A simple puzzle of generating a dragon curve and calculating the checksum.\
The main challenge here was to read and understand the problem statement; implementation was straightforward.

## Day 17: [Two Steps Forward](https://adventofcode.com/2016/day/17) &rarr; [Solution](./day17/d17.py)
A simple path search puzzle in a 4x4 grid.\
Passages between rooms are open based on some criteria on corrsponding digit in the MD5 hash of the currently traveled path.\
I used a BFS algorithm to find the shortest path to the target room.\
In part 2, we need to find the longest path to the target room, which can be done by completing the BFS for all possible paths.

## Day 18: [Like a Rogue](https://adventofcode.com/2016/day/18) &rarr; [Solution](./day18/d18.py)
A simple puzzle of generating the pattern of each row based on the previous row.\
The simple implementation of the rules can solve this puzzle in a few seconds.\
I tried to optimize the solution by keeping a history of the generated rows, but it didn't improve the run time at all.\
Apparently there was no repetitive pattern in the generated rows in the required number of rows.