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

## Day 5: [How About a Nice Game of Chess?](https://adventofcode.com/2016/day/5) &rarr; [Solution](./day05/d05.py)
MD5 hash mining.\
It's very similar to AoC 2015 Day 4.\
Nothing fun in looping over hash values.

## Day 6: [Signals and Noise](https://adventofcode.com/2016/day/6) &rarr; [Solution](./day06/d06.py)
Finding the most common and least common characters at each position in a list of strings.\
* `collections.Counter` to count the characters in each position.
* [`Counter.most_common()`](https://docs.python.org/3/library/collections.html#collections.Counter.most_common) to get the sorted tuples of characters and their counts.

## Day 7: [Internet Protocol Version 7](https://adventofcode.com/2016/day/7) &rarr; [Solution](./day07/d07.py)
Playing with patterns like `ABBA` and `ABA` in strings.\
This was a fun puzzle to solve with `re` (regular expressions) library tools.

Specifically, to find the `ABBA`s, I used:
`re.search(r"(?=(\w)(?!\1)(\w)\2\1)", s)`.
* `(?=...)` is a positive lookahead assertion, which matches the pattern but doesn't consume the string; which is needed to catch all the overlapping patterns.
* `(?!\1)` is a negative lookahead assertion, which matches if the next character is not the same as the first one.

And for the `ABA`s, I used:
* `re.findall(r"(?=(\w)(?!\1)(\w)\1)", s)`

## Day 8: [Two-Factor Authentication](https://adventofcode.com/2016/day/8) &rarr; [Solution](./day08/d08.py)
An easy puzzle of rotating values in a 2D grid.\
I used a dictionary to represent the grid and rotated the values in the grid by copying the values to a buffer list.

## Day 9: [Explosives in Cyberspace](https://adventofcode.com/2016/day/9) &rarr; [Solution](./day09/d09.py)
A puzzle of expanding strings based on two different versions (parts 1 and 2).\
The only mistake one can do here is to try to really expand the strings, which is not necessary.\
All we need to do is to implement a recursive function to calculate the length of the expanded strings, with two different versions.


## Day X: [Title](https://adventofcode.com/2016/day/X) &rarr; [Solution](./dayXX/dXX.py)
Desc
### Optimizations:
### Bugs and issues: