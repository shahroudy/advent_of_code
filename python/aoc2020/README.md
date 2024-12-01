# Advent of Code 2020

## Day 1: [Report Repair](https://adventofcode.com/2020/day/1) &rarr; [Solution](./day01/d01.py)
We are provided with a set of numbers and need to find the two (three in part 2) numbers that sum up to 2020 and return their product.
Adhoc looping works here, but a better approach is to use a set to store the numbers and check if the difference is in the set.
It will be of O(n) and O(n^2) complexity respectively.
Warm up on:
* `set`

## Day 2: [Password Philosophy](https://adventofcode.com/2020/day/2) &rarr; [Solution](./day02/d02.py)
Simple string validation problem.\
In each line we are provided with two numbers, a character and a password, and we need to count valid passwords.\
In part 1, a password is valid if the occurence of the character is within the given range.\
In part 2, a password is valid if the character is present at exactly one of the given positions.\
`re` was a good fit to parse the input lines.\
Warm up on:
* `re`
* `str`
* `^` a.k.a. `xor` operator

## Day 3: [Toboggan Trajectory](https://adventofcode.com/2020/day/3) &rarr; [Solution](./day03/d03.py)
We are provided with a grid of trees and need to count the number of trees encountered while traversing the grid with a given slope.\
The grid is repeated infinitely in the horizontal direction.\
No special trick is needed here, just a simple modulo operation to wrap around the grid in horizontal axis.\
Warm up on:
* `%` a.k.a. `modulo` operator
* reading maps of characters from input files