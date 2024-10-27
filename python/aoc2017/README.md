# Advent of Code 2017
## Day 1: [Inverse Captcha](https://adventofcode.com/2017/day/1) &rarr; [Solution](./day01/d01.py)
Warming up on:
* looping
* list indexing
### Bugs and issues:
* not reading the text precisely: 
  * for the first puzzle I missed the circularity of the list
  * for the second one I misunderstood the target of the comparison being only one item

## Day 2: [Corruption Checksum](https://adventofcode.com/2017/day/2) &rarr; [Solution](./day02/d02.py)
Warming up on:
* list operations
* regular expressions
  * `\s` pattern for whitespace
* code factoring 
* `is_integer()` function

## Day 3: [Spiral Memory](https://adventofcode.com/2017/day/3) &rarr; [Solution](./day03/d03.py)
Nice and simple spatial map generation via looping.

### Bugs and issues:
* I started with an efficient formula for the first part that took me a long time to solve.
But the proper solution was to actually build the map :laughing:
* Writing a help function to print the map, I again mixed the directions 
(order of the indices `x`, `y`)

## Day 4: [High-Entropy Passphrases](https://adventofcode.com/2017/day/4) &rarr; [Solution](./day04/d04.py)
Warming up on:
* `set`
* `tuple`
* `collections.Counter`
* `list.sort` with custom `key`s

## Day 5: [A Maze of Twisty Trampolines, All Alike](https://adventofcode.com/2017/day/5) &rarr; [Solution](./day05/d05.py)
Warming up on:
* Reusing input `list`s
* `list` indices
* Using and updating a variable at the same step!

## Day 6: [Memory Reallocation](https://adventofcode.com/2017/day/6) &rarr; [Solution](./day06/d06.py)
Warming up on:
* `list` 
  * `max(list)`
  * `list.index()`
* `tuple`
* `set`
* `dict`

## Day 7: [Recursive Circus](https://adventofcode.com/2017/day/7) &rarr; [Solution](./day07/d07.py)
Warming up on:
* regular expressions for reading inputs
* `collections.deque` for building a queue 
* `collections.Counter` for finding the frequency of items in a list

## Day 8: [Heard You Like Registers](https://adventofcode.com/2017/day/8) &rarr; [Solution](./day08/d08.py)
Warming up on:
* `eval()` function
* regular expressions
### Optimizations:
* using `eval()` function!
### Bugs and issues:
* Using `eval(exp, variable_dict)` will add an unwanted `__builtins__` key to the `variable_dict`
  * Solution is to use `eval(exp, None, variable_dict)` since the second argument is the `globals` and the third is actually the `locals`.
  * This unwanted key/value pair was preventing me from finding `max(variable_dict.values())` easily!

## Day 9: [Stream Processing](https://adventofcode.com/2017/day/9) &rarr; [Solution](./day09/d09.py)
Simple "Stream Processing" exercise.
The only important aspect of this day was to implement the proper order of the rules.
### Bugs and issues:
* My first quick implementation for the second part was missing the `<`s inside garbage sections.

## Day 10: [Knot Hash](https://adventofcode.com/2017/day/10) &rarr; [Solution](./day10/d10.py)
Long unnecessary story to read :laughing:
Warming up on:
* `collections.deque`
* Usage of `stack` for reversing the order items
* `deque.rotate`
* `hex()` function
* `str.rjust` function

## Day 11: [Hex Ed](https://adventofcode.com/2017/day/11) &rarr; [Solution](./day11/d11.py)
Finally a puzzle that needs some thinking to solve; yet easy one.\
It's all about thinking how to aggregate hex steps.\
As soon as you figure out how, the problem is solved!

## Day 12: [Digital Plumber](https://adventofcode.com/2017/day/12) &rarr; [Solution](./day12/d12.py)
An easy connected-components of a graph problem.
### Optimizations:
* Of course, using sets
* Since inputs are only numbers, `re.findall(r"\d+", line)` easily extracts the numbers

## Day 13: [Packet Scanners](https://adventofcode.com/2017/day/13) &rarr; [Solution](./day13/d13.py)
Another easy puzzle.\
All you need to do is to simulate the described scenario, with a small optimization.
### Optimizations:
* No full path of the security scanner needs to be simulated. Every `(depth-1)*2` picoseconds, the 
  scanner is back to the top of the layer and can catch us.

## Day 14: [Disk Defragmentation](https://adventofcode.com/2017/day/14) &rarr; [Solution](./day14/d14.py)
The puzzle was to reuse the Knot Hash from Day 10.\
The only thing to do is to generate the 128 hashes and count the number of `1`s in them.\
For part 2, we  need to find the number of connected components (`1`s) in the grid of `0`s and `1`s.\
To do so, I stored all the locations of `1`s in a set and iterated over them to find the connected components.
### Bugs and issues:
* While turning the hash to binary, I forgot to add the leading zeros to the binary representation, which led to wrong locations of `1`s.

## Day 15: [Dueling Generators](https://adventofcode.com/2017/day/15) &rarr; [Solution](./day15/d15.py)
A modulus multiplication problem.\
There are two generators that generate numbers based on the previous number with different factors in the same modulus.\
And we need to count the number of pairs that have matching 16 least significant bits.\
The second part is to find the number of pairs that have matching 16 least significant bits after 5 million iterations.\
But this time each generator will generate the first number which is divisible by a specific number (4 for A and 8 for B).\
The solution was to simply implement the generators and count the number of matching pairs.

### Optimizations:
* Instead of using `%16` or `bin()` function, we can speed up by using `&0xFFFF` to get the 16 least significant bits.
* I spent some time trying to find a better solution using the modulus properties, but I couldn't find any :sweat_smile:. The ad-hoc solutions run in about 10 seconds, which is acceptable.

## Day X: [Title](https://adventofcode.com/2017/day/X)
Desc
### Optimizations:
### Bugs and issues: