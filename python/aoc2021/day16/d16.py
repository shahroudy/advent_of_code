import os
from functools import reduce
from pathlib import Path
from myutils.io_handler import get_input_data


class PacketDecoder:
    def __init__(self, filename=None, input=None):
        if not input:
            self.lines = Path(filename).read_text().strip().split("\n")
            input = self.lines[0]
        self.code = bin(int(input, 16))[2:].zfill(len(input) * 4)
        self.process()

    def process(self):
        self.sum_versions = 0
        self.result, _ = self.evaluate(self.code)

    def operation(self, typeid, vals):
        if typeid == 0:
            return sum(vals)
        if typeid == 1:
            return reduce(lambda x, y: x * y, vals)
        if typeid == 2:
            return min(vals)
        if typeid == 3:
            return max(vals)
        assert len(vals) == 2
        if typeid == 5:
            return 1 if vals[0] > vals[1] else 0
        if typeid == 6:
            return 1 if vals[0] < vals[1] else 0
        if typeid == 7:
            return 1 if vals[0] == vals[1] else 0

    def evaluate(self, packet):
        head = 0
        version = int(packet[head : head + 3], 2)
        self.sum_versions += version
        typeID = int(packet[head + 3 : head + 6], 2)
        head += 6
        if typeID != 4:
            length_type_id = packet[head]
            head += 1
            operands = []
            if length_type_id == "0":
                total_len = int(packet[head : head + 15], 2)
                head += 15
                newpacket = packet[head : head + total_len]
                head += total_len
                sub_head = 0
                while sub_head < total_len:
                    value, length = self.evaluate(newpacket[sub_head:])
                    operands.append(value)
                    sub_head += length
                return self.operation(typeID, operands), head
            else:
                no_sub_packets = int(packet[head : head + 11], 2)
                head += 11
                for _ in range(no_sub_packets):
                    value, length = self.evaluate(packet[head:])
                    operands.append(value)
                    head += length
                return self.operation(typeID, operands), head
        else:  # typeID == 4 a.k.a. literal value
            value = ""
            while head < len(packet):
                flag_bit = packet[head]
                binary = packet[head + 1 : head + 5]
                value = value + binary
                head += 5
                if flag_bit == "0":
                    break
            return int(value, 2), head


if __name__ == "__main__":
    data = get_input_data(__file__)

    test1 = PacketDecoder(input="D2FE28")
    assert test1.result == 2021

    test2 = PacketDecoder(input="38006F45291200")
    assert test2.sum_versions == 9

    test3 = PacketDecoder(input="EE00D40C823060")
    assert test3.sum_versions == 14

    test4 = PacketDecoder(input="8A004A801A8002F478")
    assert test4.sum_versions == 16

    test5 = PacketDecoder(input="620080001611562C8802118E34")
    assert test5.sum_versions == 12

    test6 = PacketDecoder(input="C0015000016115A2E0802F182340")
    assert test6.sum_versions == 23

    test7 = PacketDecoder(input="A0016C880162017C3686B18A3D4780")
    assert test7.sum_versions == 31

    test8 = PacketDecoder(input="C200B40A82")
    assert test8.result == 3

    test9 = PacketDecoder(input="04005AC33890")
    assert test9.result == 54

    test10 = PacketDecoder(input="880086C3E88112")
    assert test10.result == 7

    test11 = PacketDecoder(input="CE00C43D881120")
    assert test11.result == 9

    test12 = PacketDecoder(input="D8005AC2A8F0")
    assert test12.result == 1

    test13 = PacketDecoder(input="F600BC2D8F")
    assert test13.result == 0

    test14 = PacketDecoder(input="9C005AC2F8F0")
    assert test14.result == 0

    test15 = PacketDecoder(input="9C0141080250320F1802104A08")
    assert test15.result == 1

    packet_decoder = PacketDecoder(filename=input_file)
    print(packet_decoder.sum_versions, packet_decoder.result)
