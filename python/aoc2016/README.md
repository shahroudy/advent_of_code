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

## Day 19: [An Elephant Named Joseph](https://adventofcode.com/2016/day/19) &rarr; [Solution](./day19/d19.py)
This was the most challenging puzzle so far in AoC 2016.\
You have a circle of numbered elves, starting from number 1, they eliminate the immediate next elf.\
We want to find the last elf remaining.\
The first part can be efficiently simulated using a linked-list-like structure, keeping track of who's next to each remaining elf.\
But in the second part, each elf eliminates the elf in front of him/her in the circle.
This requires a more sophisticated solution, since there is not an efficient way to simulate the process for a large number of elves.\
**So, I had to use the non-efficient implementation for the second part (order of n<sup>2</sup>), find the pattern of the answers, and model the pattern instead**:

1 -> 1

2 -> 1\
3 -> 3

4 -> 1\
5 -> 2\
6 -> 3\
7 -> 5\
8 -> 7\
9 -> 9

10 -> 1\
11 -> 2\
12 -> 3\
13 -> 4\
14 -> 5\
15 -> 6\
16 -> 7\
17 -> 8\
18 -> 9\
19 -> 11\
20 -> 13\
21 -> 15\
22 -> 17\
23 -> 19\
24 -> 21\
25 -> 23\
26 -> 25\
27 -> 27

28 -> 1\
29 -> 2\
30 -> 3\
31 -> 4\
32 -> 5\
33 -> 6\
34 -> 7\
35 -> 8\
36 -> 9\
37 -> 10\
38 -> 11\
39 -> 12\
40 -> 13\
41 -> 14\
42 -> 15\
43 -> 16\
44 -> 17\
45 -> 18\
46 -> 19\
47 -> 20\
48 -> 21\
49 -> 22\
50 -> 23\
51 -> 24\
52 -> 25\
53 -> 26\
54 -> 27\
55 -> 29\
56 -> 31\
57 -> 33\
58 -> 35\
59 -> 37\
60 -> 39\
61 -> 41\
62 -> 43\
63 -> 45\
64 -> 47\
65 -> 49\
66 -> 51\
67 -> 53\
68 -> 55\
69 -> 57\
70 -> 59\
71 -> 61\
72 -> 63\
73 -> 65\
74 -> 67\
75 -> 69\
76 -> 71\
77 -> 73\
78 -> 75\
79 -> 77\
80 -> 79\
81 -> 81

82 -> 1\
83 -> 2\
84 -> 3\
85 -> 4\
86 -> 5\
87 -> 6\
88 -> 7\
89 -> 8\
90 -> 9\
91 -> 10\
92 -> 11\
93 -> 12\
94 -> 13\
95 -> 14\
96 -> 15\
97 -> 16\
98 -> 17\
99 -> 18\
100 -> 19

Looks like the pattern is:

```python
def who_wins_grab_from_front(self):
    winner = 1
    for i in range(2, self.elf_count + 1):
        if winner == i - 1:
            winner = 1
        elif winner >= i // 2:
            winner += 2
        else:
            winner += 1
    return winner
```

This solution is of a linear order can solve the puzzle for a large number of elves in a fraction of a second.

## Day 20: [Firewall Rules](https://adventofcode.com/2016/day/20) &rarr; [Solution](./day20/d20.py)
A range-handling puzzle.\
We have a list of invalid ranges of numbers and we need to find the smallest valid number.\
Obviously since it's about very very long ranges, looping over indices will not be tractable.\
So the solution here is to to find the range that invalidates the current number and jump to its end; and repeat this until we find a valid IP.\
In the second part, we need to find the number of all valid numbers.\
To do so, we can continue with the same approach, and every time we find a valid number, we can find the next invalid range, and count the numbers in between.\
Inspired by this puzzle, I implemented a `ExRange` class to handle the multi-ranges and the operations on them.

## Day 21: [Scrambled Letters and Hash](https://adventofcode.com/2016/day/21) &rarr; [Solution](./day21/d21.py)
A puzzle to scramble and unscramble passwords based on a set of modification rules.\
The rules are string operations: swap, rotate, reverse, move, and rotate based on the position of a character.\
For faster implementation, I converted the string to a list of characters and applied the rules on the list.\
For the second part, we need to find the reverse operation of the scramble rules.\
Due to the nature of the rules, the reverse operation of each rule is not so straightforward, so we need another way: brute force search, which was tractable thanks to the efficient implementation of the scramble operations.

## Day 22: [Grid Computing](https://adventofcode.com/2016/day/22) &rarr; [Solution](./day22/d22.py)
Another nice puzzle that needs some thinking to solve.\
We are given a grid of nodes, each node has a volume size and usage in TeraBytes.\
In part 1, we need to find the number of viable pairs of nodes, defined by 3 simple rules, doable in one line of code :smile:\
In part 2, we need to find the minimum number of steps to move the data from the top-right node to the top-left node, moving the data through the only empty node in the grid.\
This reminds me of a jig-saw puzzle, where we need to move the empty piece to the right place to move the other pieces.\
In my first implementation, I kept all the usage values of the nodes in the search state, which made the memory usage out of control.\
***In AoC this is a hint that there is a possible relaxation of the problem to make it more tractable.\
Similar to the example provided in the statement of the puzzle, we can limit the usable nodes to the ones that have data fittable in the empty node.\
This point was actually hinted in part 1 as well :smile:***\
This way, you do not need to keep the usage values of the nodes in the search state, and you can use a simple BFS algorithm to find the minimum number of steps in about a second.

## Day 23: [Safe Cracking](https://adventofcode.com/2016/day/23) &rarr; [Solution](./day23/d23.py)
An assembly (assmebunny) code translation puzzle.\
We have a new instruction in the assembly code, `tgl`, which toggles the instruction at the given offset, which makes the emulation very slow for larger input values (inital `a-register` values).\
I let it run for 6-7 minutes for part 2, and it gave the correct answer.\
Apparently one can analyze and translate the input assembly code.\
I managed to do so, finding out the answer (for `egg counts >= 7`) is `n! + X * Y` where:
* `n` is the initial value of the `a-register` a.k.a egg count, 
* `X` and `Y` are the values of the constants used as the first arguments in the input command lines 20 and 21 respectively.

## Day 24: [Air Duct Spelunking](https://adventofcode.com/2016/day/24) &rarr; [Solution](./day24/d24.py)
A map based search puzzle.\
We need to find the shortest path that visits all the numbers in the map.\
The only challenge here was to formulate the problem as a graph search problem.\
The rest was a simple BFS algorithm to find the shortest path.\
In the second part, we need to find the shortest path that visits all the numbers and returns to the starting point.\
Which had more-or-less the same challenge; how to formulate!\
What I did was to keep the sorted list of the visited numbers in the search state, and find the shortest path that visits all the numbers in the list.\
In part 2, we need an extra twist, ignore the start point (#0) before visiting all the rest of the numbers.
