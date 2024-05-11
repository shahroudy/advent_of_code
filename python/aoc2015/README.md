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

## day 9: [All in a Single Night](https://adventofcode.com/2015/day/9)
The puzzle was about finding the shortest (part one) and the longest (part two) path between a set of cities, passing all of them.\
The ad-hoc solution was to use the `itertools.permutations` to generate all the possible paths and calculate the distances.\
Regarding the size of the input file, this solution was efficient enough and I have not spent time to find a more efficient algorithm.

## Day 10: [Elves Look, Elves Say](https://adventofcode.com/2015/day/10)
Iterative conversion of a sequence of numbers based on the repetition of the numbers in a row.\
The ad-hoc solution that is not efficient is to build the sequence as a string at each step.

### Optimizations:
* Operate over `list` of `int` instead of `str` to avoid the overhead of string operations!.\
  I was looking for more sophisticated optimizations and did not think of this simple one for a long time.

## Day 11: [Corporate Policy](https://adventofcode.com/2015/day/11)
Applying some conditions to a string, counting on the string characters and finding the next valid password.\
Nothing very challenging, the ad-hoc solution is still efficient enough.

## Day 12: [JSAbacusFramework.io](https://adventofcode.com/2015/day/12)
Warm-up on:
* Usage of `re` to find all numbers (positive and negative) by using the pattern `r"-?\d+"` 
* Parsing JSON input using `json.loads` 

## Day 13: [Knights of the Dinner Table](https://adventofcode.com/2015/day/13)
Finding the optimum seating arrangement for a group of people based on their happiness with regards to their neighbors.\
Since the number of guests are few in both the sample and the puzzle input, the brute-force solution is efficient enough.\
Warm-up on:
* Reading inputs with `re`
* `collections.defaultdict` for storing the happiness
* `itertools.permutations` to generate all the possible seating arrangements

### Optimizations:
* Fixing the first seat and loop over the permutations of the rest of the guests; since the seating arrangement is circular.

## Day 14: [Reindeer Olympics](https://adventofcode.com/2015/day)
Comparing the distances a group of reindeers fly after a certain time.\
Each raindeer has a speed and a time for which it can fly at that speed, and a rest time.\
In part two we need to simulate each second and calculate the distance of each reindeer to find the winner for each second.\
Still not a challenging puzzle, the ad-hoc looping is efficient enough.

## Day 15: [Science for Hungry People](https://adventofcode.com/2015/day/15)
Yet another puzzle with efficient enough brute-force solution.\
I honestly believe brute-force is preferred when the input size is small enough, since the implementation is simpler.\
The only challenge here was to dynamically loop over possible values of the ingredients and calculate the score; since the number of ingredients were not equal between the sample and the puzzle input.

## Day 16: [Aunt Sue](https://adventofcode.com/2015/day/16)
Finding the aunt Sue that matches the given criteria, in the input list of aunt Sue's.\
Nothing challenging again.

## Day 17: [No Such Thing as Too Much](https://adventofcode.com/2015/day/17)
Finding the number of combinations in the input list that sum up to a certain value.\
Warm-up on:
* `itertools.combinations` to generate all the possible combinations of a list

## Day 18: [Like a GIF For Your Yard](https://adventofcode.com/2015/day/18)
A simple cell-automaton puzzle, to simulate the lights on a grid.\
Warm-up on:
* Map reading and parsing
* `collections.defaultdict` for storing the grid

## Day 19: [Medicine for Rudolph](https://adventofcode.com/2015/day/19)
We are provided with a set of replacement rules and a string (medicine molecule).\
In the first part, we need to find the number of unique molecules derivable from the medicine molecule by applying single replacement rules.\
The only trick here is to keep a set of derivable molecules to avoid counting the same molecule multiple times.\
In the second part, we need to find the minimum number of steps to reach the medicine molecule from the starting molecule (`e`).\
The solution is to apply the replacement rules in reverse order and count the steps.\
We also need to have the replacement rules sorted by the length of the replacement string.

## Day 20: [Infinite Elves and Infinite Houses](https://adventofcode.com/2015/day/20)
Alright, it took 20 days to see a puzzle that needs some optimization.\
We have infinite houses and infinite elves delivering presents to them.\
The puzzle is about finding the first house that receives at least a certain number of presents.\
In the first part, we need to find an efficient way of finding all the factors of a number and sum them up.\
It took me a while to figure out you can find all the factors of a number by iterating over the numbers up to the square root of the number and find the remaining factor by dividing the number by the current factor.\
In the second part, we need to find the first house that receives at least a certain number of presents, but this time each house can receive presents from 50 houses.\
My solution was to count till 50 and consider the quotient for summation.\
And of course, for both parts, we can divide the minimum present number by the number of presents each elf can deliver to reduce the search space.

## Day 21: [RPG Simulator 20XX](https://adventofcode.com/2015/day/21)
Simulating a fight between a player and a boss.\
There are various possible weapons, armors, and rings to equip with.\
Only and only one weapon, at most one armor, and at most two rings can be bought, each for a predefined cost.\
The question is to find the minimum cost to win the fight, and the maximum cost to lose it.\
My solution was to find possible combinations for each type and then iterate over all the possible combinations to find the minimum and maximum costs.\
Warm-up on:
* `itertools.combination`
* `itertools.product`

## Day X: [Title](https://adventofcode.com/2015/day/X)
desc
### Optimizations:
### Bugs and issues:
