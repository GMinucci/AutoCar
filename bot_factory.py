import os
import subprocess
import json
import numpy as np
import random as rand
from numpy.random import random
from itertools import combinations, repeat
from settings import default_settings
from plotter import Plotter


class BotFactory():

    settings = None
    mutation_count = 0

    def __init__(self, settings):
        self.settings = settings

    def run_test(self, bot_weights):
        # write to file
        with open('weights.txt', 'w') as outfile:
            if isinstance(bot_weights, (np.ndarray, np.generic)):
                json.dump({"weights":bot_weights.tolist()}, outfile)
            else:
                json.dump({"weights":bot_weights}, outfile)
            outfile.close()

        # run simulation
        simulation = ['python3', 'simulate.py', '&']
        subprocess.Popen(simulation).wait()

        # return results
        score = json.load(open('score.txt'))
        return score["value"]

    def reproduce(self, bot1, bot2, amount=None):
        """
        Reproduce two bots and return the new bots weight.
        Each reproduction create 2*<number_of_weights>
        Return an list of bot seeds
        """
        nw = len(bot1)
        new_bot_seeds = []
        for i in range(1, nw):
            new_bot_seeds.append(self.mutate(
                list(bot1[:i]) +
                list(bot2[-(nw-i):])
            ))
            new_bot_seeds.append(self.mutate(
                list(bot2[:i]) +
                list(bot1[-(nw-i):])
            ))
        new_bot_seeds.append(self.mutate(bot1))
        new_bot_seeds.append(self.mutate(bot2))
        if amount is None:
            return new_bot_seeds
        else:
            return rand.sample(new_bot_seeds, amount)

    def mutate(self, weights):
        """
        For each weight can generate a mutation with mutation_rate chance.
        To mutate generate a random number between -1 and 1
        and add mutation_factor of it into the weights.
        """
        new_weights = weights
        for i in range(len(weights)):
            if random() < self.settings.mutation_rate:
                self.mutation_count = self.mutation_count + 1
                mutation = self.settings.mutation_factor * \
                    (2 * random() - 1)
                new_weights[i] = weights[i] + mutation
        return new_weights

    def run_generation(self, initial_bots):
        bots = []
        new_weights = []
        for bot1, bot2 in combinations(initial_bots, 2):
            new_weights.extend(self.reproduce(bot1, bot2, 20))
        print(len(new_weights))
        for weights in new_weights:
            bots.append((weights, self.run_test(weights)))
        return bots


if __name__ == "__main__":
    factory = BotFactory(default_settings)
    plotter = Plotter()
    bots = []

    if factory.settings.initial_seed is not None:
        initial_bot_weights = repeat(factory.settings.initial_seed, 10)
        for weights in initial_bot_weights:
            bots.append((weights, 99.0))
    else:
        initial_bot_weights = (2 * random((10, 10))) - 1
        for weights in initial_bot_weights:
            bots.append((weights, factory.run_test(weights)))

    for i in range(factory.settings.generation_amount):
        sorted_bots = sorted(bots, key=lambda tup: tup[1], reverse=True)[:2]
        bots = [value[0] for value in sorted_bots]
        print("------------")
        print("GENERATION %s" % i)
        print("BEST FIT: %s" % sorted_bots[0][1])
        if i % 10 == 0 and i != 0:
            print("------------")
            print("Current best bot: \n%s" % sorted_bots[0][0])
        plotter.add_fitness(sorted_bots[0][1])
        plotter.add_mutation(factory.mutation_count)
        factory.mutation_count = 0
        bots = factory.run_generation(bots)
        print("AMOUNT: %s" % len(bots))
        if sorted_bots[0][1] < factory.settings.approach_change_parameter:
            factory.settings.change_approach()

    final = sorted(bots, key=lambda tup: tup[1], reverse=True)[:1][0]
    print("-----------")
    print("-- Final --")
    print("Fitness: %s" % final[1])
    print("Best bot: \n%s" % final[0])
    plotter.show()
    factory.save_to_csv(bots, "final_generation.csv")
