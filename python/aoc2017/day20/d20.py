import re
from copy import deepcopy
from pathlib import Path

from myutils.io_handler import get_input_data


class ParticleSwarm:
    def __init__(self, filename):
        lines = Path(filename).read_text().splitlines()
        self.particles = [list(map(int, re.findall(r"-?\d+", line))) for line in lines]

    def closest_particle(self):
        particles = deepcopy(self.particles)
        sum_distances = {i: 0 for i in range(len(particles))}
        for _ in range(1000):
            for i in range(len(particles)):
                for j in range(3):
                    particles[i][3 + j] += particles[i][6 + j]
                    particles[i][j] += particles[i][3 + j]
                sum_distances[i] += sum(abs(x) for x in particles[i][:3])
        return sorted(sum_distances.items(), key=lambda x: x[1])[0][0]

    def count_no_colliding_particles(self):
        particles = deepcopy(self.particles)
        existing_particles = set(range(len(particles)))
        for _ in range(1000):
            colliding_particles = set()
            current_positions = {}
            for i in existing_particles:
                for j in range(3):
                    particles[i][3 + j] += particles[i][6 + j]
                    particles[i][j] += particles[i][3 + j]
                position = tuple(particles[i][:3])
                if position in current_positions:
                    colliding_particles.add(i)
                    colliding_particles.add(current_positions[position])
                else:
                    current_positions[position] = i
            existing_particles -= colliding_particles
        return len(existing_particles)


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert ParticleSwarm("sample1.txt").closest_particle() == 0
    assert ParticleSwarm("sample2.txt").count_no_colliding_particles() == 1

    print("Tests passed, starting with the puzzle")

    puzzle = ParticleSwarm(data.input_file)

    print(puzzle.closest_particle())
    print(puzzle.count_no_colliding_particles())
