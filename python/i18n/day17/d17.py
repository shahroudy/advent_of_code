import os
from itertools import product
from pathlib import Path


class XMarksTheSpot:
    def __init__(self, filename):
        self.tiles = [t.splitlines() for t in Path(filename).read_text().split("\n\n")]

    def hexstring(self, char):
        return "".join([str(hex(b))[2:] for b in char.encode()])

    def codes_compatible(self, code1, code2):
        # assert code1 is not None
        # assert code2 is not None
        if code1 is None and code2 is None:
            return True
        if code1 is None or code2 is None:
            return False
        if (len(code1) == 1) and (len(code2) == 1):
            return True
        if (len(code1) == 1) or (len(code2) == 1):
            return False
        code = code1 + code2
        while True:
            try:
                byte_data = bytes.fromhex(code)
                unicode_string = byte_data.decode("utf-8")
                if unicode_string == "╳":
                    return False
                return True
            except UnicodeDecodeError as e:
                return False
                if e.reason == "invalid start byte":
                    code = code[2:]
                    continue
                if e.reason == "invalid continuation byte":
                    return False

    def convert_tile_to_unicode(self, tile):
        code = []
        for row in tile:
            rem_start = ""
            rem_end = ""

            complete = False
            while not complete:
                try:
                    byte_data = bytes.fromhex(row)
                    unicode_string = byte_data.decode("utf-8")
                    unicode_row = list(unicode_string)
                    complete = True
                except UnicodeDecodeError as e:
                    if e.reason == "invalid start byte":
                        rem_start = rem_start + row[:2]
                        row = row[2:]
                    elif e.reason == "unexpected end of data":
                        rem_end = row[-2:] + rem_end
                        row = row[:-2]
            if rem_start:
                unicode_row = [rem_start] + unicode_row
            if rem_end:
                unicode_row = unicode_row + [rem_end]
            code.append(unicode_row)
        return code

    def convert_tile_to_unicode_top_left(self, tile, left_over):
        code = []
        for rn, row in enumerate(tile):
            left = left_over[rn] if (rn < len(left_over)) else ""
            rem_end = ""
            rem_start = ""
            if len(left) > 1:
                row = left + row
            complete = False
            while not complete:
                try:
                    byte_data = bytes.fromhex(row)
                    unicode_string = byte_data.decode("utf-8")
                    unicode_row = list(unicode_string)
                    complete = True
                except UnicodeDecodeError as e:
                    if e.reason == "unexpected end of data":
                        rem_end = row[-2:] + rem_end
                        row = row[:-2]
                        if len(row) == 0:
                            return None
                    elif e.reason == "invalid start byte":
                        if len(left) == 0:
                            rem_start = rem_start + row[:2]
                            row = row[2:]
                            if len(row) == 0:
                                return None
                        else:
                            return None
                    else:
                        return None
            if rem_end:
                unicode_row = unicode_row + [rem_end]
            if rem_start:
                unicode_row = [rem_start] + unicode_row
            code.append(unicode_row)
        return code

    def convert_tile_to_unicode_bottom_left(self, tile, left_over):
        code = []
        for rn, row in enumerate(reversed(tile)):
            left = left_over[rn] if (rn < len(left_over)) else ""
            rem_end = ""
            rem_start = ""
            if len(left) > 1:
                row = left + row
            complete = False
            while not complete:
                try:
                    byte_data = bytes.fromhex(row)
                    unicode_string = byte_data.decode("utf-8")
                    unicode_row = list(unicode_string)
                    complete = True
                except UnicodeDecodeError as e:
                    if e.reason == "unexpected end of data":
                        rem_end = row[-2:] + rem_end
                        row = row[:-2]
                        if len(row) == 0:
                            return None
                    elif e.reason == "invalid start byte":
                        if len(left) == 0:
                            rem_start = rem_start + row[:2]
                            row = row[2:]
                            if len(row) == 0:
                                return None
                        else:
                            return None
                    else:
                        return None
            if rem_end:
                unicode_row = unicode_row + [rem_end]
            if rem_start:
                unicode_row = [rem_start] + unicode_row
            code.append(unicode_row)
        return code[::-1]

    def print_grid(self):
        text = []
        for y in range(self.height):
            row_text = []
            for x in range(self.width):
                if self.grid[(x, y)] is not None:
                    if len(self.grid[(x, y)]) > 1:
                        row_text.append("�")
                    else:
                        row_text.append(self.grid[(x, y)])
                else:
                    row_text.append(" ")
            text.append("".join(row_text))
        print("\n".join(text))

    def calc(self):
        topleftchar = "╔"
        toprightchar = "╗"
        bottomleftchar = "╚"
        bottomrightchar = "╝"
        leftrightchars = "|║"
        topbottomchars = "═-"
        topleftcode = self.hexstring(topleftchar)
        toprightcode = self.hexstring(toprightchar)
        bottomleftcode = self.hexstring(bottomleftchar)
        bottomrightcode = self.hexstring(bottomrightchar)
        leftrightcodes = [self.hexstring(leftrightchars[0]), self.hexstring(leftrightchars[1])]
        topbottomcodes = [self.hexstring(topbottomchars[0]), self.hexstring(topbottomchars[1])]

        toplefttile = None
        toprighttile = None
        bottomlefttile = None
        bottomrighttile = None

        lefttiles = set()
        righttiles = set()
        toptiles = set()
        bottomtiles = set()

        incomplete_starts = []
        incomplete_ends = []

        for tile_no, tile in enumerate(self.tiles):
            if tile[0].startswith(topleftcode):
                if toplefttile is not None:
                    print("Duplicate tile found")
                toplefttile = tile_no
            if tile[0].endswith(toprightcode):
                if toprighttile is not None:
                    print("Duplicate tile found")
                toprighttile = tile_no
            if tile[-1].startswith(bottomleftcode):
                if bottomlefttile is not None:
                    print("Duplicate tile found")
                bottomlefttile = tile_no
            if tile[-1].endswith(bottomrightcode):
                if bottomrighttile is not None:
                    print("Duplicate tile found")
                bottomrighttile = tile_no
            if tile[0].startswith(leftrightcodes[0]) or tile[0].startswith(leftrightcodes[1]):
                lefttiles.add(tile_no)
            if tile[0].endswith(leftrightcodes[0]) or tile[0].endswith(leftrightcodes[1]):
                righttiles.add(tile_no)
            if tile[0].startswith(topbottomcodes[0]) or tile[0].startswith(topbottomcodes[1]):
                toptiles.add(tile_no)
            if tile[-1].endswith(topbottomcodes[0]) or tile[-1].endswith(topbottomcodes[1]):
                bottomtiles.add(tile_no)

            for row_no, row in enumerate(tile):
                bad_start = False
                bad_end = False
                check_done = False
                while not check_done:
                    try:
                        byte_data = bytes.fromhex(row)
                        unicode_string = byte_data.decode("utf-8")
                    except UnicodeDecodeError as e:
                        if e.reason == "invalid start byte":
                            bad_start = True
                            row = row[2:]
                            continue
                        if e.reason == "unexpected end of data":
                            bad_end = True
                    check_done = True
                if bad_start:
                    incomplete_starts.append((tile_no, row_no))
                if bad_end:
                    incomplete_ends.append((tile_no, row_no))

        corners = {toplefttile, toprighttile, bottomlefttile, bottomrighttile}

        lefttiles -= corners
        righttiles -= corners
        toptiles -= corners
        bottomtiles -= corners

        self.width = 0
        self.height = 0

        tttt = [toplefttile, toprighttile]
        tttt.extend(toptiles)
        for t in tttt:
            byte_data = bytes.fromhex(self.tiles[t][0])
            unicode_string = byte_data.decode("utf-8")
            self.width += len(unicode_string)
        tttt = [toplefttile, bottomlefttile]
        tttt.extend(lefttiles)
        for t in tttt:
            self.height += len(self.tiles[t])

        unicode_tiles = [self.convert_tile_to_unicode(tile) for tile in self.tiles]

        self.grid = {(x, y): None for x, y in product(range(self.width), range(self.height))}
        remaining_tiles = set(range(len(self.tiles)))

        ### topleft tile
        for row_no, row in enumerate(unicode_tiles[toplefttile]):
            for col_no, char in enumerate(row):
                x, y = col_no, row_no
                self.grid[x, y] = char
        ### topright tile
        for row_no, row in enumerate(unicode_tiles[toprighttile]):
            for col_no, char in enumerate(row):
                x, y = self.width - len(row) + col_no, row_no
                self.grid[x, y] = char
        ### bottomleft tile
        for row_no, row in enumerate(unicode_tiles[bottomlefttile]):
            for col_no, char in enumerate(row):
                x, y = col_no, self.height - len(unicode_tiles[bottomlefttile]) + row_no
                self.grid[x, y] = char
        ### bottomright tile
        for row_no, row in enumerate(unicode_tiles[bottomrighttile]):
            for col_no, char in enumerate(row):
                x, y = (
                    self.width - len(row) + col_no,
                    self.height - len(unicode_tiles[bottomrighttile]) + row_no,
                )
                self.grid[x, y] = char

        remaining_tiles -= {toplefttile, toprighttile, bottomlefttile, bottomrighttile}

        self.print_grid()

        # trying to find a valid trail of top tiles
        def left_match_right(tno1, tno2, top=True):
            # tile1 is left, tile2 is right
            left_col = [row[-1] for row in unicode_tiles[tno1]]
            right_col = [row[0] for row in unicode_tiles[tno2]]
            if not top:
                left_col.reverse()
                right_col.reverse()
            return all(self.codes_compatible(a, b) for a, b in zip(left_col, right_col))

        # stack = [toplefttile]
        # rem = sorted(toptiles)
        # while len(stack) <= len(toptiles):
        tttoptiles = [toplefttile, toprighttile]
        tttoptiles.extend(toptiles)
        after = {n: [] for n in tttoptiles}
        for left, right in product(tttoptiles, repeat=2):
            if left_match_right(left, right):
                after[left].append(right)

        bbbottomtiles = [bottomlefttile, bottomrighttile]
        bbbottomtiles.extend(bottomtiles)
        afterb = {n: [] for n in bbbottomtiles}
        for left, right in product(bbbottomtiles, repeat=2):
            if left_match_right(left, right, top=False):
                afterb[left].append(right)

        current = toplefttile
        cols_so_far = len(unicode_tiles[current][0])
        while remaining_tiles & toptiles:
            assert len(after[current]) == 1
            current = after[current][0]
            remaining_tiles.remove(current)
            for y, row in enumerate(unicode_tiles[current]):
                incomp_delta = -1 if len(row[0]) > 1 else 0
                for x, char in enumerate(row):
                    p = (cols_so_far + x + incomp_delta, y)
                    if len(char) > 1:
                        if self.grid[p] is None:
                            self.grid[p] = char
                        else:
                            code = self.grid[p] + char if x == 0 else char + self.grid[p]
                            byte_data = bytes.fromhex(code)
                            unicode_string = byte_data.decode("utf-8")
                            assert len(unicode_string) == 1
                            self.grid[p] = unicode_string
                    else:
                        self.grid[p] = char
            cols_so_far += len(unicode_tiles[current][0])

        # trying to find a valid trail of bottom tiles
        current = bottomlefttile
        cols_so_far = len(unicode_tiles[current][-1])
        while remaining_tiles & bottomtiles:
            assert len(afterb[current]) == 1
            current = afterb[current][0]
            remaining_tiles.remove(current)
            for yr, row in enumerate(reversed(unicode_tiles[current])):
                y = self.height - 1 - yr
                incomp_delta = -1 if len(row[0]) > 1 else 0
                for x, char in enumerate(row):
                    p = (cols_so_far + x + incomp_delta, y)
                    if len(char) > 1:
                        if self.grid[p] is None:
                            self.grid[p] = char
                        else:
                            code = self.grid[p] + char if x == 0 else char + self.grid[p]
                            byte_data = bytes.fromhex(code)
                            unicode_string = byte_data.decode("utf-8")
                            assert len(unicode_string) == 1
                            self.grid[p] = unicode_string
                    else:
                        self.grid[p] = char
            cols_so_far += len(unicode_tiles[current][-1])

        self.print_grid()

        while remaining_tiles:
            # find the topleft corner of missing tiles
            corners = []
            for yc, xc in product(range(self.height), range(self.width)):
                if (
                    (self.grid[(xc, yc)] is None)
                    and (self.grid.get((xc - 1, yc), None) is not None)
                    and (self.grid.get((xc, yc - 1), None) is not None)
                    and (self.grid.get((xc - 1, yc - 1), None) is not None)
                ):
                    corners.append((xc, yc))

            for xc, yc in corners:
                left_col = []
                x, y = xc, yc
                while self.grid[x, y] is None and self.grid.get((x - 1, y), None) is not None:
                    left_col.append(self.grid[(x - 1, y)])
                    y += 1

                matches = []
                for tile_no in remaining_tiles:
                    if new_tile := self.convert_tile_to_unicode_top_left(
                        self.tiles[tile_no], left_col
                    ):
                        matches.append((tile_no, new_tile))
                if len(matches) == 1:
                    current, new_tile = matches[0]
                    print(f"Found tl tile {current} at {xc}, {yc}")
                    remaining_tiles.remove(current)
                    for y, row in enumerate(new_tile):
                        if y >= len(left_col):
                            incomp_delta = -1 if len(row[0]) > 1 else 0
                        else:
                            incomp_delta = -1 if len(left_col[y]) > 1 else 0
                        for x, char in enumerate(row):
                            p = (xc + x + incomp_delta, y + yc)
                            if len(char) > 1:
                                if self.grid[p] is None:
                                    self.grid[p] = char
                                else:
                                    assert self.grid[p] is not None
                                    if x == 0:
                                        code = self.grid[p] + char
                                    else:
                                        code = char + self.grid[p]
                                    byte_data = bytes.fromhex(code)
                                    unicode_string = byte_data.decode("utf-8")
                                    assert len(unicode_string) == 1
                                    self.grid[p] = unicode_string
                            else:
                                self.grid[p] = char
                    break  # the corners loop

            # find the bottomleft corner of missing tiles
            corners = []
            for yc, xc in product(reversed(range(self.height)), range(self.width)):
                if (
                    (self.grid[(xc, yc)] is None)
                    and (self.grid.get((xc - 1, yc), None) is not None)
                    and (self.grid.get((xc, yc + 1), None) is not None)
                    and (self.grid.get((xc - 1, yc + 1), None) is not None)
                ):
                    corners.append((xc, yc))

            for xc, yc in corners:
                left_col_rev = []
                x, y = xc, yc
                while self.grid[x, y] is None and self.grid.get((x - 1, y), None) is not None:
                    left_col_rev.append(self.grid[(x - 1, y)])
                    y -= 1

                matches = []
                for tile_no in remaining_tiles:
                    if new_tile := self.convert_tile_to_unicode_bottom_left(
                        self.tiles[tile_no], left_col_rev
                    ):
                        matches.append((tile_no, new_tile))

                if len(matches) == 1:
                    current, new_tile = matches[0]
                    print(f"Found bl tile {current} at {xc}, {yc}")
                    remaining_tiles.remove(current)
                    for yr, row in enumerate(reversed(new_tile)):
                        if yr >= len(left_col_rev):
                            incomp_delta = -1 if len(row[0]) > 1 else 0
                        else:
                            incomp_delta = -1 if len(left_col_rev[yr]) > 1 else 0
                        for x, char in enumerate(row):
                            p = (xc + x + incomp_delta, yc - yr)
                            if len(char) > 1:
                                if self.grid[p] is None:
                                    self.grid[p] = char
                                else:
                                    assert self.grid[p] is not None
                                    if x == 0:
                                        code = self.grid[p] + char
                                    else:
                                        code = char + self.grid[p]
                                    byte_data = bytes.fromhex(code)
                                    unicode_string = byte_data.decode("utf-8")
                                    assert len(unicode_string) == 1
                                    self.grid[p] = unicode_string
                            else:
                                self.grid[p] = char
                    break  # the corners loop
            self.print_grid()
            if "╳" in self.grid.values():
                for x, y in self.grid:
                    if self.grid[(x, y)] == "╳":
                        return x * y
        return 0


if __name__ == "__main__":
    assert XMarksTheSpot("test-input.txt").calc() == 132
    print("Tests passed, starting with the puzzle")
    input_folder = os.environ.get("i18n_inputs")
    print(XMarksTheSpot(f"{input_folder}/i18n2025_day17.txt").calc())
