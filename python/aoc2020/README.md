# Advent of Code 2020

## Day 1: [Report Repair](https://adventofcode.com/2020/day/1) &rarr; [Solution](./day01/d01.py)
We are provided with a set of numbers and need to find the two (three in part 2) numbers that sum up to 2020 and return their product.
Adhoc looping works here, but a better approach is to use a set to store the numbers and check if the difference is in the set.
It will be of O(n) and O(n^2) complexity respectively.
