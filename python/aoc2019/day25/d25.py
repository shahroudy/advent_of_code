import os
import re
from collections import defaultdict, deque
from itertools import combinations
from pathlib import Path

from aoc2019.day09.d09 import IntcodeComputer
from myutils.io_handler import get_input_data


class Cryostasis:
    def __init__(self, filename):
        self.program = list(map(int, Path(filename).read_text().split(",")))

    def compile_to_text(self, intcode):
        return "".join(map(chr, intcode))

    def compile_to_intcode(self, text):
        if text[-1] != "\n":
            text += "\n"
        return deque(map(ord, text))

    def analyze_output(self, output_text):
        room_name = re.search(r"== (.*) ==", output_text).group(1)
        doors_text = re.search("Doors here lead:\n(.*)\n\n", output_text, re.DOTALL).group(1)
        doors = re.findall(r"- (north|west|east|south)", doors_text)
        if items_search := re.search("Items here:\n(.*)\n\n", output_text, re.DOTALL):
            items = re.findall(r"- (.*)", items_search.group(1))
        else:
            items = []
        return room_name, doors, items

    def find_path(self, start, end, next_rooms):
        previous = dict()
        q = deque()
        visited = set()
        q.append(start)
        visited.add(start)
        while q:
            u = q.popleft()
            for d, v in next_rooms[u]:
                if v not in visited:
                    previous[v] = (d, u)
                    if v == end:
                        doors = [d]
                        while u != start:
                            d, u = previous[u]
                            doors.append(d)
                        return doors[::-1]
                    visited.add(v)
                    q.append(v)

    def run_droid(self, show_announcements=False):
        opposite = {"east": "west", "west": "east", "north": "south", "south": "north"}
        dont_take = {"molten lava", "giant electromagnet", "escape pod", "infinite loop", "photons"}
        computer = IntcodeComputer(self.program)
        computer.reset(deque())

        next_rooms = defaultdict(set)
        to_check_rooms = defaultdict(set)
        rooms_order = []
        last_door = current_room_name = room_to_go = None
        while True:  # explore rooms and pick safe items, finish at Security Checkpoint
            output_text = self.compile_to_text(computer.compute_while_input())
            last_room = current_room_name
            if room_to_go:
                output_text = output_text.split("\n\n\n")[-1]
                last_door = None
            current_room_name, doors, items = self.analyze_output(output_text)
            if room_to_go:
                assert current_room_name == room_to_go
                room_to_go = None
            if current_room_name not in rooms_order:
                rooms_order.append(current_room_name)
            if last_door is not None:
                next_rooms[last_room].add((last_door, current_room_name))
                to_check_rooms[last_room].discard(last_door)
                next_rooms[current_room_name].add((opposite[last_door], last_room))
                to_check_rooms[current_room_name].discard(opposite[last_door])
            for last_door in doors:
                if last_door not in {n[0] for n in next_rooms[current_room_name]}:
                    to_check_rooms[current_room_name].add(last_door)
            for item in set(items) - dont_take:
                computer.input.extend(self.compile_to_intcode("take " + item))
            if to_check_rooms[current_room_name] and current_room_name != "Security Checkpoint":
                last_door = to_check_rooms[current_room_name].pop()
                computer.input.extend(self.compile_to_intcode(last_door))
            else:
                for room in rooms_order[::-1]:  # find the last room with unexplored doors
                    if to_check_rooms[room] and room != "Security Checkpoint":
                        room_to_go = room
                        break
                else:  # no more rooms to explore, let's go to the Security Checkpoint
                    room_to_go = "Security Checkpoint"
                if room_to_go == current_room_name == "Security Checkpoint":
                    break
                else:
                    path = self.find_path(current_room_name, room_to_go, next_rooms)
                    computer.input.extend(self.compile_to_intcode("\n".join(path)))
        # now we need to evaluate the items in the inventory and find the right combination
        computer.input.extend(self.compile_to_intcode("inv"))
        output_text = self.compile_to_text(computer.compute_while_input())
        items = set(re.findall(r"- (.*)", output_text))
        selections = set()
        for item_count in range(len(items) + 1):
            selections |= set(combinations(items, item_count))
        weight_err_re = r"Alert! Droids on this ship are (\w+) than the detected value!"
        door_to_pressure_sensor_floor = to_check_rooms["Security Checkpoint"].pop()
        holding_items = items
        while selections:
            inp = ""
            current_items = set(selections.pop())
            for item in holding_items - current_items:
                inp += "drop " + item + "\n"
            for item in current_items - holding_items:
                inp += "take " + item + "\n"
            inp += door_to_pressure_sensor_floor + "\n"
            computer.input.extend(self.compile_to_intcode(inp))
            output_text = self.compile_to_text(computer.compute_while_input())
            holding_items = current_items
            if m := re.search(weight_err_re, output_text):
                if m.group(1) == "lighter":
                    selections -= {s for s in selections if set(s) > set(current_items)}
                elif m.group(1) == "heavier":
                    selections -= {s for s in selections if set(s) < set(current_items)}
            else:
                announcement = output_text.split("\n\n")[-1]
                code = int(re.search(r"\d+", announcement).group(0))
                if show_announcements:
                    print(announcement)
                return code


if __name__ == "__main__":
    data = get_input_data(__file__)
    fn = data.input_file

    assert Cryostasis(fn.replace(".txt", "_sample1.txt")).run_droid() == 2228740
    assert Cryostasis(fn.replace(".txt", "_sample2.txt")).run_droid() == 11534338
    assert Cryostasis(fn.replace(".txt", "_sample3.txt")).run_droid() == 269520896
    assert Cryostasis(fn.replace(".txt", "_sample4.txt")).run_droid() == 529920

    print("Tests passed, starting with the puzzle")

    puzzle = Cryostasis(fn)
    print(puzzle.run_droid(show_announcements=True))
