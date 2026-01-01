from pathlib import Path

from myutils.geometry import Point
from myutils.io_handler import get_input_data
from myutils.utils import read_map_dict_of_sets_of_points


class TrenchMap:
    def __init__(self, filename):
        algorithm_text, image_text = Path(filename).read_text().split("\n\n")
        self.code = [ch == "#" for ch in algorithm_text]
        image_dict, self.rows, self.cols = read_map_dict_of_sets_of_points(image_text)
        self.init_image = image_dict["#"]

    def enhance(self, iterations):
        image = self.init_image
        top, bottom = 0, self.rows
        left, right = 0, self.cols
        default_value = 0

        for _ in range(iterations):
            output_image = set()
            for p in Point.loop(left - 1, right + 1, top - 1, bottom + 1):
                code = 0
                for n in p.n9():
                    if top <= n.y < bottom and left <= n.x < right:
                        pixel = 1 if n in image else 0
                    else:
                        pixel = default_value
                    code = code * 2 + pixel
                if self.code[code]:
                    output_image.add(p)
            image = output_image

            top -= 1
            bottom += 1
            left -= 1
            right += 1

            default_value = self.code[-1] if default_value else self.code[0]
        return len(image)


if __name__ == "__main__":
    data = get_input_data(__file__)

    test1 = TrenchMap("sample1.txt")
    assert test1.enhance(2) == 35
    assert test1.enhance(50) == 3351

    trench_map = TrenchMap(data.input_file)
    print(trench_map.enhance(2))
    print(trench_map.enhance(50))
