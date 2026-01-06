from myutils.exrange import (
    range_includes,
    range_is_included,
    ranges_intersection,
    ranges_minus,
    ranges_overlap,
    ranges_sub_super_set,
)


def range2d_overlap(r1, r2):
    return all(ranges_overlap(r1[i], r2[i]) for i in range(2))


def range2d_intersection(r1, r2):
    if not range2d_overlap(r1, r2):
        return None
    return (
        ranges_intersection(r1[0], r2[0]),
        ranges_intersection(r1[1], r2[1]),
    )


class Pixel2D:
    def __init__(self, ranges):
        self.x_idx = sorted({r[0].start for r in ranges} | {r[0].stop for r in ranges})
        self.y_idx = sorted({r[1].start for r in ranges} | {r[1].stop for r in ranges})
        self.pixels = set()
        for input_range in ranges:
            xr, yr, sign = input_range
            x1 = self.x_idx.index(xr.start)
            x2 = self.x_idx.index(xr.stop)
            y1 = self.y_idx.index(yr.start)
            y2 = self.y_idx.index(yr.stop)
            p = {(x, y) for x in range(x1, x2) for y in range(y1, y2)}
            if sign:
                self.pixels |= p
            else:
                self.pixels -= p

    def current_pixels(self):
        return [
            (
                range(self.x_idx[x], self.x_idx[x + 1]),
                range(self.y_idx[y], self.y_idx[y + 1]),
            )
            for x, y in self.pixels
        ]

    def area(self):
        total = 0
        for rx, ry in self.current_pixels():
            total += (rx.stop - rx.start) * (ry.stop - ry.start)
        return total
