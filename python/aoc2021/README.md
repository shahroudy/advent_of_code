# Advent of Code 2021

## Day 1: [Sonar Sweep](https://adventofcode.com/2021/day/1) &rarr; [Solution](./day01/d01.py)
We are provided with a list of integers (as depth levels) and we need to find:
* Part 1: How many times we have an increase in depth level.
* Part 2: How many times we have an increase in the sum of 3 consecutive depth levels.

### Optimizations:
* In part 2, one can simply find the number of times `depths[i+3] > depths[i]`.

## Day 2: [Dive](https://adventofcode.com/2021/day/2) &rarr; [Solution](./day02/d02.py)
We are provided with a list of pairs of directions and values.\
Directions are `forward`, `down`, and `up`.\
In part 1, we move in 2D based on the directions and values.\
In part 2, `up` and `down` only move an "aim" value, and `forward` moves based on the value horizontally, and based on the value multiplied by the "aim" vertically.\
In both parts, we need to calculate the `x*y` of the final position.\
Use of the internal library classes of `Point2D` and `Point3D` helped here.\
In part 2, we can use the `Point3D` class to keep track of the position and the aim.

## Day 3: [Binary Diagnostic](https://adventofcode.com/2021/day/3) &rarr; [Solution](./day03/d03.py)
We are provided with a list of binary numbers.\
In part 1 we need to find the number consisting of most common bits at each position, multiplied by the number consisting of least common bits.\
In part 2, we need to iteratively find the most common bit and filter the list and only keep the numbers that have that bit at that position.\
We iterate until we have only one number left, and that would be the result.\
In the case of equal counts, `1` is picked.\
Similarly we find the result for least common bit (picking `0` on equal counts).\
And then multiply these two together to get the final answer.

One can use the `Counter` class from the `collections` module to find the most and least common bits.\
I preferred to implement the logic myself, mainly using `str` values directly.

### Optimizations:
* In part 1, the least common bits are actually the complement of the most common bits, so we don't need to calculate them separately.