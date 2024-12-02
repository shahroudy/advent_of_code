# Advent of Code 2024

## Day 1: [Historian Hysteria](https://adventofcode.com/2024/day/1) &rarr; [Solution](./day01/d01.py)
Typical day 1 problem, we are provided with two columns of numbers and we need to find:
* sum of distances between the corresponding numbers in the sorted columns.
* sum of values of left column numbers, each multiplied by the number of occurrences in the right column.

## Day 2: [Red-Nosed Reports](https://adventofcode.com/2024/day/2) &rarr; [Solution](./day02/d02.py)
We are given a list of numbers (a report of multiple levels) in each input line and we need to find how many are safe.\
The criteria for the report to be safe is:
* It must be either strictly increasing or strictly decreasing.
* The difference between adjacent numbers must be between 1 and 3.\
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