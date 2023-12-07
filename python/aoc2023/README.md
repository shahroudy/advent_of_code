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
Part two was the challenge, running the mappings on all the input ranges was impossible.
### Optimizations:
* My current implementation was to iterate over the locations from 0 (since we need to find the minimum) and apply the reverse mappings to check if the initial seed was in the list or not.
* This was very slow (13 minutes on my computer), so I'm still thinking there should be a better way to do this in range level! [TODO]

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

## Day X: [Title](https://adventofcode.com/2023/day/X)
Desc
### Optimizations:
### Bugs and issues: