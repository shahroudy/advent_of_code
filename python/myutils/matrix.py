def transpose(m):
    return (
        tuple(tuple(row) for row in zip(*m))
        if isinstance(m, tuple)
        else [list(row) for row in zip(*m)]
    )


def flip(m):
    return m[::-1]


def mirror(m):
    r = [row[::-1] for row in m]
    return r if isinstance(m, list) else tuple(r)


def rotate_90(m):
    return mirror(transpose(m))


def rotate_180(m):
    return mirror(flip(m))


def rotate_270(m):
    return flip(transpose(m))


def rotate(m, times):
    t = times % 4
    if t == 0:
        return m
    elif t == 1:
        return rotate_90(m)
    elif t == 2:
        return rotate_180(m)
    else:
        return rotate_270(m)


def tuple_matrix(m):
    return tuple(tuple(row) for row in m)


test1 = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
assert transpose(test1) == [[0, 3, 6], [1, 4, 7], [2, 5, 8]]
assert flip(test1) == [[6, 7, 8], [3, 4, 5], [0, 1, 2]]
assert mirror(test1) == [[2, 1, 0], [5, 4, 3], [8, 7, 6]]
assert rotate_90(test1) == [[6, 3, 0], [7, 4, 1], [8, 5, 2]]
assert rotate_180(test1) == [[8, 7, 6], [5, 4, 3], [2, 1, 0]]
assert rotate_270(test1) == [[2, 5, 8], [1, 4, 7], [0, 3, 6]]
