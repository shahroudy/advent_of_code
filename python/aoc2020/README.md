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

## Day 9: [Encoding Error](https://adventofcode.com/2020/day/9) &rarr; [Solution](./day09/d09.py)
In this puzzle we are provided with a list of numbers and need to find the first number that is not the sum of any two of the previous 25 numbers.\
In part 2, we need to find a contiguous set of numbers that sum up to the number found in part 1.\
A simple sliding window algorithm is enough and tractable to solve this problem with the provided input.

### Optimizations
* We can improve the runtime of part 2 in orders of magnitude by building an integral sum array and use it to find the summation between each pair of numbers in O(1) time.
* We can further improve the runtime by indexing the integral sum values to indices and find the end-of-range index for each start-of-range index in O(1) time.

## Day 10: [Adapter Array](https://adventofcode.com/2020/day/10) &rarr; [Solution](./day10/d10.py)
We are provided with a list of numbers (adapters with different joltages) and need to find way to use them to connect a `0-jolt` outlet to a device with a joltage of `3` higher than the maximum adapter.\
Each connection can have at most 3 jolts difference.\
In part 1, we need to find the `1-jolt` and `3-jolt` differences and return their product.\
Which is easily doable by sorting the input list and counting the differences.\
In part 2, we need to find all the possible ways to connect the `0-jolt` outlet to the device (with maximum 3 jolts difference) in an efficient way (as stated in the problem statement, there will be trillions of ways!).\
The obvious way to solve this is **dynamic programming**.\
Across the sorted list of adapters, we can find the number of ways to connect each adapter to the outlet by summing the number of ways to achieve last 3 joltages!

## Day 11: [Seating System](https://adventofcode.com/2020/day/11) &rarr; [Solution](./day11/d11.py)
A cellular-automata-like problem.\
We are provided with a grid of seats and need to simulate the seating system and find its stable state.\
Each table's state depends on its current state and the state of its neighbors.\
In part 1, the neighbors are the 8 adjacent seats.\
In part 2, the neighbors are the first visible seat in each of the 8 directions (skipping the empty floor `.` tiles ).

### Optimizations
* The key to optimize here is the fact that neighbors are not actually moving, so for each seat the neighbors are the same across the simulation.\
The only changing factor will be their state.\
This way for both parts we can precompute the neighbors of each seat and use them in the simulation.

### Bugs and Issues
* I used a function in my library that was checking if a point is inside the grid or not.\
I passed the `rows` and `cols` in a wrong order to the function and it took me a while to figure out the bug.\
To prevent this, I updated the function to take the `self` object and access its `.cols` and `.rows` attributes directly!
* Once again, avoid single character variable names :sweat_smile:

## Day 12: [Rain Risk](https://adventofcode.com/2020/day/12) &rarr; [Solution](./day12/d12.py)
A puzzle of 2D translation and rotation.\
We are provided by a set of movement instructions and need to find the final position of a ship.\
In part 1, the ship moves in 4 directions (N, E, S, W), rotates in 2 directions (L, R), and moves forward (F).\
In part 2, all of the above instructions are applied to a waypoint relative to the ship, except for the forward instruction, which moves the ship towards the waypoint.\
For this, I added the implementation of rotation for `Point` class in my library.

## Day 13: [Shuttle Search](https://adventofcode.com/2020/day/13) &rarr; [Solution](./day13/d13.py)
We have an ordered list of bus IDs, and a starting time.\
Each bus arrives at intervals equal to its ID.\
In part 1, starting from the start time, we need to find the first arriving bus.\
In part 2, we need to find the earliest timestamp from which all buses arrive at their indexes in the list.\
In other works, we need to find the smallest number which has provided remainders when divided by the bus IDs.\
To build this number, we can:
* Start with time=0 and step=1
* For each bus, find the next time that satisfies the condition by adding the step to time until the condition is met.
* Make step the LCM of the previous step and the bus ID (this way the currently met remainders will be preserved).

### Bugs and Issues
* Understanding the fact that the expected remainder is the negative of the order not its positive value took me a while :sweat_smile:

## Day 14: [Docking Data](https://adventofcode.com/2020/day/14) &rarr; [Solution](./day14/d14.py)
A puzzle of bitwise AND/OR masking operations.\
We are provided with a set of instructions to write values to memory addresses.\
Mask definition commands update the current mask, which is defined based on 36 bits of `0`s, `1`s, and `X`s.\
And other commands are write values to addresses with the mask applied to them.\
In part 1, each value is masked and each `0` and `1` bit in the mask is applied to the value.\
In part 2, addresses are masked instead, `1` bits set the corresponding bit to `1`, `0` bits leave the corresponding bit unchanged, and `X` bits are floating bits that can be either `0` or `1`.\
This way each `X` doubles the number of addresses to write to.\
For both of the parts, we need to return the sum of all set values in memory.\
The important part here was to properly implement the masking and address generation functions.\
Good to recall:
* Bitwise operations to `int`s: (`&`, `|`, `^`)
* ```f"{value:036b}"``` to convert an integer to a 36-bit binary string.
* `int(binary_string, 2)` to convert a binary string to an integer.
* `bin(int_value)[2:]` to convert an integer to a binary string.
* `value_str.zfill(36)` to pad a string with zeros to the left.
* `value_str.rjust(36, '0')` to pad a string with zeros to the left.
* `value_str.ljust(36, '0')` to pad a string with zeros to the right.

### Optimizations
* Using the actual bitwise `&` and `|` operations on `int` values is much faster than using string manipulation and casting them to `int`.

### Bugs and Issues
* I first didn't understand the fact that we have more than one mask operations in the input.