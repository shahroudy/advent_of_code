from pathlib import Path

from myutils.io_handler import get_input_data


class ElvesLookElvesSay:
    def __init__(self, filename=None):
        if filename:
            self.input = Path(filename).read_text().strip()

    def look_and_say(self, s=None):
        if not s:
            s = self.input
        if isinstance(s, str):
            s = list(map(int, s))
        result, cnt, pre = [], 1, 0
        for i in s:
            if i == pre:
                cnt += 1
            else:
                if pre != 0:
                    result.extend([cnt, pre])
                pre = i
                cnt = 1
        result.extend([cnt, pre])
        return result

    def length_of_result(self, iterations=40):
        s = self.input
        for _ in range(iterations):
            s = self.look_and_say(s)
        return sum(len(str(i)) for i in s)


def test_samples(input, answer):
    assert "".join(map(str, ElvesLookElvesSay().look_and_say(input))) == answer


if __name__ == "__main__":
    data = get_input_data(__file__)

    test_samples("1", "11")
    test_samples("11", "21")
    test_samples("21", "1211")
    test_samples("1211", "111221")
    test_samples("111221", "312211")

    print("Tests passed, starting with the puzzle")

    puzzle = ElvesLookElvesSay(data.input_file)

    print(puzzle.length_of_result(40))
    print(puzzle.length_of_result(50))
