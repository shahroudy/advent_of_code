# Advent of Code 2023

## Day 1: [Trebuchet](https://adventofcode.com/2023/day/1)
Finding sub-strings of digits (in digital and alphabetic) in each line.\
This was sort of challenging due to:
* Overlapping alphabetic digits in each line
* Lack of out-of-the-shelf functions to find all overlapping alphabetic digits
  * `re.finditer` was looking like a good tool here, but it cannot find overlapping instances
  * One needs to define the `re` to be non-capturing for this to work!
* I eventually solved it by looping over indices!
* Refining it made me revisit:
  * `re.match` vs `re.search`
  * `re.findall` vs `re.finditer`
  * `str.rfind` finds the last match of a sub-string!

### Optimizations:
* We only needed to find the first and the last, so finding the first in both directions will do the job and we don't need to consider overlapping instances!
* Then a simple `re.search` can do the job
* `str[::-1]` gives the reverse of the `str`
* Now I feel stupid :sweat_smile:

## Day 2: [Cube Conundrum](https://adventofcode.com/2023/day/2)
This puzzle was mainly about reading the description carefully and implement it accordingly.
Warming up on:
* `collections.defaultdict`
* `str.split()`

## Day 3: [Gear Ratios](https://adventofcode.com/2023/day/3)
The only challenge here was to properly parse the input and find numbers, symbols and their locations.
### Bugs and issues:
* A possible bug that may happen in such inputs is to forget the final number in each line, since it is not followed by a symbol.

## Day 4: [Scratchcards](https://adventofcode.com/2023/day/4)
Again the only challenge here was to understand the puzzle statement and properly parse the input.
### Optimizations:
* Using `set.intersection` 
* Finding the match counts in the parsing step

## Day 5: [If You Give A Seed A Fertilizer](https://adventofcode.com/2023/day/5)
First real challenge of 2023!\
We have 7 layers of one-to-one mappings, and we need to find the final state of the seed (location) after applying all the mappings.
Part one was very easy, just to parse the input properly and apply the mappings one by one.\
Part two was the challenge, running the mappings on all the input numbers was too complex to run.
### Optimizations:
* My first implementation was to iterate over the locations from 0 (since we need to find the minimum) and apply the reverse mappings to check if the initial seed was in the list or not.
* The much faster implementation is to process the ranges instead of numbers.

## Day 6: [Wait For It](https://adventofcode.com/2023/day/6)
Nothing challenging here, just reading the puzzle statement, parsing inputs and calculating the different ways!\
Well, the title "Wait For It" may suggest we will see this puzzle again in the future!\
So, let's optimize it further.
### Optimizations:
  Finding waiting times which meet `(time - t) * t > distance` are actually the integers between the two roots of the equation: `time*t - t^2 - distance = 0`.\
  So we can solve this quadratic equation and find the roots, then find the integers between them.

## Day 7: [Camel Cards](https://adventofcode.com/2023/day/7)
Alright! Ranking poker hands! This one was my favorite!\
But where are the suits? :spades: :hearts: :clubs: :diamonds:\
Anyways, using `collections.Counter` was the key here.\
Using `functools.cache` could also help to speed up the running time.

## Day 8: [Haunted Wasteland](https://adventofcode.com/2023/day/8)
Another easy part1 and a little tricky part2.\
Brute force search will take a very long time to complete.
### Optimizations:
* Find needed steps for each starting node, and find `math.lcm` (least-common-multiplier) of all.
* It's the same trick for 2022 Day 11 Part2: [Monkey In The Middle](https://adventofcode.com/2022/day/11)

## Day 9: [Mirage Maintenance](https://adventofcode.com/2023/day/9)
Simple numeric implementation of extrapolation of a sequence of numbers in an unknown degree polynomials .\
Very long description of the statement, was there to skip reading :laughing:.\
My first quick yet working implementation was to build and keep all the difference steps and build the needed numbers based on the first and last items of difference values.\

### Optimizations:
* First step to improve the memory usage is to keep only the last and the first values of each difference step.
* It turns out that you can simply build the needed numbers by adding and subtracting the difference values along the way and avoid storing data in memory.
### Bugs and issues:
* My new integer reading template function was not catching negative signs :sweat_smile:. It took me a while to figure that out! so I had to fix it.
* How to calculate the fist number was a bit tricky, based on the number of the steps (being even or odd), we need to add or subtract the first difference value. So I added a sign variable and switched its sign after each step. Now the final implementation is much shorter and much more efficient:
```python 
    self.sum_firsts = self.sum_lasts = 0
    for history in self.histories:
        dif = history
        first = last = 0
        sign = -1
        while any(dif):
            last += dif[-1]
            first = dif[0] - first
            sign *= -1
            dif = [dif[i + 1] - dif[i] for i in range(len(dif) - 1)]
        self.sum_lasts += last
        self.sum_firsts += first * sign
```

## Day 10: [Pipe Maze](https://adventofcode.com/2023/day/10)
I got really stuck on this one!\
I had obvious wrong assumptions about the starting point.\
So I implemented a BFS search to find the farthest point from the starting point.\
It eventually turned out to be a single and simple loop which was very easy to find.\
For part two, my trick was to up-sample the map by a factor of 2 and then flood-fill to detect all the outer points.\
Then finding the inner ones is obvious.
### Bugs and issues:
Missing the point about the start point `S` is actually a simple connection that you should guess based on its neighbors.\
My first implementation was assuming all the neighbors of `S` are connected to it!\
It took me about an hour to figure this out! :sweat_smile:
### Optimizations:
Using flood-fill did the job today, but is not the most efficient way to solve this puzzle.\
The exact same problem came back in Day 18: [Lavaduct Lagoon](https://adventofcode.com/2023/day/18) :sweat_smile: and it took me hours to find a better solution.\
[TODO] So, I need to revisit this puzzle and fix it here.\
The more efficient solution is to process each row and count the inner tiles.\
Along the row, you need to check if you're in or out of the contour and count the inner tiles accordingly.

## Day 11: [Cosmic Expansion](https://adventofcode.com/2023/day/11)
This ones was easy; the efficient implementation was actually easier than the brute force one!\
Keeping track of missing rows and columns and derive a mapping of indices according to the expansion factor was the key here.\
After some cleanup, my whole solution is ~30 lines of code yet very efficient in Python!

## Day 12: [Hot Springs](https://adventofcode.com/2023/day/12)
Now a really challenging puzzle!\
We need to find all the possible ways of matching an input string to a given pattern of consecutive damaged springs.\
The input string has 3 possible characters: `.` (operational), `#` (damaged), `?` (unknown).\
The pattern to match is a list of consecutive damaged springs.\
For part one, I felt an easy brute-force search will do the job, but I was sure it will not work for part two, so I spent few minutes on it and got the answer quickly.\
For part two, I was not sure how to optimize it. The puzzle was looking very much doable by dynamic programming, but I didn't manage to model it accordingly.\
So, after spending some time thinking, I decided to start with a sub-optimal solution: finding groups of patterns (groups of `#`s and `?`s) that can be matched and then find the number of ways of matching mutual groups.\
So I started by building a stack of states that can match the pattern with the numbers from beginning and move forward in a DFS manner.\
Unfortunately, this approach failed badly! Running time was too long and I was not sure if it will ever finish!\

### Optimizations:
After some analysis of the inputs, I found out a lot of "remaining" patterns are identical and can be calculated only once.\
So I used a recursive function to find all the possible ways of matching the input string to the pattern; with `@cache` to remember the counted ways.

**So, I think this can be a clue for other puzzles: whenever dynamic programming sounds like a possible solution, try to use a recursive function with `@cache` and see if it works!**

[TODO] I need to refine my implementation and clean it up later.

## Day 13: [Point of Incidence](https://adventofcode.com/2023/day/13)
A rather easy puzzle.\
The only trick is to do the looping correctly.

### Optimizations:
* Counting the differences between the lines was the repetitive pattern that can be simply `@cache`d. My yesterday's experience helped me to find this optimization quickly.
* For finding the reflections across columns, I rotated the mirrors by 90 degrees and then applied the same logic as the rows: `list(zip(*mirror))`. This makes the `@cache`d function to be used on both rows and columns.

## Day 14: [Parabolic Reflector Dish](https://adventofcode.com/2023/day/14)
Simulating the rolling of balls towards a direction and finding the final location of the balls.
[TODO] I need to refine my implementation and clean it up later.

### Optimizations:
* Part 2 needs a history keeping trick to find the period of repetition of ball patterns and fast-forwarding accordingly.

## Day 15: [Lens Library](https://adventofcode.com/2023/day/15)
Not my favorite type of puzzle!\
I had to read the puzzle statement several times (part 2) to understand what is going on!\
Beyond that there was nothing challenging here.

## Day 16: [The Floor Will Be Lava](https://adventofcode.com/2023/day/16)
Interesting puzzle!\
It highly depends how you optimize the solution.\
My initial implementation was to keep the history of current full state and stop if it repeats.

### Optimizations:
* Keep the history of each beam `(x, y, direction)` and eliminate the seen ones instead of keeping the history of all the beams at the same time.
* `@cache` the next state function to speed up the search.

## Day 17: [Clumsy Crucible](https://adventofcode.com/2023/day/17)
This was a typical puzzle to be solved by Dijkstra's algorithm.\
The only important trick was to avoid repetitive states by keeping the history of the visited states.\
Using a minimum heap was also a good trick to speed up the search.
Warming up on:
* `heapq`

### Optimizations:
* Simply using a `set` of visited states, since the first time you see a state (in Dijsktra's algorithm) is the shortest path to that state.

### Bugs and issues:
* I misunderstood the termination condition for the second part. The minimum straight steps was needed on the terminal state as well.

## Day 18: [Lavaduct Lagoon](https://adventofcode.com/2023/day/18)
Weakest day for me so far in AoC 2023!\
It took me a long while to find efficient solutions for today's puzzles.\
It was a very simple problem statement, counting edge and inner points of a 2D contour which can be drastically large!\
Anyways, is the hexadecimal color representation a hint for some future puzzles? :thinking: Let's prepare some util functions for it!
### Optimizations:
This was a very similar puzzle to Day 10: [Pipe Maze](https://adventofcode.com/2023/day/10).\
Using flood-fill did the job on day 10, but is not feasible for this puzzle.\
* The more efficient solution is to process each row and count the inner tiles.\
Along the row, you need to check if you're in or out of the contour and count the inner tiles accordingly.\
* And you need to avoid calculating the same pattern for similar rows (huge numbers of consecutive rows with exact same vertical lines).

### Bugs and issues:
* Using `-1` as the default value for last observed line/corner point was an issue which took me a couple of hours to fix! :sweat_smile: I was considering `value < 0` as not-yet-set, but in the actual input, we have plenty of negative values!

## Day 19: [Aplenty](https://adventofcode.com/2023/day/19)
Nice puzzle!\
It provides a list of items each with its values for 4 categories `x,m,a,s`!\
To solve part one, you need to feed each item to the set of workflows (each consists of a set of rules, based on category values) and find the finally accepted items.\
Part one makes you think about brute-forcing for part two which is apparently not feasible.\
Range operations will do the job for part two.\
After solving this puzzle, I now feel a util class of handling ranges will be handy for future puzzles.
[TODO]

### Optimizations:
* For part one, using `eval` function to evaluate the conditions was handy.
* For part two, all you need to do is to elevate the calculations to range level instead of item level.
### Bugs and issues:
* I had a bug of starting the full ranges from 0 instead of 1! :sweat_smile:


## Day 20: [Pulse Propagation](https://adventofcode.com/2023/day/20)
Simulating the propagation of pulses in a network of flip-flops and conjunction modules.\
They all work in negative logic, so it was a bit tricky to implement.\
Anyways, part one was mainly about implementing the mechanics of the molules and simulating the propagation of pulses.\
But the main challenge was in part two, for which (again) brute-force search was not feasible.\
It seems `rx` is only receiving signals from a conjunction module (layer-1), which also receives signals from a set of other conjunction modules (layer-2), which all in turn receive signals from a set of other conjunction modules (layer-3).\
Good news is that all the layer-3 conjunction modules are getting activated in a regular pattern, so we can simulate the whole thing and find the activation time for rx.\
To do so, we need to find the activation time for all the layer-3 conjunction modules and find the least common multiple of those times.

### Optimizations:
* Similar to Day 8: [Haunted Wasteland](https://adventofcode.com/2023/day/8), we need to find the least-common-multiplier of all the cycles.\

## Day 21: [Step Counter](https://adventofcode.com/2023/day/21)
Alright! Today's was a very tricky puzzle!\
The sample input is a normal example which is not feasible to solve at all with millions of steps!\
The provided input is a very specific map: the starting point is in the very center of the map, and its row and column are all `.`s.\
The first and last row and column are also all `.`s.\
So, when we calculate the distance to the starting point, the center tile in the first/last row/col is the first tile to be visited.\
And, the number of requested steps in the problem statement `26501365` is an integer multiple of the number of tiles away from the starting point: `26501365 = 65 + 131*202300`.\
This makes the solution very very specific to the input: after this number of steps, we will reach a diamond of tiles, `26501365` tiles to the top, bottom, left and right of the starting point.\
Which will be exactil `202300` full tiles to top, bottom, left and right of the starting tiles.\
One last trick is to handle even and odd tiles separately, like a chessboard!\
These assumptions, makes my solution very specific to the input, but it works efficiently with my input! :sweat_smile:

## Day 22: [Sand Slabs](https://adventofcode.com/2023/day/22)
Sand Slabs was rather an easy puzzle, in comparison to the previous ones.\
It way mainly about properly understand the puzzle statement (Jenga like mechanics) and implement it accordingly.\
My current implementation is not very efficient and needs to be optimized later. [TODO]

## Day 23: [A Long Walk](https://adventofcode.com/2023/day/23)
This one took a very long time from me to optimize (part two).\
The problem is simply finding the longest path (with no revisiting nodes) between two nodes in a graph with cycles.\
The time I submitted my solution, my code was still running trying to find longer paths!\
The naive way to solve this is to start from the staring point and find all the possible neighbors to move to and search in a DFS way with backtracking to find the longest path.

### Optimizations:
* The first and most important optimization is to avoid the corridor nodes (nodes with only two neighbors).\
When we have `a <-> b <-> c`, we can simply remove `b` and consider `a <-> c` with distance `2`.\
This was the main trick to solve part two.
* The second optimization is to check if there's a single final path to the end point, and consider that one instead as the end point.\
This avoids the paths with this final node in their early steps and makes the search faster.
### Bugs and issues:
* I spent a very long time thinking about a dynamic programming solution, but I couldn't find one.\
It seems impossible to find the longest path in a graph with cycles using dynamic programming.\
Brute-force is the only possible way!?

## Day 24: [Never Tell Me The Odds](https://adventofcode.com/2023/day/24)
First challenge was to read and understand the puzzle statement!\
In part one, for each pair of hailstones, we need to find the 2D intersection the two linear trajectories:
* `x = x1 + dx1 * t1 = x2 + dx2 * t2`
* `y = y1 + dy1 * t1 = y2 + dy2 * t2`
  
Using `sympy` to find `t1` and `t2` (and the `x`, `y` accordingly) made the implementation very easy, yet not very efficient.\
The rest will be to check the values of `x, y, t1, t2` to be in the expected ranges.
For part two, we need to find `6` parameters (`x, y, z, dx, dy, dz`), and a `t[i]` for each hailstone, which is a system of linear equations, and can be solved again using `sympy`.

### Optimizations:
* For part one, we can solve analytically for a way more efficient solution:
$$
  x_1+t_1dx_1 = x_2+t_2dx_2 \Rightarrow t_1 = \frac{x_2-x_1+t_2dx_2}{dx_1}\\
  y_1+t_1dy_1 = y_2+t_2dy_2 \Rightarrow t_2 = \frac{y_1-y_2+t_1dy_1}{dy_2}\\
  \therefore\\
  t_1 = \frac{\frac{x_2}{dx_1} - \frac{x_1}{dx_1} + \frac{(y_1 - y_2) dx_2}{dx_1 dy_2}}{\frac{1 - dy_1 dx_2}{dy_2 dx_1}}\\
  t_2 = \frac{y_1 - y_2 + t_1 dy_1}{dy_2}\\
  x = x_1 + t_1 dx_1\\
  y = y_1 + t_1 dy_1\\
$$
* For part two, instead of solving all the equations for all the hailstones (which takes forever), we can check if we can find a unique solution using first 3 hailstones.\
We have `6+n` unknowns and `3n` equations, considering `n` hailstones.\
So in a well-defined system we should be able to solve with only `3` hailstones.\
And if not well-defined, we can try with more hailstones!

## Day 25: [Title](https://adventofcode.com/2023/day/25)
Alright, after trying some brute-force search, I realized the solution is nothing but a classic minimum-cut algorithm!\
So, let's try some library functions to solve it!\
I tried `minimum_cut` function from `networkx` library and it did the job.
Should I try to implement it myself? :thinking:\ [TODO]