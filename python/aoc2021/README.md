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