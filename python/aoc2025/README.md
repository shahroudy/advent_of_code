# Advent of Code 2025

## Day 1: [Secret Entrance](https://adventofcode.com/2025/day/1) &rarr; [Solution](./day01/d01.py)
We are provided with a set of instructions to increase/decrease the value of a dial (starting at 50)
each line starts with either a "L" to decrease or "R" to increase followed by a number of steps.\
The values are wrapped around between and including 0 and 99.\
In part 1, we need to count the number of times we end up at value `0` after each step.\
In part 2, we need to find all the times we pass or end up at value `0`.\
Both parts can be solved in a brute-force manner by simulating each step one by one.
