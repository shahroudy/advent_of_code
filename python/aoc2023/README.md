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
For part two, my trick was to up-sample the map by a factor of 2 and then apply a region growing to detect all the outer points.\
Then finding the inner ones is obvious.
### Bugs and issues:
 Missing the point about the start point `S` is actually a simple connection that you should guess based on its neighbors.\
  My first implementation was assuming all the neigbors of `S` are connected to it!\
  It took me about an hour to figure this out! :sweat_smile:

## Day 11: [Cosmic Expansion](https://adventofcode.com/2023/day/11)
This ones was easy; the efficient implementation was actually easier than the brute force one!\
Keeping track of missing rows and columns and derive a mapping of indices according to the expansion factor was the key here.\
After some cleanup, my whole solution is ~30 lines of code yet very efficient in Python!

## Day X: [Title](https://adventofcode.com/2023/day/X)
Desc
### Optimizations:
### Bugs and issues: