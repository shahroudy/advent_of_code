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

## Day 16: [Permutation Promenade](https://adventofcode.com/2017/day/16) &rarr; [Solution](./day16/d16.py)
A string manipulation problem.\
We start with a string of characters and we need to apply a series of operations on it including:\
* `s` shift the programs (characters in the string) rotationally
* `x` swap two programs in the two input positions
* `p` swap the programs with two input values.
In part one, we need to apply the operations in the input order only once; which is doable in a fraction of a second.\
In part two, we need to apply the operations in the input order 1 billion times; which is not doable in a reasonable time.\
### Optimizations:
* The order of the programs is cyclic, so we can find the cycle length and apply the operations only the remaining times by fast-forwarding the operations.

## Day 17: [Spinlock](https://adventofcode.com/2017/day/17) &rarr; [Solution](./day17/d17.py)
An interesting puzzle to solve.\
We have a circular list (starting at [0]) and we need to insert numbers in it based on an input step size.\
At each step, we move forward the step size and insert the number after the current position.\
The first part is to find the number after 2017 when it's inserted.\
The ad-hoc solution of keeping the list as a `list` was good enough for part one.\
For part two, we need to find next value to `0` but after 50 million steps.\
The ad-hoc solution is not more tractable, so we need to find a better solution.\
### <b>Optimizations:
* First improvement was to switch to a `deque` instead of a `list` to have O(1) insertion time. `deque` can rotate the list very efficiently; This can give us the answer in about 10 seconds.
* We don't need to keep the whole list for this part :smile:, we can keep only the current position and the value after `0`. This speeds up the solution to about a couple of seconds.</b>

## Day 18: [Duet](https://adventofcode.com/2017/day/18) &rarr; [Solution](./day18/d18.py)
An interesting puzzle to simulate concurrently running programs.\
In part two we have two programs that run concurrently and communicate with each other.\
The solution was to simulate the programs and their communication.\
Python's generators seemed to be a good fit for this problem.

## Day 19: [A Series of Tubes](https://adventofcode.com/2017/day/19) &rarr; [Solution](./day19/d19.py)
A simple path following problem.\
We have a map of signs and we need to follow a path starting from the top row, catch all the alphabets and count the number of steps.\
The only twist is that we need to follow the path in the direction of the arrow, and turn when we reach a `+` sign.

## Day 20: [Particle Swarm](https://adventofcode.com/2017/day/20) &rarr; [Solution](./day20/d20.py)
A simple physics simulation problem.\
We have a list of particles with their positions, velocities, and accelerations, and need to simulation their movement over time.\
For part one, we need to find the particle that stays closest to the origin in the long run.\
For part two, we need to find the number of particles that do not collide with others.\
The ad-hoc way of simulating the particles for a long time (1000 iterations) was good enough for both parts.\
But one can analytically solve the quadratic equation to find the time of collision for part two.\
Anyways, the analytical solution will not necessarily faster than the ad-hoc one, and it will be way more complex, because the colliding particles should be immediately removed from the list.

## Day 21: [Fractal Art](https://adventofcode.com/2017/day/21) &rarr; [Solution](./day21/d21.py)
In this puzzle, we are provided with a set of expansion rules for inner grids of a grid.\
Based on the size of the whole grid, we either expand each 2x2 grid to a 3x3 grid, or each 3x3 grid to a 4x4 grid.\
We need to apply the rules for a number of iterations and count the number of `#`s in the final grid.\
The only effective optimization was to store the rules in a dictionary to speed up the lookup.\
To implement the mechanics of the puzzle, we can either use a simple list of strings or a `numpy` array.\
It's good to recall the useful `numpy` structures and functions for such puzzles:
* `np.ndarray`
* `np.rot90`
* `np.flipud`
* `np.fliplr`
* `np.concatenate`
* `np.split`
* `np.hsplit`
* `np.vsplit`
* `np.hstack`
* `np.vstack`
* `np.reshape`
* `np.sum`

## Day 22: [Sporifica Virus](https://adventofcode.com/2017/day/22) &rarr; [Solution](./day22/d22.py)
A simple cellular automata problem.\
We start with a grid of clean/infected cells and a virus career that moves based on the current cell state.\
In part two, we have 4 states instead of two.

## Day 23: [Coprocessor Conflagration](https://adventofcode.com/2017/day/23) &rarr; [Solution](./day23/d23.py)
Another assembly-code simulation problem.\
Part 1 was to run the code in normal mode and count the number of times the `mul` instruction is executed.\
Part 2 was to run the code in debug mode (set register `a` to 1) and get the final value of register `h`, which apparently runs for a very long time.

### Bugs and issues:
* <b>In the first part, I was checking the arguments if they are `is_numeric()` to distinguish between registers and values.\
This fails when we have a negative value.</b>\
So I had to change it to check if the value is a key in the registers' dictionary instead, which is more robust.
* At some of the steps, I was misinterpreting the subtracting of a negative value as a decrement operation, which was wrong.

### Optimizations:
As expected, for part 2 we had to translate the assembly code to higher level instructions and understand what it does.\
The code was actually counting the non-prime numbers in a defined range and with a defined step, in its most inefficient way.\
Registers:
  * `a` is the input switch for debug mode
  * `b` is the loop counter
  * `c` is the range upper bound
  * `d` and `e` are the inner loop counters to find the divisors for current `b` value
  * `f` is the flag to indicate if the current `b` value is prime
  * `g` is mainly used to build jump conditions
  * `h` is the counter for non-prime numbers in the range
This way we should re-implement the logic in its efficient way to get the answer in a reasonable time.
