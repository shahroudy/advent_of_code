from myutils.exrange import (
    range_includes,
    range_is_included,
    ranges_intersection,
    ranges_minus,
    ranges_overlap,
    ranges_sub_super_set,
)


def range3d_overlap(r1, r2):
    return all(ranges_overlap(r1[i], r2[i]) for i in range(3))


def range3d_intersection(r1, r2):
    if not range3d_overlap(r1, r2):
        return None
    return (
        ranges_intersection(r1[0], r2[0]),
        ranges_intersection(r1[1], r2[1]),
        ranges_intersection(r1[2], r2[2]),
    )


class Voxel3D:
    def __init__(self, ranges):
        self.x_idx = sorted({r[0].start for r in ranges} | {r[0].stop for r in ranges})
        self.y_idx = sorted({r[1].start for r in ranges} | {r[1].stop for r in ranges})
        self.z_idx = sorted({r[2].start for r in ranges} | {r[2].stop for r in ranges})
        self.voxels = set()
        for input_range in ranges:
            xr, yr, zr, sign = input_range
            x1 = self.x_idx.index(xr.start)
            x2 = self.x_idx.index(xr.stop)
            y1 = self.y_idx.index(yr.start)
            y2 = self.y_idx.index(yr.stop)
            z1 = self.z_idx.index(zr.start)
            z2 = self.z_idx.index(zr.stop)
            v = {(x, y, z) for x in range(x1, x2) for y in range(y1, y2) for z in range(z1, z2)}
            if sign:
                self.voxels |= v
            else:
                self.voxels -= v

    def current_voxels(self):
        return [
            (
                range(self.x_idx[x], self.x_idx[x + 1]),
                range(self.y_idx[y], self.y_idx[y + 1]),
                range(self.z_idx[z], self.z_idx[z + 1]),
            )
            for x, y, z in self.voxels
        ]

    def volume(self):
        total = 0
        for rx, ry, rz in self.current_voxels():
            total += (rx.stop - rx.start) * (ry.stop - ry.start) * (rz.stop - rz.start)
        return total
