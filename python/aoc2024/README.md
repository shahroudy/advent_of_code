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
* Using `functools.cmp_to_key` to convert the comparison function to a key function for sorting and is super handy here.