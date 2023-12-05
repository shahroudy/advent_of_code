import os
from myutils.file_reader import read_int_list

    input_file = f'{os.environ.get("aoc_inputs")}/aoc2020_day01.txt'
values = read_int_list(input_file)

# first challenge, using dictionary
d = {}
for n in values:
    if d.get(n, None) is not None:
        print(n * d[n])
    d[2020-n] = n

# second challenge, using double dictionaries
d = {}
dd = {}
for n in values:
    if dd.get(n, None) is not None:
        print(n * dd[n])
    for k, v in d.items():
        dd[k-n] = v * n
    d[2020-n] = n

# second challenge, using brute-force looping!
for i in range(len(values)):
    for j in range(i+1, len(values)):
        for k in range(j+1, len(values)):
            if values[i]+values[j]+values[k] == 2020:
                print(values[i]*values[j]*values[k])
