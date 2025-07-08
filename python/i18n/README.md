# Internationali­zation Puzzles (https://i18n-puzzles.com/)

## Day 1: [Length limits on messaging platforms](https://i18n-puzzles.com/puzzle/1/) &rarr; [Solution](./day01/d01.py)
Understanding the difference between the `length` of a string and its size in `bytes` on `utf8` encoding.\
To solve this puzzle, we can simply encode each line of the input file to `utf8` and check its length.\
To do so, we have `.encode("utf-8")` function in `str` class in python.


## Day 2: [Detecting gravitational waves](https://i18n-puzzles.com/puzzle/2/) &rarr; [Solution](./day02/d02.py)
This puzzle is all about understanding the timezones and how to convert them to `UTC` time.\
We are provided with a list of local times (in `2019-06-05T08:15:00-04:00` format) and need to find the most frequent time, in `UTC` timezone.\
Useful libraries, functions and tools:
* `datetime` module in python
    * `datetime` class in `datetime` module provides a type for date and time.
    * `datetime.strptime` function can be used to parse a string to a `datetime` object.
        * It uses an input format `str` to define how to parse inputs.
        * For this puzzle, the input format is `"%Y-%m-%dT%H:%M:%S%z"`.
    * `datetime.strftime` function can be used to format a `datetime` object to a string.
        * It uses an output format `str` to define how to format the output.
        * For this puzzle, the output format is `"%Y-%m-%dT%H:%M:%S%:z"`.
            * Note, the `"%:z"` format is used to include the timezone delta in the output.
    * `datetime.astimezone()` function can be used to convert a `datetime` object to a specific timezone.
        * It takes a timezone object as an argument.
        * In this puzzle, the needed timezone is `datetime.UTC`.
    * `datetime.timestamp()` function can be used to get the timestamp of a `datetime` object.
    * `datetime.fromtimestamp()` function can be used to get a `datetime` object from a timestamp.
        * As the second argument, it can take a timezone object to convert the timestamp to a specific timezone. In this puzzle, the needed timezone is `datetime.UTC`.
* `collections.Counter` class in python was handy to find the frequency of each time.
    * `Counter.most_common()` function can be used to find the most common elements in a list.

## Day 3: [Unicode Passwords](https://i18n-puzzles.com/puzzle/3/) &rarr; [Solution](./day03/d03.py)
We have a list of unicode passwords and need to find the one that is valid.\
A valid password is at least 4 and at most 12 characters, has at least one digit, one lowercase, one uppercase, and one accented letter.\
To find the the accented letters, I simply used `ord(ch) >= 128` condition; maybe this will be proved to be a naive solution in future days, but was enough for this puzzle. By the way, one may need to consider the char to be `ch.isalpha()` as well.

## Day 4: [A trip around the world](https://i18n-puzzles.com/puzzle/4/) &rarr; [Solution](./day04/d04.py)
We have a list of departure and arrival date/time of a series of flights and need to find the total flight time.\
The key to solve this puzzle is to:
* Parse the date/time strings to `datetime` objects.
* Used `ZoneInfo` class in `zoneinfo` module to get the timezone information.
* Replace the timezone of each `datetime` object with the proper timezone.
* Calculate the difference between the arrival and departure time.
In short: 
```python
datetime.strptime(t, "%b %d, %Y, %H:%M").replace(tzinfo=ZoneInfo(c))
```

## Day 5: [Don't step in it...](https://i18n-puzzles.com/puzzle/5/) &rarr; [Solution](./day05/d05.py)
We have a map of unicode characters and we travel from the top-left corner to the bottom-right corner, with slope of 2, and wrapping in the horizontal direction.\
We need to calculate the number of 💩s we are stepping on :)\
Solving this in Python is rather straightforward, just iterate over the rows and check the character at the current position.\
In other languages, one may need to consider the unicode characters with surrogate pairs and and how to handle them properly.

## Day 6: [Mojibake puzzle dictionary](https://i18n-puzzles.com/puzzle/6/) &rarr; [Solution](./day06/d06.py)
This puzzle is about to change the encoding of some of the input words.\
Every 3rd and every 5th word is decoded with `latin-1` encoding instead of `utf-8`.\
Every 15th word is doubly encoded/decoded this way.\
We need to find all the words (with proper encoding) that are fit in the input grid of words.\
The key to solve this puzzle is to simply encode the corresponding words with `latin-1` and then decode the result with `utf-8`.

## Day 7: [The audit trail fixer](https://i18n-puzzles.com/puzzle/7/) &rarr; [Solution](./day07/d07.py)
We have a list of date/times from two different timezones: `Amierca/Halifax` and `America/Santiago`.\
They are both either `+4` or `+3` hours from `UTC`, depending on the time of the year and daylight saving time.\
For each date/time, we need to add a number of minutes, decrease a number of minutes and find the result in local time.\
The key to solve this puzzle is to:
* Figure out timezone is not only a shift from `UTC`, but also depends on the time of the year.
* Find which city the input time is from.
    * To do so, we can first parse the input date/time string to a `datetime` object.
    * Translate the `datetime` object to `UTC` timezone (since the delta is provided).
    * Then, we can use the `datetime.astimezone()` function to convert the `datetime` object to the local timezones for both cities and check which one is identical to the original local time.
    * Add the `timedelta` to the `datetime` object in `UTC` and then convert it to the local timezone of the proper city.

## Day 8: [Unicode passwords redux](https://i18n-puzzles.com/puzzle/8/) &rarr; [Solution](./day08/d08.py)
A similar puzzle to Day 3, but this time with more complex rules.\
We need to normalize all the accented letters to their base letters.\
Also ensure at least one vowel, at least one consonant, at least one digit and no repeated normalized characters are present in the password.\
To normalize the accented letters, we can use the `unicodedata` module in python:
```python
from unicodedata import normalize
normalized = normalize("NFD", line).encode("ascii", "ignore").decode("utf-8")
```
To check the non-repeated characters, we can use `collections.Counter` class in python.
* `Counter.most_common()` function can be used to find the most common elements in a list.

## Day 9: [Nine Eleven](https://i18n-puzzles.com/puzzle/9/) &rarr; [Solution](./day09/d09.py)
We have a list of dates and corresponding names.\
Each date consists of 3 numbers, but we don't know which order they are in.\
The used order for each name is consistent.\
We need to find the correct order of the numbers and list the names which are related to the date `Sep/11/2001`.\
The key to solve this is to iterate over possible ordering for each name and try building `datetime` objects for all the related dates.\
If all the `datetime` object is successfully built, then we can check if `Sep/11/2001` is in the list.

### Bugs and Issues:
* Simply looking at minimum and maximum possible values for each field (year, month, day) is not enough.
* Using only two digits for the year value leads to wrong leap year calculations.

## Day 10: [Unicode passwords strike back!](https://i18n-puzzles.com/puzzle/10/) &rarr; [Solution](./day10/d10.py)
We have pairs of usernames and encrypted passwords with `bcrypt` algorithm, plus a list of login attempts.\
We need to find the correct username/password pairs.\
The challenge is two fold:
* Passwords are encrypted with `bcrypt` algorithm, which is not reversible.
* Passwords are not limited to `ascii` characters, but can be any unicode character.
* Same password can be encoded differently in unicode (composed vs decomposed forms of accented letters).

To solve this puzzle, we can: 
* use the `bcrypt` library in python (`checkpw` function) to check if a password is valid for a given username.
* first normalize all the password attempts to their composed form using `unicodedata.normalize("NFC", password)`.
* generate all the possilbe combinations of the passwords at each attempts (iterating over all possible forms of the accented letters).
* then, we can use the `bcrypt` library to check if any of the passwords is valid for the given username.
* To speed up the process, we can parallelize the process using `concurrent.futures` module in python.
    * Use `ThreadPoolExecutor` to run the password checks in parallel.

### Bugs and Issues:
* I initially missed the fact that I have to normalize all the passwords to their composed form before expanding them to all possible combinations. 


## Day 11: [Homer's cipher](https://i18n-puzzles.com/puzzle/11/) &rarr; [Solution](./day11/d11.py)
A puzzle of playing with Caesar's cipher in greek alphabet.\
Caesar's cipher shifts the characters by a fixed number of positions in the alphabet in a cyclic manner.\
We need to find all the possible shift values which deciphers `Odysseus`s name in all of the possible spelling ways.\
The main challenges here are:
* We have to handle greek alphabet characters in unicode.
* The non-capital letter sigma has two forms: `σ` and `ς` and in unicode values they are coming next to each other (so add/subtraction operations will not be very helpful).
* The `Odysseus` name can be a subset of a longer word, so we need to check all the possible substrings of the input string as well.

To solve this:
* I first capitalized all the letters in the input string (to get rid of the `ς` character: the capital sigma has only one form: `Σ`).
* I hard-coded the list of all capital letters in the greek alphabet and made a dictionary to map them to their index in the list.
* For every word in the text, I checked all the possible shifts and checked if any form of `Odysseus` is present in the word.
* I `cache`d the resulted shift value for each word to  avoid recalculating them.


##  Day 12: [The Great Emoji Escape](https://i18n-puzzles.com/puzzle/12/) &rarr; [Solution](./day12/d12.py)
We are provided with a phone-book, consisting of a list of family names, names and phone numbers.\
We need to pre-process the names in three different ways:
* English: 
    * Replace `Æ` with `AE`
    * Replace `Ø` with `O`
    * Normalize all the remaining accented letters
* Swedish:
    * Replace `Æ` with `Ä`
    * Replace `Ø` with `Ö`
    * Keep all Swedish letters (`Ä`, `Ö`, and `Å`)
    * Normalize all the remaining accented letters
* Dutch:
    * Replace `Æ` with `AE`
    * Replace `Ø` with `O`
    * Normalize all the remaining accented letters
    * Ignore all the Dutch family name prefixes (e.g. `VAN`, `DE`, `DEN`, `DER`, etc). 
Then we need to sort the list of names in each language.\
When sorting, we need to ignore all the non-alphabetic characters (e.g. `-`, `'`, etc).\
We also need to sort them based on family names first and then names, ignoring the case.\
Finally we need to find the very middle name's phone number in the sorted list.

### Bugs and Issues:
* Mixing the family names and names in the sorting process!
    * "DOE, JOHN" should be sorted before "DOERR, JANE" but "DOEJOHN" will be sorted after "DOERRJANE".
    * So ideally the names should be split into tuples of (`family_name`, `name`) and then sorted based on the tuple values.
* For Swedish rules, one needs to handles characters individually since we only want to normalize non-swedish characters.
* For Dutch rules, the combination of the prefixes are also important and needs to be ignored, e.g. `VAN DER` should be ignored as well.



## Day 13: [Gulliver's puzzle dictionary](https://i18n-puzzles.com/puzzle/12/) &rarr; [Solution](./day12/d12.py)
The mechanics of this puzzle is similar to Day 6.\
The difference is that we need to consider the words as hexadecimal strings and convert them to either:
* `utf-8` encoding
* `latin-1` encoding
* `utf-16le` encoding
* `utf-16be` encoding
* `utf-8` encoding with BOM (`efbbbf`)
* `utf-16le` encoding with BOM (`fffe`)
* `utf-16be` encoding with BOM (`feff`)
To convert the input `str` codes to binary, we can use either:
* the `bytes.fromhex()` function,
* `codecs.decode(str, "hex")`,
* `binascii.unhexlify(str)`, 
* etc.
The we can use the `.decode` method to decode the binary stream to a string.\
One point to consider today was to ensure the decoded string is alphabetic (`isalpha()`), and ignore it if now.\
Fortunately, each pattern had only one and only one matching word, which simplified the solution.

## Day 14: [Metrification in Japan](https://i18n-puzzles.com/puzzle/14/) &rarr; [Solution](./day14/d14.py)
A puzzle of handing Japanese metric system via Japanese characters.\
We need to read and convert:
* Japanese numbers
* Japanese length units
Fortunately, for the hard part (numbers) we have `kanjize` library in python, which can convert Japanese numbers.\
For length units, I copy/pasted the characters from the puzzle and made a dictionary to map them to their corresponding values.

## Day 15: [24/5 support](https://i18n-puzzles.com/puzzle/15/) &rarr; [Solution](./day15/d15.py)
Handling time-ranges in different timezones.\
We are provided with a set of service offices in different timezones with their working hours and holidays, plus a list of time zones for which we need to provide 24/5 support.\
We need to find the time ranges (for each request timezone) when the service is needed but not available.\
The key to solve this puzzle is to:
* Parse the input date/time strings to `datetime` objects for both service and request timezone/durations.
* Use `ZoneInfo` class in `zoneinfo` module to get the timezone information.
* Convert the start time and the end time to `UTC` timezone.
* Find the gaps between the service hours and the request hours.
    * This can be done by iterating over minute values and handle all the minutes in `set`s.
    * Consider ranges of minutes and add/substract them to/from the set.

TODO: I still need to further refine my code for this day!

## Day 16: [8-bit unboxing](https://i18n-puzzles.com/puzzle/16/) &rarr; [Solution](./day16/d16.py)
We are provided a grid of misaligned 8-bit "pipe" characters in `CP437` (MS-DOS) encoding (e.g. "╕╣║).\
We need to find the number of needed rotations to align all the pipes in the grid.\

To read the grid, we can use:
```python
from pathlib import Path
grid = Path(filename).read_text(encoding="CP437")
```
which maps the `CP437` characters to their corresponding unicode characters.

To solve this, I had to build a dictionary to keep the number of connections on each of the 4 sides of each possible character.\
This way, we can simply map each character to a quadraple of 4 values (connection count on right, down, left, and up) and check if the number of connections is equal to the number of connections on the other side.\
Fortunately, the solution was easy to achieve and didn't need any backtracking.

## Day 17: [╳ marks the spot](https://i18n-puzzles.com/puzzle/17/) &rarr; [Solution](./day17/d17.py)
A jig-saw puzzle of finding the right pieces to fit in a grid.\
Tiles consist of hexadecimal strings, when all put together properly, interpreted as byte arrays and decoded as 'utf-8', represent a map of characters with pipe characters in the borders.\

TODO: Refine my code and the description here for this day!

## Day 18: [Rex To Lynx](https://i18n-puzzles.com/puzzle/18/) &rarr; [Solution](./day18/d18.py)
An interesting puzzle of handling bi-directional text with `RLI` (right-to-left isolate), `LRI` (left-to-right isolate), and `PDI` (pop directional isolate) unicode characters.\
The puzzle statement provides an easy to understand explanation of the BiDi algorithm and how to implement it.\
The only tricky point which is not explicitly mentioned in the puzzle is:
* The `PDI` character pops the latest `RLI` or `LRI`, so it decreases the current embedding level by one.

Python's `eval` was very handy today to evaluate the expression and get the result.

TODO:
* There should be a way to do the BiDi part in a single pass, instead of two passes.
* I would like to implement the `eval()` function as well.
* There should be a library to handle the BiDi algorithm out-of-the box.

### Bugs and Issues:
* Casting the evaluation result to `int` will truncate the decimal part and may lead to wrong results, since we have division operations and may get minor imprecise values. Thus we need to round the values first:
```python
int(5850.999999999999) -> 5850
int(round(5850.999999999999)) -> 5851
```

## Day 19: [](https://i18n-puzzles.com/puzzle/19/) &rarr; [Solution](./day19/d19.py)
## Day 20: [](https://i18n-puzzles.com/puzzle/20/) &rarr; [Solution](./day20/d20.py)