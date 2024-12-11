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

## Day 4: [Passport Processing](https://adventofcode.com/2020/day/4) &rarr; [Solution](./day04/d04.py)
A puzzle of parsing input key-value pairs and validating then against a set of rules.\
Nice one to solve using regular expressions.

### Bugs and Issues
* Forgot to use `^` and `$` in `re` to ensure the string is an exact match.\
This way I accepted longer strings that start with a matching substrings.

## Day 5: [Binary Boarding](https://adventofcode.com/2020/day/5) &rarr; [Solution](./day05/d05.py)
All you need to do here is to understand the problem statement.\
Inputs are binary-like strings and we need to convert them to decimal numbers.\
In part 1 we need to find the maximum seat ID.\
In part 2 we need to find the missing seat ID in the input range.

## Day 6: [Custom Customs](https://adventofcode.com/2020/day/6) &rarr; [Solution](./day06/d06.py)
A simple problem of counting the number of unique characters in groups of strings.\
In part 1 we need to count the number of unique characters in each group.\
In part 2 we need to count the number of characters that are present in all strings of each group.\
Very easy to solve using sets; part 1 is mainly about finding the `union` of characters in each group, and part 2 is about finding the `intersection` of them.

## Day 7: [Handy Haversacks](https://adventofcode.com/2020/day/7) &rarr; [Solution](./day07/d07.py)
We are provided with a set of rules about how many of other colored bags are included in each colored bag.\
In part 1 we need to find the number of different colored bags that can contain a "shiny gold" bag.\
In part 2 we need to find the number of bags that are included in a "shiny gold" bag.\
Recursion with memoization (`@cache`) is a good fit for this problem.

### Bugs and Issues
* reading the input lines with `re` was a bit tricky here.\
I ended up having two different regular expressions for the container and the contained bags.

## Day 8: [Handheld Halting](https://adventofcode.com/2020/day/8) &rarr; [Solution](./day08/d08.py)
An easy puzzle of simulating an assembly program with a set of instructions.\
The computer has an accumulator, an instruction pointer, and a set of instructions.\
In part 1 we need to find the value of the accumulator before the program enters an infinite loop.\
In part 2 we need to find the value of the accumulator after fixing the program by changing one `nop` to `jmp` or vice versa.