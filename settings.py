

class Settings(object):

    # def __init__(self, initial_seed=None, mutation_rate=0.8,
    #     mutation_factor=0.5, generation_amount=50, should_normalize=True,
    #     normalization_factor=255.0):
    #     self.initial_seed = initial_seed
    #     self.mutation_rate = mutation_rate
    #     self.mutation_factor = mutation_factor
    #     self.generation_amount = generation_amount
    #     self.should_normalize = should_normalize
    #     self.normalization_factor = normalization_factor

    # initial_seed can be used to start using an previous individual instead of
    # generating random ones. If you want to start with random individuals set
    # this to None
    initial_seed = None

    # mutation_rate determine the amount of mutation per gene in the DNA
    # written in decimal from 0 to 1
    mutation_rate = 0.5

    # mutation_factor determine how hard the mutation occurs, from 0 to 1
    mutation_factor = 0.5

    # amount of generation to run. Too many generations can cause longer runs.
    # Too little generations can not end with a good specie
    generation_amount = 30

    # configure to change if want to normalize the input data
    should_normalize = False

    # set the value in wich all input is divided by. Shouldn't be an integer
    # to not loose the input data integrity
    normalization_factor = 255.0

    # if active use two different mutation_rate and mutation_factor to
    # accelerate the convergence of the fitness
    can_change_reach_approach = False
    approach_change_parameter = 10

    def change_approach(self):
        if self.can_change_reach_approach:
            self.mutation_rate = 0.1
            self.mutation_factor = 0.1
            print("Approach changed. Now with %s mutation rate and %s " \
                "mutation factor" % (self.mutation_rate, self.mutation_factor))
            self.can_change_reach_approach = False

default_settings = Settings()
