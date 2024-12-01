import os
from myutils.file_reader import read_lines
from myutils.io_handler import get_input_data


class BinaryDiagnostic:
    def __init__(self, filename):
        lines = read_lines(filename)
        self.digits = [list(line) for line in lines]
        self.digit_len = len(self.digits[0])

    def power_consumption(self):

        current_digits = self.digits.copy()

        gamma_rate = ""
        epsilon_rate = ""
        for i in range(self.digit_len):
            one_count = 0
            zero_count = 0
            for digits in current_digits:
                if digits[i] == "1":
                    one_count += 1
                else:
                    zero_count += 1
            if one_count > zero_count:
                gamma_rate = gamma_rate + "1"
                epsilon_rate = epsilon_rate + "0"
            else:
                gamma_rate = gamma_rate + "0"
                epsilon_rate = epsilon_rate + "1"
        return int(gamma_rate, 2) * int(epsilon_rate, 2)

    def life_support_rating(self):

        # calculate oxygen_generator_rating
        current_digits = self.digits.copy()
        for i in range(self.digit_len):
            one_count = 0
            zero_count = 0
            for digits in current_digits:
                if digits[i] == "1":
                    one_count += 1
                else:
                    zero_count += 1

            new_digits = []
            for digits in current_digits:
                if (digits[i] == "1") ^ (one_count < zero_count):
                    new_digits.append(digits)

            if len(new_digits) == 1:
                oxygen_generator_rating = int("".join(new_digits[0]), 2)
                break
            current_digits = new_digits

        # calculate co2_generator_rating
        current_digits = self.digits.copy()
        for i in range(len(current_digits[0])):
            one_count = 0
            zero_count = 0
            for digits in current_digits:
                if digits[i] == "1":
                    one_count += 1
                else:
                    zero_count += 1

            new_digits = []
            for digits in current_digits:
                if (digits[i] == "1") ^ (one_count >= zero_count):
                    new_digits.append(digits)

            if len(new_digits) == 1:
                co2_scrubber_rating = int("".join(new_digits[0]), 2)
                break
            current_digits = new_digits

        return oxygen_generator_rating * co2_scrubber_rating


if __name__ == "__main__":
    data = get_input_data(__file__)
    test1 = BinaryDiagnostic("test1.txt")
    assert test1.power_consumption() == 198
    assert test1.life_support_rating() == 230

    binary_diagnostic = BinaryDiagnostic(data.input_file)
    print(binary_diagnostic.power_consumption())
    print(binary_diagnostic.life_support_rating())
