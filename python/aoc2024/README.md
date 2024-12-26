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

## Day 12: [Garden Groups](https://adventofcode.com/2024/day/12) &rarr; [Solution](./day12/d12.py)
A puzzle of analyzing a graph of connected nodes.\
We are provided with a plot of a garden with areas of different types of plants.\
We need to find:
* Each region of 4-connected cells with the same plant type.
* Area of each region: number of cells in the region.
* Perimeter of the region: number of all outer and inner edges of the region.
* In part 2, we need to find the number of sides (edges at the same straight line are counted as one side) of the region.

To solve this problem, we need to implement a simple connected components search algorithm.\
I added this to my `geometry` library as a `find_connected_components` function.\
I tried to implement it in its most possible general form, to be used in future days as well!\
It receives a `dict/set/list` of points and a function to generate the neighbors of a cell.

I also implemented two functions to extract outer and inner borders of a region (`outer_border` and `inner_border`)\
They return border cells and the direction of the border to the cells.

For part 2, we simply need to re-use the `find_connected_components` function to group the 4-connected border cells from each border direction.

**This problems seems to be a good candidate for a future day extension, maybe in 3D or even in super-larger scales!**

## Day 13: [Claw Contraption](https://adventofcode.com/2024/day/13) &rarr; [Solution](./day13/d13.py)
We have a claw machine and two buttons to move the claw right and forward with defined units.\
We have the location of the prize and we need to find the minimum number of moves to reach the prize.\
Pushing button `B` costs `1` token and pushing button `A` costs `3` tokens.\
In part 1, we we are limited to maximum of `100` pushes of each button.\
In part 2, the prize's location is moved `10000000000000` units to both right and forward!\
We need to find the minimum number of tokens to collect maximum number of prizes.\
For some entries, it's impossible to reach the prize, so we shouldn't spend any tokens.\
This puzzle is actually a system of linear equations, with 2 variables and two equations; so easy to solve using `sympy.solve` library function!\
We also need to check some criteria on the solutions:
* The variables should be non-negative,
* They should be integers,
* They should be less than or equal to `100` in part 1.

### Bugs and Issues:
* Again I failed to understand the problem statement properly, and implemented a `MinHeap` search for this!
* Then I figured out what's requested and got the answer in part 1 with an ad-hoc search over `0-100 x 0-100` space.
* Reading and understanding the problem statement was the main challenge in this puzzle.

## Day 14: [Restroom Redoubt](https://adventofcode.com/2024/day/14) &rarr; [Solution](./day14/d14.py)
We have a list of robots' positions and directions in a grid of cells.\
We need to simulate their motion and find their positions after 100 steps and count the number of robots in each of 4 quadrants of the grid.\
In part 2, we need to find the minimum step number that the robots form an easter egg pattern of a christmas tree (see below).\
Since I didn't know what pattern I should expect to find, it took me a long while to formulate the solution.\
Eventually, filtering the size of the connected robots in the center of the frame did the job for me!

### Issues and Bugs:
* In part 2, counting the time from `0`, gave me the `answer - 1` value!
* I initially though maybe the quadrant concept in part 1 could be a clue for part 2, but it was there to mislead us :sweat_smile: The actual key to solution was hidden in [day 12](https://adventofcode.com/2024/day/12)'s [solution](./day12/d12.py)!

### Optimizations:
* Knowing the expected pattern and inspired by part 1, I found a simpler way to find the answer in part 2.\
Counting the robots in the center of the frame (0.25 <= x <= 0.75 and 0.25 <= y <= 0.75) and check if they are more than 50% of all the robots was enough to find the answer!\
I couldn't imaging such a solution without knowing what I'm expecting to find!

### The Easter Egg Pattern of the Christmas Tree:
```
.....................................................................................................
....#................................................................................................
.....................................................#..........................#....................
............#..................................#.......................................#.............
#.........#..........................................................................................
.................#......#.....................................................................#......
.....................................................#........................................#......
..................................................#..................................................
.....#.......................................#..........................#............................
............................#.........#.......................#......................................
.....................................................................................................
....................#................................................................................
.....................................................................................................
................................................#....................................................
.#..............#...#.................................................#..............................
...................#.................................................................................
...................................................................#.................................
.....................................................................................................
.....................................................................................................
.......................................................................................#.............
........................................................................#............................
................................#....................................................................
.............................................................#.........#..............#..............
.................................................................................#...................
.....................................................#...............................................
.......................#.......#..........#..........................................................
...........................................#.........................................................
.....................................................................................................
........................................#......#.....#........#..................#................#..
..............................................................#......................................
.......................................................#.............................................
.#..........................................................................................#........
..................................###############################..............#..........#..........
..................................#.............................#.#..................................
..................................#.............................#........................#...........
.................#..#..........#..#.............................#......#.............................
..................................#.............................#....................................
..................................#..............#..............#....................................
.........................#........#.............###.............#....................................
.....................#............#............#####............#....................................
..................................#...........#######...........#....................................
..................................#..........#########..........#....................................
..................................#............#####............#..#.................................
...........................##.....#...........#######...........#...........................#........
..................................#..........#########..........#....................................
.............................#....#.........###########.........#....................................
..................................#........#############........#....................................
..#...............................#..........#########..........#.#.......................#..........
..................................#.........###########.........#....................................
.....................##...........#........#############........#....................................
..................................#.......###############.......#.................#..................
...#...........................#..#......#################......#.......................#............
.........#........................#........#############........#..#.................................
...........................#......#.......###############.......#....................................
...............#..................#......#################......#....................................
..................................#.....###################.....#....................................
..................................#....#####################....#....................................
......................#...........#.............###.............#....................................
..................................#.............###.............#....................................
..................................#.............###.............#........................#...........
.......#..........................#.............................#....................................
...........................#......#.............................#................#....#..............
......#...........................#.............................#....................................
..................................#.............................#....................................
..................................###############################....................................
.............#.......................................................................................
.............................................................................................#......#
............#........................................................................................
.......................#........................................................#............#.......
.......................#.............................................................................
....................#................................................................................
....................................#................................................................
.....................................................................................................
...............................#.....#........#.............................#........................
..................................................#.............................#.............#......
.....................................................................................................
......................................#...............................#..................#...........
...............................................................................#.....................
..#..................................................................................................
.......................#..........#.........................................................#........
...................................................................................................#.
.....#...............................................................................................
...........#.........................................................................................
......#...................#..........................................................................
.....................................................................................................
.......................................#......#..#............................#......................
.....................................................................................................
...#..........................................................#......................................
...........#.....#......................#.............#...#..........................................
..........................#..........................................................................
.....................................................................................................
...#.............................................................#...................................
.....................................................................................................
..................#...........#...................................................................#..
........#...............#............................................................................
........................#..............................................#.............................
........................................................................................#............
.......................#..........................................................#..#...............
.............................................................#.....................#.................
..................................................................................#............#.....
.....................................................................................................
.........................................................................#...........................
..........................................#..#.......................................................
```

## Day 15: [Warehouse Woes](https://adventofcode.com/2024/day/15) &rarr; [Solution](./day15/d15.py)
We have a 2D warehouse layout with locations of a robot, some boxes and wall cells, plus a set of movement commands for the robot.\
If the cell robot wants to move to is occupied with a box (or a set of boxes next to it), it will try to push them forward.\
The robot and the boxes will move if they have empty space in the direction of the move.\
In part 2, the grid is widened two times (double number of columns, same number of rows) and each box is two cells wide.\
We need to find the final layout of the warehouse after all the (possible) moves are done.\
I got the answer with an ugly implementation; but after re-implementing the solution, I found a much cleaner way to solve the problem:\
* Keep track of the cells to be occupied in a `set`.
* Add the new expected location of the robot to the set.
* While the set is not empty, pop a location and check if any box is there, if so, find the "to be occupied" cell(s) by this box and add it to the set.
* If the current location is occupied with a box which is already in "moving" set (part 2), don't process it.
* If any of the locations we are trying to occupy is a wall, we cannot move, so ignore all the moving boxes.
* If not, and all the "to be occupied" cells are successfully processed, then move the boxes and the robot to the new locations.

Maybe this can be implemented in a cleaner way using `recursion`?

### Bugs and Issues:
* Removing the moved boxes and adding the new ones, one by one is a common mistake!\
We may overwrite the new boxes with the old ones, and the final layout will be wrong!\
Especially when you use a `set` to keep the location of the current boxes :sweat_smile:

## Day 16: [Reindeer Maze](https://adventofcode.com/2024/day/16) &rarr; [Solution](./day16/d16.py)
We have a maze of open cells and walls.\
Moving forward costs `1` and turning left or right costs `1000`.\
All we need to do is to:
* Find the minimum distance cost from the start (marked as `S`) to the end (marked as `E`).
* Find all the possible paths with the minimum distance cost.

Apparently, this is a simple shortest path problem, which can be solved with Dijkstra's algorithm.

### Bugs and Issues:
* Forgetting about `S` and `E` cells to be considered as open tiles!
* It took me a while to figure out Dijsktra's is the proper algorithm to solve this problem.\
I started the hard way with A* and a general MinHeap search!\
Let's say this is what I get when starting to code while I'm sleepy, and without proper thinking and planning :sweat_smile:

## Day 17: [Chronospatial Computer](https://adventofcode.com/2024/day/17) &rarr; [Solution](./day17/d17.py)
This year's first puzzle of simulating a computer!\
We have a set of instructions to be executed on a computer with 3 registers (A, B, and C).\
Part 1 is mainly about simulating the instructions and get the output of the provided program.\
In part 2, we need to find the minimum initial value of registar `A` to make the program generate the same program sequence in its output :smile:\
Letting it run in a brute-force search would give us the answer in centuries!\
So, as expected, we needed to check what the program is doing and find a way to optimize/reverse-engineer it.\
The program iteratively takes the last 3-bits of `A` register (`A % 8`), process it, generates an output value based on it, and then shifts the register to the right by 3 bits.\
This way, we can reverse the order of the loop, search for all the remainder values between `b000`=`0` and `b111`=`7` and pick the minimum one that generates the same output as expected.\
We will get the minimum possible initial value for `A` iteratively, by multiplying the `A` value from the previous iteration by `8` and adding the current possible value or the remainder.\
But, for some indices, there are no possible value and when this happens, we need to backtrack to the previous indices and pick higher possible values.

### Bugs and Issues:
* First I tried to fully understand what the actual loop is doing, to simplify it.\
<b>But like many of the previous years' "Assembly Simulation" puzzles, it was not necessary.\
Here we still can let the majority of the program run as is, but understand the main loop and model it in a simpler way.</b>

## Day 18: [RAM Run](https://adventofcode.com/2024/day/18) &rarr; [Solution](./day18/d18.py)
Yet another min-distance path finding puzzle!\
We are provided with the location of the walls (falling bytes) and default start and goal locations.\
We need to find the minimum distance from the start to the goal, considering only first `N` falling bytes and walls.\
Out of the box algorithm to solve this is Dijkstra's algorithm.\
In part 2, we need to add the falling bytes one by one and find the first one which blocks the path from the start to the goal.\
The ad-hoc looping may take minutes to complete, but we can use a binary search find the answer in logarithmic time.

### Bugs and Issues:
* Forgot to cast `str` to `int` for `x` and `y` coordinates of the falling bytes!
* Being low in the global and private leaderboards, hints me that I need more prepared libraries for classic problems like these :smile:

## Day 19: [Linen Layout](https://adventofcode.com/2024/day/19) &rarr; [Solution](./day19/d19.py)
We are provided with a list of available patters (in `str`) and a list of needed designs (in `str`).\
In part 1 we need to find how many of the needed designs can be composed by the available patterns (with simple concatenation and possible repeating).\
In part 2, we need to find the sum of all possible ways to do so.\
This may sound complicated at first, but it's quite easy to implement it with (`@cache`ed) recursion.\
All we need to do is, for each needed design, iterate over all the and if the design starts with the pattern, call the function recursively with the rest of the design.\
My implementation for this recursive function is a single line of code in Python:\

```python
@cache
def ways(self, d):
    return sum(self.ways(d[len(p) :]) for p in self.pat if d.startswith(p)) if d else 1
```

## Day 20: [Race Condition](https://adventofcode.com/2024/day/20) &rarr; [Solution](./day20/d20.py)
Another shortest-path related puzzle!\
We are provided with a grid of cells with walls and open tracks, plus start (`S`) and end (`E`) locations.\
The special rule in this puzzle is that we can cheat and bypass walls now!\
In part 1, we need to find all the possible 2-step cheats (bypassing one wall) that can shorten the shortest path at least 100 steps.\
In part 2, we need to find the the possible maximum 20-step cheats that can shorten the shortest path at least 100 steps (not all the steps need to be walls!).\
The solution was simple:
* First we need a simple Dijkstra's algorithm to find the shortest distances to start for all the track cells.
* For part 1, iterate over all the wall cells and check the max and min shortest path values to the start in their neighborhood. If the difference is more than 100, we found one cheat!
* For part 2, we can iterate over all the possible pairs of track cells and check if cheating between them can shorten the path by at least 100 steps.
    * The conditions for the cheat are:
        * The manhattan distance between the pair should be at most `20`.
        * The difference between their shortest path values to the start should be at least `100`.

The above part 2 solution is also usable for part 1, consider the maximum distance between the pair to be only `2`.

### Bugs and Issues:
* For part 2, I got my mind locked with my initial solution of part 1; thinking about finding paths between walls!\
All I needed was to rethink and find the proper yet easy way to solve the problem.

### Optimizations:
* Instead of iterating over all the pairs of track cells, we can iterate over the range of the manhattan distance for each cell!\
The implementation will be a bit more complex, but it will be much faster.

## Day 21: [Keypad Conundrum](https://adventofcode.com/2024/day/21) &rarr; [Solution](./day21/d21.py)
This puzzle was the most challenging one in 2024 so far for me!\
We have a physical keypad with 10 digits and an `A` button.\
We need to enter some sequences of digits ending with an `A`.\
We start at the `A` button and need to find the moves in `<, >, ^, v` directions to reach the desired digit, and the press it.\
To apply these moves, we have a robot with a different keypad layout (named directional keyboard, including `<, >, ^, v, A` buttons).\
And we need to find the minim movements on this keyboard to enter the desired sequence in the first physical keyboard.\
Yet, we have another robot entering the sequence in a similar directional keyboard.\
So each single move in the first keyboard exapnds to a large sequence for the last keyboard.\
In part 2, instead of 2 robots, we have 25 robots in the loop!\
Each input sequence can be entered by more than one sequence in each of these keyboard levels, but we need to find the shortest!\
They key to solve this puzzle was to calculate the histogram of each of the moves (in a dictionary like data structure) and then expand it step by step for next robot, in a dynamic programming way.\
I need to get back to this puzzle, refine and explain better here! `TODO` :sweat_smile:

## Day 22: [Monkey Market](https://adventofcode.com/2024/day/22) &rarr; [Solution](./day22/d22.py)
Rather a break for today!\
The main challenge in this puzzle was actually to read and understand the problem statement!\
We are provided with a list of numbers (buyers' secrets).\
We need to apply a set of operations (including `*, //, ^, %`) to generate next numbers, 2000 times each.\
In part 1, we need to find the sum of all the numbers after the operations.\
In part 2, we need to find a pattern that maximizes the prices of banana sales! :monkey:\
Price at each step (during the 2000 iterations) is the right most digit of the secret number.\
But we only sell when we see a pattern of 4 numbers in the last 4 price changes.\
We need to find the best pattern that maximizes the sales, and return that sum of sales.\
My solution was to use a `deque` of last `4` price changes, a `defaultdict` (keyed on the last 4 changes) to keep the sum of sales for each 4-tuple, and a set to keep the seen 4-tuples per customer (it will be sold on the first seen pattern).

## Day 23: [LAN Party](https://adventofcode.com/2024/day/23) &rarr; [Solution](./day23/d23.py)
A puzzle of finding the maximal set of all-interconnected nodes in a graph.\
To do so, I started with the input edges (as level `2`) and iteratively for each new level:
* Check each group in the previous level and find the common connected nodes between all of them.
* Build a new group by adding the common nodes to the previous group and add it to this level's groups.
* Stop when we cannot find any new group in the current level.

To avoid repetitive groups, we need to cast them to tuples of sorted nodes and keep them in a set.

## Day 24: [Crossed Wires](https://adventofcode.com/2024/day/24) &rarr; [Solution](./day24/d24.py)
A puzzle of emulating some input binary gates of `AND`, `OR` and `XOR` which are connected to some input `0`s and `1`s.
In part 1 we need to find the value of `z`-named output gates.\
In part 2, we need to emulate half-adder and full-adder circuits!\
We are provided with a set of input binary bits and full-adder connections, but four of the wires are incorrectly connected.\
We need to find those four wires (four pairs of incorrect connections) and return their sorted names.\
I initially solved this puzzle manually (knowing what connections are needed) is much easier than an algorithm to automatically find the pairs.\
Now the initial implementation of finding those incorrectly connected pairs is done, but it's not very neat yet!\
Will be refined :wink:

## Day 25: [Code Chronicle](https://adventofcode.com/2024/day/25) &rarr; [Solution](./day25/d25.py)
A very simple puzzle of reading 2D patterns of keys and locks and find the number of fit (non-overlapping) pairs.\
Locks have their top row filled and keys have their bottom row filled.\
Solution can be done very simply by turning all the patterns to sets of 2D points and count how many of all the possible pairs don't have any `intersection`.