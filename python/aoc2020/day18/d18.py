import re
from itertools import count
from pathlib import Path

from myutils.io_handler import get_input_data


class OperationOrder:
    def __init__(self, filename):
        self.inp = [re.sub(r"\s", "", exp) for exp in Path(filename).read_text().splitlines()]

    def find_first_matching_parenthesis(self, expr: str) -> str:
        if "(" not in expr:
            return None
        depth, left = 1, expr.index("(")
        for right in count(left + 1):
            depth += {"(": 1, ")": -1}.get(expr[right], 0)
            if depth == 0:
                return expr[left : right + 1]

    def eval1(self, expr: str) -> int:
        if expr.isnumeric():
            return int(expr)
        if sub := self.find_first_matching_parenthesis(expr):
            return self.eval1(expr.replace(sub, str(self.eval1(sub[1:-1]))))
        left_most = re.match(r"(\d+[+*]\d+)", expr).group()
        return self.eval1(expr.replace(left_most, str(eval(left_most)), 1))

    def eval2(self, expr: str) -> int:
        if expr.isnumeric():
            return int(expr)
        if sub := self.find_first_matching_parenthesis(expr):
            return self.eval2(expr.replace(sub, str(self.eval2(sub[1:-1]))))
        if m := re.search(r"(\d+\+\d+)", expr):
            return self.eval2(expr.replace(m.group(), str(eval(m.group()))))
        return eval(expr)

    def homework(self):
        return sum(map(self.eval1, self.inp))

    def homework_advanced(self):
        return sum(map(self.eval2, self.inp))


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert OperationOrder("sample1.txt").homework() == 71
    assert OperationOrder("sample2.txt").homework() == 26
    assert OperationOrder("sample3.txt").homework() == 437
    assert OperationOrder("sample4.txt").homework() == 12240
    assert OperationOrder("sample5.txt").homework() == 13632

    assert OperationOrder("sample1.txt").homework_advanced() == 231
    assert OperationOrder("sample2.txt").homework_advanced() == 46
    assert OperationOrder("sample3.txt").homework_advanced() == 1445
    assert OperationOrder("sample4.txt").homework_advanced() == 669060
    assert OperationOrder("sample5.txt").homework_advanced() == 23340

    print("Tests passed, starting with the puzzle")

    puzzle = OperationOrder(data.input_file)

    print(puzzle.homework())
    print(puzzle.homework_advanced())
