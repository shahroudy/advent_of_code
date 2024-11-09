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

## Day 14: [Chocolate Charts](https://adventofcode.com/2018/day/14)
Expanding a list of numbers till a certain number of digits is reached.\
Nothing special here, just a simple loop.\
My implementation is brute-force and slow, but it works fine for the input (taking ~16 seconds).\
Using type casts between `int` and `str` was making the implementation simple here.

## Day 15: [Beverage Bandits](https://adventofcode.com/2018/day/15)
Simulating a battle between elves and goblins.\
The battle is turn-based, and the units can move and attack.\
The main challenge in this problem was to read and understand the problem statement.\
There were some details to consider.\
The implementation of the operations in the "reading order" was easily done by always considering the adjacent cells in the order of "up, left, right, down".\
Even the concept of finding the in-range cells was simply applied if you find the shortest path to the closest enemy to take the first step towards it.

### Bugs and issues:
* Figuring out how to find the proper round number for the last round was a bit tricky.\
  Especially if you try to break the loop when the combat is over!\
  The proper way was to calculate the "outcome of the combat" right inside the loop and return it there.
* I had a disturbing bug in my implementation:\
  I was building the list of locations of the units, sorted in reading order, to handle the turns.\
  There were cases (only happening for the input, and not in samples) that the dead units' location were later occupied by other units, and when it was their turn I was further moving the new unit instead of skipping the dead one.\
  This literally took me days to fix! :sweat_smile:

## Day 16: [Chronal Classification](https://adventofcode.com/2018/day/16)
Simulating a computer with some simple instructions to read and write from/to registers.\
Nothing challenging here, just a simple simulation and matching the instructions to the opcodes.


## Day 17: [Reservoir Research](https://adventofcode.com/2018/day/17)
Simulating water flow in a grid of open and clay blocks.\
Though it took me a long while to solve this puzzle, the solution was simple eventually.\
The keys to solve this puzzle were:
* To quickly visualize the state and check the possible mistakes in the implementation.\
Since the input spans a large area, I had to save the state of the grid to a file and keep the file open in an editor to visualize the state, step by step.
* To create extra samples to cover the corner cases easier.\
The provided sample was too simple and did not cover corner cases happening in the input file.
  
## Day 18: [Settlers of The North Pole](https://adventofcode.com/2018/day/18)
A cellular automaton problem.\
Each acre (cell) changes its state based on the states of its neighbors.\
Not much of a challenge here, just a simulation, with one optimization trick.

### Optimizations:
* In part 2, the simulation runs for a billion steps, which makes the simple brute-force approach too slow.\
  The trick is to find the cycle in the state of the grid and fast-forward to the final state.
* For easier handling of cells and their neighbors, I used a string to represent the grid, and I used a dictionary to store the indices of neighbors for each cell.

## Day 19: [Go With The Flow](https://adventofcode.com/2018/day/19)
Emulating another assembly program (extension of Day 16), with jump command functionality.\
Part 1 was simple, just running the program and finding the value of a register.\
Part 2 was not tractable with the brute-force approach, so I had to translate the assembly code to higher levels and implement it in a more efficient way.\
Analyzing the assembly code, I found that it was calculating the sum of the divisors of a number.\
The input number is generated in a sub-routine (lines 17 afterwards), and the sum of its divisors is calculated in the main loop.

### Optimizations:
Simply let the sub-routine generate the number and save it in register #5.\
Then we can calculate the sum of the divisors of it in Python.

### Bugs and issues:
<b>Looking at the assembly code, I should be able to find the sub-routine part quickly and skip analyzing it.\
We always cal let that part run in the emulator and get the result.\
All we need to analyze is the main loop which is not running efficiently.</b>

## Day 20: [A Regular Map](https://adventofcode.com/2018/day/20)
This puzzle was about passing through the input path and finding the farthest room from the starting point.\
They provided path is consists of a set of doors towards north, south, east or west.\
The also have branches, coded with parentheses.\
The key to the solution was:
* use a list (as a stack) to keep track of the position when we encounter a branch.
* use a dictionary to store the distance of each room from the starting point.

And the input being a `regex` was just a distraction, we really don't need to use `re` here; simply ignore `^` and `$` and use the input as is.

## Day X: [Title](https://adventofcode.com/2018/day/X)
desc
### Optimizations:
### Bugs and issues:
