# Advent of Code 2016

## Day 1: [No Time for a Taxicab](https://adventofcode.com/2016/day/1) &rarr; [Solution](./day01/d01.py)
Simple rotation and moving implementation.\
Good to recall the rotation formula; 
when you rotate left: `dx, dy = dy, -dx`
and when you rotate right: `dx, dy = -dy, dx`
### Bugs and issues:
* The only tricky point in this puzzle was to consider all the positions on the way of each step in the visited positions and not only the final position (for part 2)

## Day 2: [Bathroom Security](https://adventofcode.com/2016/day/2) &rarr; [Solution](./day02/d02.py)
A simple moving on the map puzzle.\
Warming up on:
* `dict`
* reading input files

## Day 3: [Squares With Three Sides](https://adventofcode.com/2016/day/3) &rarr; [Solution](./day03/d03.py)
A simple checking of triangle rule puzzle.\
In the first part I need to check the values horizontally, and in the second part I need to check the values vertically.

### Bugs and issues:
* In my first try, I sorted the vertical values in-place and ruined the original order.

## Day 4: [Security Through Obscurity](https://adventofcode.com/2016/day/4) &rarr; [Solution](./day04/d04.py)
A simple puzzle of counting and shifting the characters in strings.
* `collections.Counter` to count the characters in the string.
* `ord()` and `chr()` to shift the characters.



## Day X: [Title](https://adventofcode.com/2016/day/X) &rarr; [Solution](./dayXX/dXX.py)
Desc
### Optimizations:
### Bugs and issues: