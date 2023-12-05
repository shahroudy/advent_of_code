def find_a_mapping(connections):
    """
    Finds a full mapping between two sets of nodes (left and right).
    Compatible right nodes for each left node is provided in 'connections'.
    connections is a list of lists, each item of the list will consist
    of a scalar (index of the left node) and a list of indexes of connected
    right nodes.
    Left and right nodes must be zero-based indexes.
    """

    # sort the connection list to start with the most limiting ones
    connections = sorted(connections, key=lambda x: len(x[1]))

    size = len(connections)

    current_match = [-1] * size
    result = [-1] * size
    head = 0
    while head < size:
        left_index, matched_columns = connections[head]

        while current_match[head] < 0 or (
            current_match[head] < len(matched_columns)
            and matched_columns[current_match[head]] in result
        ):
            current_match[head] += 1

        if current_match[head] == len(matched_columns):
            # no match is found from this branch, so backtrack
            current_match[head] = -1
            head -= 1
            result[connections[head][0]] = -1
            current_match[head] += 1
        else:
            result[left_index] = matched_columns[current_match[head]]
            head += 1
    return result


test1 = [[0, [0, 1, 2, 3]], [1, [0, 1, 2]], [2, [0, 2]], [3, [0]]]
assert find_a_mapping(test1) == [3, 1, 2, 0]
test2 = [[2, [0, 1, 2, 3]], [0, [0, 1, 2]], [1, [0, 2]], [3, [0]]]
assert find_a_mapping(test2) == [1, 2, 3, 0]
