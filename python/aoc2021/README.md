# Advent of Code 2021

## Day 1: [Sonar Sweep](https://adventofcode.com/2021/day/1)
We are provided with a list of integers (as depth levels) and we need to find:
* Part 1: How many times we have an increase in depth level.
* Part 2: How many times we have an increase in the sum of 3 consecutive depth levels.

### Optimizations:
* In part 2, one can simply find the number of times `depths[i+3] > depths[i]`.
