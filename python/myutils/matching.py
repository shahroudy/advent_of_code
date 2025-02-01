from functools import reduce


def find_match_dict(connections):
    result = dict()
    remaining_keys = set(connections.keys())
    remaining_values = reduce(set.union, connections.values())
    while remaining_keys:
        for key in remaining_keys:
            valid_values = connections[key] & remaining_values
            if len(valid_values) == 1:
                value = valid_values.pop()
                result[key] = value
                break
        else:
            raise Exception("No match found")
        remaining_values.remove(value)
        remaining_keys.remove(key)
    return result


if __name__ == "__main__":
    test1 = {0: {0, 1, 2, 3}, 1: {0, 1, 2}, 2: {0, 2}, 3: {0}}
    assert find_match_dict(test1) == {0: 3, 1: 1, 2: 2, 3: 0}
    test2 = {2: {0, 1, 2, 3}, 0: {0, 1, 2}, 1: {0, 2}, 3: {0}}
    assert find_match_dict(test2) == {0: 1, 1: 2, 2: 3, 3: 0}
