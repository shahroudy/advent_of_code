from pathlib import Path

from myutils.io_handler import get_input_data
from myutils.utils import multiply


class PacketDecoder:
    def __init__(self, filename):
        bits_list = []
        for hex_digit in Path(filename).read_text().strip():
            decimal_value = int(hex_digit, 16)
            four_bit_binary = bin(decimal_value)[2:].zfill(4)
            bits_list.append(four_bit_binary)
        self.bits = "".join(bits_list)
        self.head = 0
        self.sum_of_packet_versions = 0
        self.packets = self.read_packets()

    def read_bits(self, bit_count):
        bits = self.bits[self.head : self.head + bit_count]
        self.head += bit_count
        return bits

    def read_int_from_bits(self, bit_count):
        bits = self.read_bits(bit_count)
        return int(bits, 2)

    def is_end_of_stream(self, size_limit=None):
        size_limit = size_limit or len(self.bits)
        return self.head >= size_limit or all(
            bit == "0" for bit in self.bits[self.head : size_limit]
        )

    def read_packets(self, number_of_packets=None, size_limit=None):
        target_head = self.head + size_limit if size_limit is not None else None
        packets = []
        while not self.is_end_of_stream(target_head) and (
            number_of_packets is None or len(packets) < number_of_packets
        ):
            packet_version, packet_type = self.read_int_from_bits(3), self.read_int_from_bits(3)
            self.sum_of_packet_versions += packet_version
            if packet_type == 4:
                is_last_group = False
                value_bits_list = ["0b"]
                while not is_last_group:
                    is_last_group = self.read_int_from_bits(1) == 0
                    value_bits_list.append(self.read_bits(4))
                value = int("".join(value_bits_list), 2)
            else:
                length_type_id = self.read_int_from_bits(1)
                if length_type_id == 0:
                    total_length_in_bits = self.read_int_from_bits(15)
                    sub_packets = self.read_packets(size_limit=total_length_in_bits)
                else:
                    sub_packet_count = self.read_int_from_bits(11)
                    sub_packets = self.read_packets(number_of_packets=sub_packet_count)
                match packet_type:
                    case 0:
                        value = sum(sub_packets)
                    case 1:
                        value = multiply(sub_packets)
                    case 2:
                        value = min(sub_packets)
                    case 3:
                        value = max(sub_packets)
                    case 5:
                        value = int(sub_packets[0] > sub_packets[1])
                    case 6:
                        value = int(sub_packets[0] < sub_packets[1])
                    case 7:
                        value = int(sub_packets[0] == sub_packets[1])
            packets.append(value)
        return packets

    def root_packet_value(self):
        return self.packets[0]


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert PacketDecoder("sample1.txt").sum_of_packet_versions == 6
    assert PacketDecoder("sample2.txt").sum_of_packet_versions == 16
    assert PacketDecoder("sample3.txt").sum_of_packet_versions == 12
    assert PacketDecoder("sample4.txt").sum_of_packet_versions == 23
    assert PacketDecoder("sample5.txt").sum_of_packet_versions == 31

    assert PacketDecoder("sample1.txt").root_packet_value() == 2021
    assert PacketDecoder("sample6.txt").root_packet_value() == 3
    assert PacketDecoder("sample7.txt").root_packet_value() == 54
    assert PacketDecoder("sample8.txt").root_packet_value() == 7
    assert PacketDecoder("sample9.txt").root_packet_value() == 9
    assert PacketDecoder("sample10.txt").root_packet_value() == 1
    assert PacketDecoder("sample11.txt").root_packet_value() == 0
    assert PacketDecoder("sample12.txt").root_packet_value() == 0
    assert PacketDecoder("sample13.txt").root_packet_value() == 1

    print("Tests passed, starting with the puzzle")

    puzzle = PacketDecoder(data.input_file)

    print(puzzle.sum_of_packet_versions)
    print(puzzle.root_packet_value())
