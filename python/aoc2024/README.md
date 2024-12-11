# Advent of Code 2024

## Day 1: [Historian Hysteria](https://adventofcode.com/2024/day/1) &rarr; [Solution](./day01/d01.py)
Typical day 1 problem, we are provided with two columns of numbers and we need to find:
* sum of distances between the corresponding numbers in the sorted columns.
* sum of values of left column numbers, each multiplied by the number of occurrences in the right column.

## Day 2: [Red-Nosed Reports](https://adventofcode.com/2024/day/2) &rarr; [Solution](./day02/d02.py)
We are given a list of numbers (a report of multiple levels) in each input line and we need to find how many are safe.\
The criteria for the report to be safe is:
* It must be either strictly increasing or strictly decreasing.
* The difference between adjacent numbers must be between 1 and 3.

In part 2, we can accept one bad level in each report, and we need to find the number of safe reports.\
Easy and tractable to do ad-hoc.\
But this seems to be something we should know how to optimize in larger scales for future days :wink:
### Optimizations:
* Using `itertools.combinations` to find the number of ways to remove one element from the list.\
This is maybe not an optimization, but a good use of the library and clean code.\
It's good to remember, `itertools.combinations` keeps the order of the elements in the list.
### Bugs and Issues:
* <b>Never ever refresh the webpage few seconds before the puzzle unlocks.\
This made my session shaky and took me about a minute to get the puzzle and inputs :angry: </b>

## Day 3: [Mull It Over](https://adventofcode.com/2024/day/3) &rarr; [Solution](./day03/d03.py)
A nice yet simple problem to be solved using regular expressions.\
The only challenge here is implement the parsing of the input quickly and correctly.\
In part one, we need to find all proper patterns of `mul(X,Y)` for integer `X` and `Y`s, and calculate the sum of all multiplications.\
In part two, we also need to find `do()` and `don't()` commands and enable/disable the calculation temporarily (till the next command).

### Bugs and Issues:
* I was millimeters to the proper implementation, but forgot to capture the `do()` and `don't()` commands.\
<b>Instead of "mul\((\d+),(\d+)\)|<span style="color:red">(</span>do\(\)<span style="color:red">)</span>|<span style="color:red">(</span>don't\(\)<span style="color:red">)</span>" I used "mul\((\d+),(\d+)\)|do\(\)|don't\(\)"!</b>\
This took me more than 20 minutes to implement another uglier solution to get the correct answer.

## Day 4: [Ceres Search](https://adventofcode.com/2024/day/4) &rarr; [Solution](./day04/d04.py)
A puzzle of searching for patterns in a map of characters.\
In part one, we need to find the number occurrences of the word "XMAS" in the map, horizontally, vertically, diagonally, and reverse.\
In part two, we need to find the X patterns of 5 characters that has two "MAS" in it.\
Nothing special here to optimize!

### Bugs and Issues:
* Instead of using a `dict` to store the characters, it will be better to use a `defaultdict` with an invalid default value.\
This way, you do not need to check if the key exists in the dictionary or not.
* I had a stupid bug in part one, forgetting to multiply the step number by the direction vector in the loop! Took minutes to figure it out :facepalm:
* Looking at my code, after cleaning it up, I think I could be way quicker to implement the solution; maybe I need few seconds of thinking and planning before starting to code.

## Day 5: [Print Queue](https://adventofcode.com/2024/day/5) &rarr; [Solution](./day05/d05.py)
This puzzle was mainly about sorting lists with partial ordering.\
We are provided with a set of partial ordering rules and some lists of numbers to be sorted.\
We need to sum the medial values of pre-sorted lists, and sorted lists with the given rules.\

### Optimizations:
* Using `functools.cmp_to_key` to convert the comparison function to a key function for sorting.
* Do we need to cast all the numbers to `int`? Not really; we use them as keys, so we can simply keep them as `str`.

## Day 6: [Guard Gallivant](https://adventofcode.com/2024/day/6) &rarr; [Solution](./day06/d06.py)
Another puzzle of traveling simulation inside a grid of open and blocked cells.\
The guard moves forward till it hits a wall, then it turns right and continues.\
In the first part we need to find the number of visited cells by a guard before it exits the grid.\
In the second part, we need to find the possible positions in the grid which blocking them would put the guard in an infinite loop.

### Bugs and Issues:
For such an easy and familiar problem, I had numerous bugs in my implementation, which slowed me down a lot:
* I failed to properly read the problem statement in part 2, and searched over different starting positions and directions!
* Instead of initiating the visited `set` as `{(x,y)}`, I initiated it as `{x,y}`!
* I started the implementation by keeping all the grid values in a `dict` with the coordinates as keys, which was not necessary at all!\
I knew it's way more efficient to only keep the blocked cells in a `set`, but I didn't start with that!
* For part 2, I started with searching for all cells to check obstruction! But the only needed cells to be checked are actually the ones we travelled in part 1!

## Day 7: [Bridge Repair](https://adventofcode.com/2024/day/7) &rarr; [Solution](./day07/d07.py)
Searching for the missing operations between a list of numbers and check if we can find a valid operation sequence to reach the target number.\
In part one, we only have `+` and `*` operations; in part two a third operation of concatenation is added (`10 || 11 = 1011`).\
For now, the ad-hoc way of searching all the possible combinations is enough to solve the problem.\
Will we face an extension of this in future days? :thinking:

### Bugs and Issues:
* I first solved this with a full BFS search! But then I realized that we can simply use `itertools.product` and iterate over possible combinations.

### Optimizations:
* Since numbers are all positive and greater than 0, we can stop the calculation if the current result is greater than the target number.
* Alright, DFS search supposed to be and actually is faster than BFS and the `itertools.product` solution; I added the DFS search solution as well.
* Moving from right to left should limit the search space drastically, since:
    * `*` operator can get eliminated if the current value would not be divisible by the next number.
    * `||` operator can get eliminated if the current value would not be a suffix of the next number.


## Day 8: [Resonant Collinearity](https://adventofcode.com/2024/day/8) &rarr; [Solution](./day08/d08.py)
A simple puzzle of extrapolating pairs of points in a map (with same character) and counting the new extrapolated points which are also in the map.\
In part one, we extrapolate only once in each direction, and in part two we extrapolate multiple times in each direction.

## Bugs and Issues:
* Again the main challenge was to read and understand the problem statement.\
The text was unnecessarily long and confusing, but the problem was simple and easy to implement.
* The provided sample for part 2 was quite tricky! It was showing the final state of the map after the extrapolation!
* I really needed a `Point` library class to handle the points and operations on them quickly.\
It's included in my solution now :wink:

## Day 9: [Disk Fragmenter](https://adventofcode.com/2024/day/9) &rarr; [Solution](./day09/d09.py)
A puzzle of simulating a disk defragmentation.\
I would say this one was the first puzzle of 2024 that needed some thinking to implement the proper solution.\
We are provided with a list of digits, odd ordered ones are file sizes and even ordered ones are the free space between files.\
In part one, we can break the files into unit sizes and moved each unit to the first available free space.\
In part two, we need to find a free space to move the whole file, if not found, we have to keep the file as is.

### Bugs and Issues:
* Understating the problem statement was a challenge here as well.\
In part 2, we have to move the files in the descending order of their IDs, not their locations!
* Ignoring the consecutive free spaces leads to very hard to catch bugs!

### Optimizations:
* Using `deque` for part 1, to quickly add/remove parts to the beginning and the end of the disk.
* Implementing a double linked list for part 2, to quickly insert new nodes in the middle of the list.

## Day 10: [Hoof It](https://adventofcode.com/2024/day/10) &rarr; [Solution](./day10/d10.py)
A simple path finding puzzle in a grid of digits.\
Each valid path starts at a cell with value `0`, moves step by step to neighboring cells with strictly `+1` increasing values, and ends at a cell with value `9`.\
In part 1, we need to find the sum of count of reachable `9`s from all `0`s.\
In part 2, we need to find the number of all paths from each `0` to each `9`.

### Bugs and Issues:
* As always, reading and understanding the problem statement was the main challenge to me.\
I literally implemented part 2 reading part 1 :sweat_smile:

### Optimizations:
* Today's was a perfect example puzzle to be solved with dynamic programming.\
Starting from `9`s and moving backward to `0`s, we can find reachable `9`s and calculate the number of paths from each cell.

## Day 11: [Plutonian Pebbles](https://adventofcode.com/2024/day/11) &rarr; [Solution](./day11/d11.py)
We are provided a list of stones with numbers engraved on them.\
At each time step, stones change based on their own numbers:\
* If the number is `0`, it turns to `1`.
* Else if the number has even digits, it split to halves with higher and lower halves of digits, e.g. `1234` -> `12` and `34`.
* Else the number is multiplied by `2024`!
We need to find the number of total stones after `25` (`75` in part 2) time steps.

### Optimizations:
* Understanding what is requested as the final answer (number of stones) was a key in this puzzle:
    * The order of stones does not matter;
    * Each stone evolves by its own number and does not affect the others;
* Thus, it's obviously another **dynamic programming** problem, we can keep track of the number of stones generated by each stone number and after each number time steps.\
This way, we can build the grid of higher step values based on previous step values.\
Python's `@cache` decorator is a perfect tool for this kind of problems.