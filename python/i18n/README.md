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