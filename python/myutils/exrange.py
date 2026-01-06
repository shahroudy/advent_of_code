from functools import reduce


def ranges_overlap(r1: range, r2: range):
    return r1.start < r2.stop and r1.stop > r2.start


def range_includes(r1: range, r2: range):
    return r1.start <= r2.start and r1.stop >= r2.stop


def range_is_included(r1: range, r2: range):
    return r1.start >= r2.start and r1.stop <= r2.stop


def ranges_sub_super_set(r1: range, r2: range):
    return range_includes(r1, r2) or range_is_included(r1, r2)


def ranges_minus(r1: range, r2: range):
    if not ranges_overlap(r1, r2):
        return [r1]
    if r1 == r2:
        return []
    if r1.start < r2.start and r1.stop < r2.stop:
        return [range(r1.start, r2.start)]
    if r1.start < r2.start and r1.stop > r2.stop:
        return [range(r1.start, r2.start), range(r2.stop, r1.stop)]
    if r1.start > r2.start and r1.stop < r2.stop:
        return []
    if r1.start > r2.start and r1.stop > r2.stop:
        return [range(r2.stop, r1.stop)]
    if r1.start == r2.start:
        return [range(r2.stop, r1.stop)]
    if r1.stop == r2.stop:
        return [range(r1.start, r2.start)]
    raise Exception("Unexpected case")


def ranges_intersection(r1: range, r2: range):
    if not ranges_overlap(r1, r2):
        return None
    return range(max(r1.start, r2.start), min(r1.stop, r2.stop))


class ExRange:
    def __init__(self, *args):
        assert len(args) <= 2
        if not args:
            self.ranges = []
        elif len(args) == 1:
            assert isinstance(args[0], (range, ExRange, list))
            if isinstance(args[0], range):
                self.ranges = [args[0]]
            elif isinstance(args[0], ExRange):
                self.ranges = args[0].ranges.copy()
            else:
                if isinstance(args[0][0], range):
                    self.ranges = args[0].copy()
                elif isinstance(args[0][0], ExRange):
                    self.ranges = []
                    for r in args[0]:
                        self.ranges += r.ranges
        else:
            self.ranges = [range(*args)]
        self._merge_ranges()

    def __contains__(self, item):
        if len(self.ranges) == 0 or item < self.ranges[0].start or item >= self.ranges[-1].stop:
            return False
        start, end = 0, len(self.ranges) - 1
        while start <= end:
            mid = (start + end) // 2
            if item in self.ranges[mid]:
                return True
            elif item < self.ranges[mid].start:
                end = mid - 1
            else:
                start = mid + 1

    def length(self):
        return sum(len(r) for r in self.ranges)

    def _sort_ranges(self):
        self.ranges.sort(key=lambda r: r.start)

    def _merge_ranges(self):
        self._sort_ranges()
        merged_ranges = []
        for r in self.ranges:
            if merged_ranges and (merged_ranges[-1].stop >= r.start):
                merged_ranges[-1] = range(
                    merged_ranges[-1].start, max(r.stop, merged_ranges[-1].stop)
                )
            else:
                merged_ranges.append(r)
        self.ranges = merged_ranges

    def add(self, *args):
        self.ranges.extend(ExRange(*args).ranges)
        self._merge_ranges()

    def __add__(self, *args):
        new_range = ExRange(self)
        new_range.add(*args)
        return new_range

    def subtract(self, *args):
        minus_range = ExRange(*args)
        ranges = self.ranges
        for m in minus_range.ranges:
            new_ranges = []
            for r in ranges:
                new_ranges += ranges_minus(r, m)
            ranges = new_ranges
        self.ranges = ranges
        self._sort_ranges()

    def __sub__(self, *args):
        new_range = ExRange(self)
        new_range.subtract(*args)
        return new_range

    def intersect(self, *args):
        intersect_range = ExRange(*args)
        new_ranges = []
        for r in self.ranges:
            for i in intersect_range.ranges:
                if intersection := ranges_intersection(r, i):
                    new_ranges.append(intersection)
        self.ranges = new_ranges
        self._sort_ranges()


if __name__ == "__main__":
    r = ExRange(0, 10)
    r.add(5, 15)
    assert r.length() == 15
    r.add(20, 30)
    assert r.length() == 25
    assert 25 in r
    assert 10 in r
    assert 17 not in r
    r.add(25, 35)
    assert r.length() == 30
    r.subtract(2, 5)
    assert r.length() == 27
    r.add(-10, 50)
    assert r.length() == 60

    s = ExRange(9, 21) + ExRange(30, 40)
    s2 = ExRange([range(9, 21), range(30, 40)])
    r2 = r - s
    assert r2.length() == 38
    r2 = r - s2
    assert r2.length() == 38
    r1 = ExRange(0, 10)
    r1.intersect(5, 15)
    assert r1.length() == 5
    r1 = ExRange([range(30, 40), range(10, 20)])
    r1.intersect([range(5, 15), range(25, 35)])
    assert r1.length() == 10
    print("All tests passed")
