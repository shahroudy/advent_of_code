# Advent of Code 2022
## Day 1: [Calorie Counting](https://adventofcode.com/2022/day/1)
Warming up on:
* loading input files (group of integer lines)
* summing them up
* sorting lists
### Bugs and issues:
* sorted(values) returns a sorted copy of the input list (ascending order)
* sort(values) sorts the input list (ascending order)
* sort(values, **reverse=True**) sorts the input list in descending order

## Day 2: [Rock Paper Scissors](https://adventofcode.com/2022/day/2)
The only challenge was to read and understand the problem!
### Optimizations:
* using **ord** function

## Day 3: [Rucksack Reorganization](https://adventofcode.com/2022/day/3)
A perfect puzzle to be solved by sets.
### Optimizations:
* using sets and their intersections
* using `set.intersection` on an unpacked set of elements:

  ```python
   set.intersection(*(set(rucksack) for rucksack in rucksacks))
  ```

## Day 4: [Camp Cleanup](https://adventofcode.com/2022/day/4)
For a quick result, I used **set**s (ranges casted to sets) and set operations:
* **<=** and **>=** operations on sets for subset and superset
* **&** operation on sets for intersection (and cast it to bool).

This can be a good idea for first few days, such solutions will not be efficient for tricky inputs,
which are quite common in later days.
### Optimizations:
* Comparing upper and lower bounds of the ranges will efficiently do the job here but needs a bit
  of thinking :blush::

    ```python
    def sub_super_set_count(self):
        return sum([c >= a and d <= b or a >= c and b <= d for a, b, c, d in self.ranges])
    def overlapping_count(self):
        return sum([not (c < a and d < a or c > b and d > b) for a, b, c, d in self.ranges])
    ```
## Day 5: [Supply Stacks](https://adventofcode.com/2022/day/5)
The problem statement was easy to clear: implement some stack functionality.<br>
For this we have **list** with **append** and **pop**.<br>
The only challenge here was to program the input reading for the current stack status.<br>
In my initial try, **I skipped this and copied the stacks to my editor and used them
hard-coded**.<br>

### Bugs and issues:
* **Stripping the input lines** by default is a recurring issues I face.<br>
  I need to be very careful about it for problems like this.
### Optimizations:
* My solution for the second part (obviously) was to use a temporary stack to push to and pop from,
  in order to keep the order of the items.

## Day 6: [Tuning Trouble](https://adventofcode.com/2022/day/6)
Another puzzle which solves easily using sets.<br>
The only challenge here was to read and understand the problem quickly :smile:

## Day 7: [No Space Left On Device](https://adventofcode.com/2022/day/7)
It took me a while to decide on the data structure I want to use to store the data.
Eventually I decided to represent each file/directory as a tuple of subdir names and keep their
sizes in a `defaultdict` of `int`.<br>
I also used another `defaultdict` of `list` to keep track of subdirectories of each directory.
### Bugs and issues:
* Forgot one of the mentioned line templates!

## Day 8: [Treetop Tree House](https://adventofcode.com/2022/day/8)
For part A, I scanned from each direction once and counted the visible ones,
instead of checking every tree!
## Day 9: [Rope Bridge](https://adventofcode.com/2022/day/9)
The only twist in this problem was to clearly understand when and how a trailing knot moves.
## Day 10: [Cathode Ray Tube](https://adventofcode.com/2022/day/10)
Once again a puzzle with hard-to-understand problem statement :smile:.

## Day 11: [Monkey In The Middle](https://adventofcode.com/2022/day/11)
It was an easy to solve puzzle, if you know how to cope with the big numbers in part B.
### Optimizations:
* Using eval function was an advantage here.
* To prevent the numbers to grow out of control, we have to use the remainders of the numbers to the
  least-common-multiplier of the divisors.
* Using `math.lcm` function to calculate least-common-multiplier of inputs.
## Day 12: [Hill Climbing Algorithm](https://adventofcode.com/2022/day/12)
A typical puzzle to be solved by BFS.

## Day 13: [Distress Signal](https://adventofcode.com/2022/day/13)
A recursive approach of comparing the two sides did the job.
### Bugs and issues:
* At first I mistakenly compared the plain lists together and took me a while to find the proper
  solution.
* The corner cases of:
  * equal size sides
  * smaller size left
  * smaller size right
### Optimizations:
* Using `functools.cmp_to_key` to use a lambda function as comparison operation for sorting:

  ```python
  from functools import cmp_to_key
  q.sort(key=cmp_to_key(self.compare))
  ```

## Day 14: [Regolith Reservoir](https://adventofcode.com/2022/day/14)
Reading the input and formulating the solution was challenging here.

## Day 15: [Beacon Exclusion Zone](https://adventofcode.com/2022/day/15)
Once nice and fun to solve puzzle today (part B).
### Optimizations:
* Brute-force search fails awfully for part B.
  Proper understanding of the problem gives you the clue.
  There is only one undetected point, so it must be located on the border of one (or more) beacons.
  This limits the search space drastically!
## Day 16: [??](https://adventofcode.com/2022/day/16)
### Bugs and issues:
### Optimizations:

## Day 17: [Pyroclastic Flow](https://adventofcode.com/2022/day/17)
The first challenge in this puzzle was to implement the mechanics of the Tetris-like game.
Second was to find a trick to avoid another brute-force search/simulation of the game.
### Optimizations:
* Finding the repeating patterns after a number of iterations and fast-forwarding accordingly.

## Day 18: [Boiling Boulders](https://adventofcode.com/2022/day/18)
It was mainly about how to solve the puzzle quickly
For part B, I calculated the outer 3D region first and solved the puzzle based on that.
### Optimizations:
* Using `functools.cache` for repeatedly called functions.

## Day 19: [??](https://adventofcode.com/2022/day/19)
### Bugs and issues:
### Optimizations:

## Day 20: [Grove Positioning System](https://adventofcode.com/2022/day/20)
My initial solution was actually the working one.<br>
Using double hash tables to keep the positions of values and values in each position.
### Bugs and issues:
* Finding the proper new position after a deletion was a challenge.
  It was a bit challenging to figure our the length of the list is now one item shorter! :)

  ```python
  new_pos = 1 + (old_pos - 1 + int(i)) % (code_len - 1)
  ```
* Handling of repetitive items was the second challenge. I added small float fractions to make them
  distinct! Then handling of positive vs. negative numbers were supposed to be different:

  ```python
  while num in seen_numbers:
      if num < 0:
          num -= 0.001
      else:
          num += 0.001
  ```

## Day 21: [Monkey Math](https://adventofcode.com/2022/day/21)
This puzzle made me explore and revisit how to use `sympy` package in Python.<br>
Using it together with `exec` command, my solution ended up very succinct.

## Day 22: [Monkey Map](https://adventofcode.com/2022/day/22)
The first part of the puzzle was an easy one,
but the second needed a while to think on how to solve!<br>
My final solution has hard-coded implementation of the folding for my input,
I assume the shape of the input was the same for everyone, so it must work for all other inputs :)
```
. . . . . 1 K 1 L 1 2 M 2 N 2
. . . . . I 1 1 1 1 2 2 2 2 D
. . . . . 1 1 1 1 1 2 2 2 2 2
. . . . . J 1 1 1 1 2 2 2 2 C
. . . . . 1 1 1 1 1 2 A 2 B 2
. . . . . H 3 3 3 3 . . . . .
. . . . . 3 3 3 3 A . . . . .
. . . . . 3 3 3 3 3 . . . . .
. . . . . G 3 3 3 B . . . . .
. . . . . 3 3 3 3 3 . . . . .
4 H 4 G 4 5 5 5 5 5 . . . . .
J 4 4 4 4 5 5 5 5 C . . . . .
4 4 4 4 4 5 5 5 5 5 . . . . .
I 4 4 4 4 5 5 5 5 D . . . . .
4 4 4 4 4 5 F 5 E 5 . . . . .
6 6 6 6 F . . . . . . . . . .
K 6 6 6 6 . . . . . . . . . .
6 6 6 6 6 . . . . . . . . . .
L 6 6 6 E . . . . . . . . . .
6 M 6 N 6 . . . . . . . . . .
```
### Bugs and issues:
* First, in reading the moves line, I was saving the numbers when I read a letter (R/L); which works
  for the sample input but not for the puzzle input! It ends with a number.
* In my implementation of moves, I forgot to handle the directions similar to the locations, and
  only save them when we are not hitting a wall after wrapping! <br>This was something which was showing
  up in the part B of the puzzle since in part A direction was not changing after wrapping.
### Optimizations:
* I made a bad decision to implement part B wrapping in 3D!
  It sounded like a good idea at first, but implementation of rotations in the 3D space was a nightmare!
  It worked at the end of the day, but took me hours to get the right answer.
  I reimplemented it in 2D which let to a way shorter and easier to read code!

## Day 23: [Unstable Diffusion](https://adventofcode.com/2022/day/23)
Once again a puzzle with a number of rules to be implemented.<br>
The main challenge was to ensure you've implemented all the rules in the proper order
### Optimizations:
* Using `set`s for elves' locations.
* Using `collections.Counter` for finding unique destinations.


## Day 24: [Blizzard Basin](https://adventofcode.com/2022/day/24)
This problem was a perfect fit to be solved by an **A<sup>*</sup> algorithm**.<p>
Using a min-heap and keeping a list of states for each cost function value did the job.
### Bugs and issues:
* Once again I forgot to **eliminate the duplicate nodes** in the graph, which led to a huge set of
repetitive states and making the program running out of memory!
* The **empty newline** at the end of the input file (which was not there in my copied sample) led to a wrong map height value.
### Optimizations:
* Caching the blizzards' state for each iteration.
* Caching the open ground locations for each iteration and using them to find valid child nodes
instead of blizzards locations/states.

## Day 25: [Full Of Hot Air](https://adventofcode.com/2022/day/25)
A problem of changing numbers to a base 5 with positive and negative digits!
* 1&harr;1
* 2&harr;2
* 3&harr;1=
* 4&harr;1-
* 5&harr;10

### Bugs and issues:
* My initial solution was to build a pair of dictionaries to convert int to SNAFU and vice versa,
which apparently was not efficient due to long numbers in the input file.
It took me a while to figure out how to get the SNAFU representation of the total number.
I got the idea for the solution when I started to do it manually :sweat_smile:
### Optimizations:
* Start from the highest possible rank and find the best digit (with minim absolute remainder),
and proceed with lower ranks.