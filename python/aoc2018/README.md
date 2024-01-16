# Advent of Code 2018

## Day 13: [Mine Cart Madness](https://adventofcode.com/2018/day/13)
Simulating a set of carts on some track.\
They will select different routs on junctions (in turns), and crash if they collide.\
We need to find the first crash and the last remaining cart.\
A brute-force approach works fine here.\
The only problem I imagine can happen here is to forget moving the carts in the proper order.\
They have to be moved one by one, in the order of their position, not all at the same time.\
This changes the results.

### Bugs and issues:
* Stripping the input ruined the first line of the input; I need to remember to avoid stripping the input for map inputs like this.

## Day X: [Title](https://adventofcode.com/2018/day/X)
desc
### Optimizations:
### Bugs and issues:
