from collections import deque
from pathlib import Path

from myutils.io_handler import get_input_data


class DiskFragmenter:
    def __init__(self, filename):
        disk = []
        space = False
        counter = 0
        for i in list(map(int, list(Path(filename).read_text().strip()))):
            if i > 0:
                disk.append((-1 if space else counter, i))
            counter += space
            space = not space
        self.disk = self.merge_spaces(disk)

    def merge_spaces(self, disk):
        new_disk = []
        space_count = 0
        for id, count in disk:
            if id >= 0:
                if space_count > 0:
                    new_disk.append((-1, space_count))
                    space_count = 0
                new_disk.append((id, count))
            else:
                space_count += count
        return new_disk

    def checksum_after_moving_files(self):
        disk = deque(self.disk)
        checksum = 0
        position = 0
        while disk:
            id, count = disk.popleft()
            if id < 0:
                last_id = -1
                while last_id < 0 and disk:
                    last_id, last_count = disk.pop()
                if last_id < 0:
                    break  # no more files to consider for checksum
                m = min(last_count, count)
                if last_count < count:
                    disk.appendleft((id, count - m))
                elif count < last_count:
                    disk.append((last_id, last_count - count))
                id, count = last_id, m
            for _ in range(count):
                checksum += position * id
                position += 1
        return checksum

    def checksum_after_moving_files_in_blocks_adhoc(self):
        disk = self.disk.copy()
        current = max(a[0] for a in disk)
        while current > 0:
            j = len(disk) - 1
            while disk[j][0] != current:
                j -= 1

            k = 0
            while disk[k][0] != -1 or disk[k][1] < disk[j][1]:
                k += 1
                if k == j:
                    break
            if k == j:
                current -= 1
                continue

            block = disk[j]
            disk[j] = (-1, disk[j][1])

            if disk[k][1] == block[1]:
                disk[k] = block
            else:
                disk[k] = (-1, disk[k][1] - block[1])
                disk = disk[:k] + [block] + disk[k:]
            current -= 1

            disk = self.merge_spaces(disk)

        checksum = 0
        counter = 0
        for i, c in disk:
            for j in range(c):
                if i != -1:
                    checksum += counter * i
                counter += 1
        return checksum

    def checksum_after_moving_files_in_blocks(self):
        class Node:  # double linked list
            def __init__(self, id, count):
                self.id = id
                self.count = count
                self.next = None
                self.prev = None

        # build a double linked list
        pre = None
        for id, count in self.disk:
            node = Node(id, count)
            if pre:
                pre.next = node
                node.prev = pre
            else:
                start = node
            pre = node
        last = pre

        current_id = last.id + 1
        current = last
        while current and current_id > 0:
            current_id -= 1
            if current_id == 0:
                break
            while current.id != current_id:
                current = current.prev
            if not current:
                break

            # find space
            space = start
            while space.id >= 0 or space.count < current.count:
                space = space.next
                if space == current:
                    break
            if space == current:
                continue

            id, count = current.id, current.count
            current.id = -1

            # merge if next one is also space
            if current.next and current.next.id == -1:
                current.count += current.next.count
                if current.next.next:
                    current.next.next.prev = current
                current.next = current.next.next
            # merge if previous one is also space and not the picked space
            if current.prev and current.prev.id == -1 and current.prev != space:
                current.count += current.prev.count
                if current.prev.prev:
                    current.prev.prev.next = current
                current.prev = current.prev.prev

            if space.count == count:
                space.id = id
            else:
                # split space by inserting a new node
                space.count -= count
                new_node = Node(id, count)
                space.prev.next = new_node
                new_node.prev = space.prev
                new_node.next = space
                space.prev = new_node

        checksum = 0
        counter = 0
        current = start
        while current:
            for _ in range(current.count):
                if current.id > 0:
                    checksum += counter * current.id
                counter += 1
            current = current.next
        return checksum


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert DiskFragmenter("sample1.txt").checksum_after_moving_files() == 1928
    assert DiskFragmenter("sample1.txt").checksum_after_moving_files_in_blocks() == 2858

    print("Tests passed, starting with the puzzle")

    puzzle = DiskFragmenter(data.input_file)

    print(puzzle.checksum_after_moving_files())
    print(puzzle.checksum_after_moving_files_in_blocks())
