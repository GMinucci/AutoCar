import matplotlib.pyplot as plotter

a = [31.582630833743661, 30.298398096866453, 28.871041632519706, 28.457177910159142]
b = [518, 546, 533, 535]


class Plotter():

    fitness_list = []
    # mutation_amount_list = []

    def add_fitness(self, fit):
        self.fitness_list.append(fit)

    # def add_mutation(self, amount):
    #     self.mutation_amount_list.append(amount)

    def show(self):
        generations = range(len(self.fitness_list))

        f, axarr = plotter.subplots(2, sharex=True)
        axarr[0].plot(generations, self.fitness_list, 'b-')
        axarr[0].set_title('Fittest X Generations')
        # axarr[1].plot(generations, self.mutation_amount_list, 'r-')
        # axarr[1].set_title('Mutations X Generations')

        plotter.show()

# from plotter import *
# p = Plotter()
# p.fitness_list = a
# p.mutation_amount_list = b
# p.show()
