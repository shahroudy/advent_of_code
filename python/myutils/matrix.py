from functools import reduce

from myutils.geometry import Point


def transpose(m):
    if isinstance(m[0], str):
        return type(m)("".join(row) for row in zip(*m))
    else:
        return type(m)([type(m[0])(row) for row in zip(*m)])


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


def rotate(m, times=1):
    t = times % 4
    if t == 0:
        return m
    elif t == 1:
        return rotate_90(m)
    elif t == 2:
        return rotate_180(m)
    else:
        return rotate_270(m)


def sub_matrix(m, row_start, row_end, col_start, col_end):
    return type(m)([row[col_start:col_end] for row in m[row_start:row_end]])


def tile_side(pattern, side_no, canonical=False):
    # side_no: 0:top ltr, 1:right downwards, 2:bottom rtl, 3:left upwards, 4-7: reversed of 0-3
    # canonical: True: return min(side, side[::-1])
    if canonical:
        return min(tile_side(pattern, side_no), tile_side(pattern, (side_no + 4) % 8))
    if side_no > 3:
        return tile_side(pattern, side_no - 4)[::-1]
    if side_no == 0:
        return pattern[0]
    if side_no == 2:
        return pattern[-1]
    if side_no == 1:
        result = [row[-1] for row in pattern]
    if side_no == 3:
        result = [row[0] for row in pattern]
    if isinstance(pattern[0], list):
        return result
    if isinstance(pattern[0], str):
        return "".join(result)
    if isinstance(pattern[0], tuple):
        return tuple(result)


def tuple_matrix(m):
    return tuple(tuple(row) for row in m)


def hstack(matrices):
    return transpose(vstack(transpose(matrix) for matrix in matrices))


def vstack(matrices):
    return reduce(lambda a, b: a + b, matrices)


def concat_2d_matrices(matrices):
    return vstack(hstack(row) for row in matrices)


def find_all_points_with_value(matrix, value):
    return {Point(x, y) for y, r in enumerate(matrix) for x, cell in enumerate(r) if cell == value}


if __name__ == "__main__":
    test1 = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    assert transpose(test1) == [[0, 3, 6], [1, 4, 7], [2, 5, 8]]
    assert flip(test1) == [[6, 7, 8], [3, 4, 5], [0, 1, 2]]
    assert mirror(test1) == [[2, 1, 0], [5, 4, 3], [8, 7, 6]]
    assert rotate_90(test1) == [[6, 3, 0], [7, 4, 1], [8, 5, 2]]
    assert rotate_180(test1) == [[8, 7, 6], [5, 4, 3], [2, 1, 0]]
    assert rotate_270(test1) == [[2, 5, 8], [1, 4, 7], [0, 3, 6]]
    a = [[1, 2], [3, 4]]
    b = [[5, 6], [7, 8]]
    assert hstack([a, b]) == [[1, 2, 5, 6], [3, 4, 7, 8]]
    assert vstack([a, b]) == [[1, 2], [3, 4], [5, 6], [7, 8]]
    c = [[11, 12], [13, 14]]
    d = [[15, 16], [17, 18]]
    assert concat_2d_matrices([[a, b], [c, d]]) == [
        [1, 2, 5, 6],
        [3, 4, 7, 8],
        [11, 12, 15, 16],
        [13, 14, 17, 18],
    ]
