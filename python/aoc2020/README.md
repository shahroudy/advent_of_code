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

## Day 15: [Rambunctious Recitation](https://adventofcode.com/2020/day/15) &rarr; [Solution](./day15/d15.py)
A puzzle of sequence generation.\
Each new item is generated based on the last item's previous index in the sequence.\
If it was the first appearance, the next number will be `0`, if not, the next number will be the difference between the last and the previous index.\
In part 1, we need to find the `2020`th number in the sequence.\
In part 2, we need to find the `30,000,000`th number in the sequence.\
The ad-hoc way to build and keep the sequence in a `list`, which is not tractable for part 2.

### Optimizations
* Using a `dict` to store the last index of each number in the sequence.
* Using a `list` instead of the `dict` can run two times faster, since it don't need to hash the keys.
* Running the python code with `pypy` can run the code ~6 times faster here (~0.46s vs ~2.7s).

## Day 16: [Ticket Translation](https://adventofcode.com/2020/day/16) &rarr; [Solution](./day16/d16.py)
A puzzle of handling combinations of ranges and matching possibly values to ranges.\
We are provided with:
* A set of rules, each rule has a name (field name on the tickets) and a combination of valid ranges.
* A ticket with an ordered list of values.
* A set of nearby tickets with ordered lists of values.

In part 1, we need to find the nearby tickets which have numbers that are not valid in any of the rules, and return the sum of these numbers.\
For part 2, first we need to eliminate the invalid tickets, then we need to find the correct order of the fields on the tickets, and then we need to multiply the values of the fields that start with `departure` in our ticket and return the result.\
The easy approach to solve this was to check possible matches between rules and columns and find the matches one by one.\
The key to simplify the solution here was to implement a class to handle combinations of ranges and check if a value is valid in the ranges; I now have it in my library as `ExRange` class, and solving this helped me to fix a bug in it :smile:

## Day 17: [Conway Cubes](https://adventofcode.com/2020/day/17) &rarr; [Solution](./day17/d17.py)
A cellular automata puzzle with expanding boundaries in 3D and 4D space.\
We are provided with the initial 2D grid of active (`.`) and inactive (`#`) cubes.\
The rules are simple:
* If a cube is active and exactly 2 or 3 of its neighbors are also active, the cube remains active. Otherwise, the cube becomes inactive.
* If a cube is inactive but exactly 3 of its neighbors are active, the cube becomes active. Otherwise, the cube remains inactive.

The diagonal neighbors are also considered here; so in 3D space, each cube has 26 neighbors, and in 4D space, each cube has 80 neighbors.\
In part 1, we need to simulate the 3D cellular automata for 6 cycles and return the number of active cubes.\
In part 2, we do the same in 4D space.

### Optimizations
* Keeping only the active cubes in a set and iterating over them only can save a lot of time and memory.
* At each iteration, we only need to check the neighbors of the active cubes, not all the cubes in the space.
* Having a library of 2D, 3D, and 4D points can be very helpful in these kind of problems.

## Day 18: [Operation Order](https://adventofcode.com/2020/day/18) &rarr; [Solution](./day18/d18.py)
A puzzle of evaluating input math expressions but with customized operator precedence.\
We are provided with a set of expressions consisting of numbers, `+, *` operators, and parentheses.\

In part 1, we need to evaluate based on:
* `+` and `*` have the same precedence, and are evaluated from left to right.
* Parentheses are evaluated first.

In part 2, we need to evaluate based on:
* `+` has higher precedence than `*`.
* Parentheses are evaluated first.

My solution was to implement recursive functions to evaluate the expressions based on the rules.

### Bugs and Issues
* Using `str.replace()` to replace evaluated sub-expressions with their results is risky, since it replaces all occurrences of the sub-expression in the expression.\
It leads to wrong answers in part 1, when we have multiple occurrences of the left-most sub-expression!\
But the solution is simple, just replace the first occurrence of the sub-expression: `expr.replace(sub_expr, str(eval(sub_expr)), 1)`.
* Not about the difference between `re.match` and `re.search` in `re` module:
    * `re.match` matches the pattern from the beginning of the string.
    * `re.search` matches the pattern anywhere in the string.

## Day 19: [Monster Messages](https://adventofcode.com/2020/day/19) &rarr; [Solution](./day19/d19.py)
A puzzle of grammars and parsing input expressions.\
We are provided with a grammar (set of rules) and a set of messages to parse with the grammar.\
In part 1, we need to find the number of messages that match rule `0`.\
<b>Starting from terminals and building `re`s for each term, part 1 would be easy to solve since the input grammar is a regular grammar (everybody knows Eric loves regular expressions! :smile:).</b>\
In part 2, the grammar is updated with two rules:
* `8: 42 | 42 8`
* `11: 42 31 | 42 11 31`\
Which makes the grammar context-free and not so easy to solve with regular expressions.\
Updated `rule 8` can still be converted to a regular expression (like `(r42)+`), but `rule 11` can't.\
Looking at the very limited sizes of the input expressions, my solution was to limit the recursion to a limited depth (5 was enough for the input) and define the updated `rule 11` as a combination of `1, 2, 3, 4, and 5` repetitions of `r42` and `r31`.

### Optimizations
* <b>The `Lark` library can be used to parse context-free grammars.</b>
* This makes the implementation of the solution kind of trivial :sweet_smile:
* I added an alternative solution using `Lark` in the `day19` folder, and a related utility function to my library.

## Day 20: [Jurassic Jigsaw](https://adventofcode.com/2020/day/20) &rarr; [Solution](./day20/d20.py)
We are provided with a set of 2D binary patterns with IDs and need to find the correct arrangement of the patterns.\
Each tile can be rotated and flipped, and the final neighbor tiles should have matching 1D patterns on their common edges.\
To build the final image, first we need to find the matching sides and then get rid of the borders of each tile, merge them all together, and find the sea monsters in the final image.\
Provided sea monster pattern is also a 2D binary pattern that can be rotated and flipped as well.\
Part 1 of the puzzle is actually a very nice hint of finding the corner tiles by counting the number of matching sides.\
For part 2, we need to start with any of the corners and build the final image by matching the sides of the tiles, one by one.\
To handle the 2D patterns, one can use `numpy` 2D arrays, and to handle the rotations and flips, one can use `numpy.rot90` and `numpy.flip` functions.\
But I preferred to implement my own functions to handle these operations.\
To represent the 2D patterns, I used `tuple`s of `str`s.\
For quicker operations in part 2, I built the final image as a `set` of 2D `Point`s.\
I added a number of funcions to my `myutils.matrix` library to handle needed operations:\
`find_all_points_with_value`, `flip`, `rotate`, `sub_matrix`, `tile_side`.\
Overall, this puzzle sounds to be the most complex one in this year's AoC.

## Day 21: [Allergen Assessment](https://adventofcode.com/2020/day/21) &rarr; [Solution](./day21/d21.py)
The input is a set of lines, each include a list of ingredients and the list of all allergens they have.\
In part 1, we need to find the number of times the ingredients that can't have allergens appear in the list.\
In part 2, we need to find the exact one ingredient for each allergen.\
I had a match finding function that does the job for part 2 and obviously solves part 1 as well.\
So the only challenge was to quickly parse the input and build the needed data structures.

## Day 22: [Crab Combat](https://adventofcode.com/2020/day/22) &rarr; [Solution](./day22/d22.py)
A card game puzzle.\
We are provided with two decks of cards and need to simulate a card game.\
In each round, the top card of each deck is compared, and the winner takes both cards and puts them at the bottom of their deck.\
In part 2, if the top card of each deck has a value less than or equal to the number of cards remaining in the deck, a recursive game is played.\
The winner of the round is the winner of the recursive game.\
The game ends when one of the decks is empty, or a configuration is repeated (if so player 1 wins).\
Nothing special here, the only challenge was to read the problem statement, understand the mechanics of the game and implement it.

### Optimizations
* Using `deque` to represent the decks.
* Using `tuple` to represent the game state and `set` to keep track of seen states.

## Day 23: [Crab Cups](https://adventofcode.com/2020/day/23) &rarr; [Solution](./day23/d23.py)
An interesting puzzle of rearranging a circular list of numbers.\
We are provided with a list of numbers and need to simulate an iterative process of rearranging the numbers in the cycle.\
In part one, we need to find the final arrangement of the numbers after 100 iterations.\
But in part two, the number of iterations is increased to 10,000,000, and the number of elements is increased to 1,000,000, so no ad-hoc solution is tractable.

### Optimizations
* Using a `dict` to represent the circular list and keep track of the next number for each number is the key to optimize the solution.

## Day 24: [Lobby Layout](https://adventofcode.com/2020/day/24) &rarr; [Solution](./day24/d24.py)
A puzzle of moving on a hexagonal grid of tiles.\
We are provided with a set of instructions to move on the grid (from the center tile, at each line of input file), and flip (between white and black sides) the tile at the final position (default is white).\
Steps are in 6 possible directions: `e`, `se`, `sw`, `w`, `nw`, and `ne`.\
In part 1, we need to find the number of black tiles after the given instructions.\ 
Double flipping each tile will turn it back to white.\
In part 2, we need to simulate a cellular automata on the grid, which is based on the current state of the tile and the number of black tiles around it.\
I solved this puzzle by:
* Modelling the moves on the hexagonal grid as 2D moves: 
```python
directions = {
    "e": Point(2, 0),
    "ne": Point(1, -2),
    "se": Point(1, 2),
    "w": Point(-2, 0),
    "nw": Point(-1, -2),
    "sw": Point(-1, 2),
}
```
* Using a `set` to keep track of only the black (flipped) tiles.

### Bugs and Issues
* I misinterpreted the problem in variety of different aspects:
    * Instead of starting from the center tile for each new line of instruction, I was continuing from the last position.
    * Instead of flipping only the end tile, I was flipping all the tiles in the path.
    * And in part 2, I misread the rules of the cellular automata!