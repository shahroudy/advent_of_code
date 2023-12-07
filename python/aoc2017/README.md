# Advent of Code 2017
## Day 1: [Inverse Captcha](https://adventofcode.com/2017/day/1)
Warming up on:
* looping
* list indexing
### Bugs and issues:
* not reading the text precisely: 
  * for the first puzzle I missed the circularity of the list
  * for the second one I misunderstood the target of the comparison being only one item

## Day 2: [Corruption Checksum](https://adventofcode.com/2017/day/2)
Warming up on:
* list operations
* regular expressions
  * `\s` pattern for whitespace
* code factoring 
* `is_integer()` function

## Day 3: [Spiral Memory](https://adventofcode.com/2017/day/3)
Nice and simple spatial map generation via looping.

### Bugs and issues:
* I started with an efficient formula for the first part that took me a long time to solve.
But the proper solution was to actually build the map :laughing:
* Writing a help function to print the map, I again mixed the directions 
(order of the indices `x`, `y`)

## Day 4: [High-Entropy Passphrases](https://adventofcode.com/2017/day/4)
Warming up on:
* `set`
* `tuple`
* `collections.Counter`
* `list.sort` with custom `key`s

## Day 5: [A Maze of Twisty Trampolines, All Alike](https://adventofcode.com/2017/day/5)
Warming up on:
* Reusing input `list`s
* `list` indices
* Using and updating a variable at the same step!

## Day 6: [Memory Reallocation](https://adventofcode.com/2017/day/6)
Warming up on:
* `list` 
  * `max(list)`
  * `list.index()`
* `tuple`
* `set`
* `dict`

## Day 7: [Recursive Circus](https://adventofcode.com/2017/day/7)
Warming up on:
* regular expressions for reading inputs
* `collections.deque` for building a queue 
* `collections.Counter` for finding the frequency of items in a list

## Day 8: [Heard You Like Registers](https://adventofcode.com/2017/day/8)
Warming up on:
* `eval()` function
* regular expressions
### Optimizations:
* using `eval()` function!
### Bugs and issues:
* Using `eval(exp, variable_dict)` will add an unwanted `__builtins__` key to the `variable_dict`
  * Solution is to use `eval(exp, None, variable_dict)` since the second argument is the `globals` and the third is actually the `locals`.
  * This unwanted key/value pair was preventing me from finding `max(variable_dict.values())` easily!

## Day 9: [Stream Processing](https://adventofcode.com/2017/day/9)
Simple "Stream Processing" exercise.
The only important aspect of this day was to implement the proper order of the rules.
### Bugs and issues:
* My first quick implementation for the second part was missing the `<`s inside garbage sections.

## Day 10: [Knot Hash](https://adventofcode.com/2017/day/10)
Long unnecessary story to read :laughing:
Warming up on:
* `collections.deque`
* Usage of `stack` for reversing the order items
* `deque.rotate`
* `hex()` function
* `str.rjust` function

## Day 11: [Hex Ed](https://adventofcode.com/2017/day/11)
Finally a puzzle that needs some thinking to solve; yet easy one.\
It's all about thinking how to aggregate hex steps.\
As soon as you figure out how, the problem is solved!

## Day 12: [Digital Plumber](https://adventofcode.com/2017/day/12)
An easy connected-components of a graph problem.
### Optimizations:
* Of course, using sets
* Since inputs are only numbers, `re.findall(r"\d+", line)` easily extracts the numbers

## Day 13: [Packet Scanners](https://adventofcode.com/2017/day/13)
Another easy puzzle.\
All you need to do is to simulate the described scenario, with a small optimization.
### Optimizations:
* No full path of the security scanner needs to be simulated. Every `(depth-1)*2` picoseconds, the 
  scanner is back to the top of the layer and can catch us.

## Day X: [Title](https://adventofcode.com/2017/day/X)
Desc
### Optimizations:
### Bugs and issues: