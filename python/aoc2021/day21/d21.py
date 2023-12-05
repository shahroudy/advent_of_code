from collections import defaultdict
from itertools import product, permutations


class DiracDice:
    def __init__(self, player_1_start, player_2_start):
        self.start_position = [player_1_start, player_2_start]

    def deterministic_dice(self):
        dice = 1
        roll_counter = 0
        scores = [0, 0]
        pos = self.start_position.copy()
        while True:
            for player in [0, 1]:
                for _ in range(3):
                    pos[player] += dice
                    while pos[player] > 10:
                        pos[player] -= 10
                    dice += 1
                    roll_counter += 1
                    if dice > 100:
                        dice = 1
                scores[player] += pos[player]
                if scores[player] >= 1000:
                    return scores[1 - player] * roll_counter

    def quantum_dice(self):
        triple_roll_combinations = defaultdict(int)
        for i, j, k in product(range(1, 4), repeat=3):
            triple_roll_combinations[i + j + k] += 1

        pos = self.start_position
        score = [0, 0]
        wins = [0, 0]
        states = [[*pos, *score, 1]]

        while states:
            for player in [0, 1]:
                middle_states = list()
                while states:
                    curstate = states.pop()
                    for d, dc in triple_roll_combinations.items():
                        pos[0], pos[1], score[0], score[1], freq = curstate
                        pos[player] += d
                        if pos[player] > 10:
                            pos[player] -= 10
                        score[player] += pos[player]
                        if score[player] >= 21:
                            wins[player] += freq * dc
                        else:
                            middle_states.append([*pos, *score, dc * freq])
                states = middle_states
        return max(wins)


if __name__ == "__main__":
    test1 = DiracDice(4, 8)
    assert test1.deterministic_dice() == 739785
    assert test1.quantum_dice() == 444356092776315

    dirac_dice = DiracDice(8, 3)
    print(dirac_dice.deterministic_dice())
    print(dirac_dice.quantum_dice())
