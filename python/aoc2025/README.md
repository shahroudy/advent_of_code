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
