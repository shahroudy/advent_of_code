import re
from collections import namedtuple
from pathlib import Path

from myutils.io_handler import get_input_data
from myutils.search import Search_MinHeap

State = namedtuple(
    "State", ["spent_mana", "hit", "mana", "boss_hit", "shield", "poison", "recharge"]
)


class WizardSimulator20XX(Search_MinHeap):

    def __init__(self, filename=None, initial_state=None, **kwargs):
        if initial_state is None:
            boss_hit, boss_damage = (
                map(int, re.findall(r"\d+", Path(filename).read_text())) if filename else (0, 0)
            )
            initial_state = State(0, 50, 500, boss_hit, 0, 0, 0)
            kwargs["boss_damage"] = boss_damage

        super().__init__(initial_state, **kwargs)

    def get_next_states(self, state):
        next_states = []
        needed_mana_for_actions = [53, 73, 113, 173, 229]
        # consider all the possible actions, next state will be the result of player's+boss' action
        for action in range(5):
            spent_mana, hit, mana, boss_hit, shield, poison, recharge = state

            if self.args.get("hard_mode", False):
                hit -= 1
                if hit <= 0:
                    continue  # player lost

            # apply effects
            shield = max(0, shield - 1)
            if poison > 0:
                boss_hit -= 3
                poison -= 1
            if recharge > 0:
                mana += 101
                recharge -= 1

            # player's action
            needed_mana = needed_mana_for_actions[action]
            if mana < needed_mana:
                continue  # not enough mana, player lost
            spent_mana += needed_mana
            mana -= needed_mana

            if action == 0:
                # Magic Missile costs 53 mana. It instantly does 4 damage.
                boss_hit -= 4
            elif action == 1:
                # Drain costs 73 mana. It instantly does 2 damage and heals you for 2 hit points.
                boss_hit -= 2
                hit += 2
            elif action == 2:
                # Shield costs 113 mana. It starts an effect that lasts for 6 turns.
                # While it is active, your armor is increased by 7.
                if shield > 0:
                    continue  # shield is already active
                shield = 6
            elif action == 3:
                # Poison costs 173 mana. It starts an effect that lasts for 6 turns.
                # At the start of each turn while it is active, it deals the boss 3 damage.
                if poison > 0:
                    continue  # poison is already active
                poison = 6
            elif action == 4:
                # Recharge costs 229 mana. It starts an effect that lasts for 5 turns.
                # At the start of each turn while it is active, it gives you 101 new mana.
                if recharge > 0:
                    continue  # recharge is already active
                recharge = 5

            # apply effects
            shield = max(0, shield - 1)
            if poison > 0:
                boss_hit -= 3
                poison -= 1
            if recharge > 0:
                mana += 101
                recharge -= 1

            # boss' action
            armor = 7 if shield > 0 else 0
            if boss_hit > 0:
                hit -= max(1, self.args["boss_damage"] - armor)
            if hit <= 0:
                continue  # player lost
            next_states.append(State(spent_mana, hit, mana, boss_hit, shield, poison, recharge))
        return next_states

    def is_goal(self, state):
        if state.boss_hit <= 0 or state.boss_hit <= 3 and state.poison > 0:
            return True

    def get_result(self, state):
        return state[0]


if __name__ == "__main__":
    data = get_input_data(__file__)

    test1 = WizardSimulator20XX(initial_state=State(0, 10, 250, 13, 0, 0, 0), boss_damage=8)
    assert test1.search() == 53 + 173
    test2 = WizardSimulator20XX(initial_state=State(0, 10, 250, 14, 0, 0, 0), boss_damage=8)
    assert test2.search() == 229 + 113 + 73 + 173 + 53

    print("Tests passed, starting with the puzzle")

    print(WizardSimulator20XX(data.input_file).search())
    print(WizardSimulator20XX(data.input_file, hard_mode=True).search())
