# Advent of Code 2025

## Day 1: [Secret Entrance](https://adventofcode.com/2025/day/1) &rarr; [Solution](./day01/d01.py)
We are provided with a set of instructions to increase/decrease the value of a dial (starting at 50)
each line starts with either a "L" to decrease or "R" to increase followed by a number of steps.\
The values are wrapped around between and including 0 and 99.\
In part 1, we need to count the number of times we end up at value `0` after each step.\
In part 2, we need to find all the times we pass or end up at value `0`.\
Both parts can be solved in a brute-force manner by simulating each step one by one.

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
The only tricky part here will be to eliminate duplicates when generating the invalid IDs.\
For this solution my utility `ExRange` class was helpful.

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
