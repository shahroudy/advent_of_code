# Advent of Code 2015

## Day 1: [Not Quite Lisp](https://adventofcode.com/2015/day/1)
The very first challenge in AoC history was not something challenging.\
You need to simply read the input and count the number of `(` and `)` and return the difference.\
The second part is to find the position where the first time the current floor becomes negative.
Warming up on:
* Reading input from file
* For loop?!

## Day 2: [I Was Told There Would Be No Math](https://adventofcode.com/2015/day/2)
Another simple puzzle.\
Calculating the area and the volume of a box and summing them up.\
Warming up on:
* List comprehension
* Sort operation

## Day 3: [Perfectly Spherical Houses in a Vacuum](https://adventofcode.com/2015/day/3)
Another simple puzzle.\
Reading the input directions and count the number of unique houses visited.\
Second part needs to unzip the input moves to two sets and count the unique houses visited together.\
Warming up on:
* `set`
* `list` slicing

## Day 4: [The Ideal Stocking Stuffer](https://adventofcode.com/2015/day/4)
Mining the MD5 hash codes to find the first hash starting with 5 (6 in part 2) zeros.\
Using `hashlib` to calculate the MD5 hash simplifies the solution drastically.
### Possible Optimizations (not implemented):
* One can think of implementing the actual MD5 algorithm to optimize the solution, by caching the states of the four words for the repeated input patterns.
* Multiprocessing can be used to calculate the hashes in parallel.

## Day 5: [Doesn't He Have Intern-Elves For This?](https://adventofcode.com/2015/day/5)
Checking the input strings for different patterns and decide if they are "nice" or "naughty".\
A perfect example for using regular expressions:
  ```python 
    import re

    re.search(r"(.)\1", s)
    # Contains at least three vowels (`aeiou` only): 
    len(re.findall(r"[aeiou]", s)) >= 3
    
    # Contains at least one letter that appears twice in a row: 
    re.search(r"(.)\1", s)

    # Does not contain the strings `ab`, `cd`, `pq`, or `xy`:
    not re.search(r"ab|cd|pq|xy", s)

    # Contains a pair of any two letters that appears at least twice in the string without overlapping: 
    re.search(r"(..).*\1", s) 

    # Contains at least one letter which repeats with exactly one letter between them, like `xyx`, `efe`, or even `aaa`: 
    re.search(r"(.).\1", s)
```

## Day 6: [Probably a Fire Hazard](https://adventofcode.com/2015/day/6)
An easy yet fun-to-optimize puzzle, to turn on/off and toggle the lights on a grid.\
The brute-force solution is to use `defaultdict` for keeping the values of the lights (both parts) and loop over the grid and apply the instructions.
### Optimizations:
* Using `numpy` to represent the grid and apply the instructions in a vectorized way.
* Considering 2-dimensional ranges with their areas will definitely improve the performance, but the implementation will be more complex and seems to be an overkill for this simple puzzle.

## Day 7: [Some Assembly Required](https://adventofcode.com/2015/day/7)
Simulation of a network of wires and gates.\
Values on the wires are 16-bit unsigned integers.\
The first part is to simulate the network and find the value on the wire `a`.\
In python one can simply use `~, &, |, <<, >>` operators to simulate not, and, or, left shift, and right shift gates respectively.\
The only tricky part was to implement the `NOT` gate, sine `~` operator in python turns positive numbers to negative and vice versa.\
The solution was to use `&0xff` to mask the result to 16-bit unsigned integer.\
The input was not sorted and some operations had to wait till the values of its input wires are calculated.

## Day 8: [Matchsticks](https://adventofcode.com/2015/day/8)
This puzzle was mainly about understanding the functionality of escape characters in a string.\
In the first part we need to count the difference between the lengths of the input strings (with escape characters) and the actual strings.\
For this, using the `eval` function was very handy.\
In the second part, we need to count the difference between the lengths of the strings before and after escaping the special characters in the original strings.\
My implementation were one-liners in python for each section:\
```python
def extra_chars_from_string_literals(self):
    return sum(len(text) - len(eval(f"'{text[1:-1]}'")) for text in self.input)

def extra_chars_from_encoding(self):
    return sum(2 + text.count("\\") + text.count('"') for text in self.input)
```

## Day X: [Title](https://adventofcode.com/2015/day/X)
desc
### Optimizations:
### Bugs and issues:
