from numpy import exp, dot


class Brain(object):

    def __init__(self, weights):
        self.layer1_weights = [
            tuple(weights[0:2]),
            tuple(weights[2:4])
        ]
        self.layer2_weights = [
            tuple(weights[4:6]),
            tuple(weights[6:8])
        ]
        self.layer3_weights = tuple(weights[8:10])

    def __sigmoid(self, x):
        """Output a value from 0 to 1"""
        return 1 / (1 + exp(-x))

    def __layer_1(self, input):
        return (
            self.__sigmoid(dot(input, self.layer1_weights[0])),
            self.__sigmoid(dot(input, self.layer1_weights[1]))
        )

    def __layer_2(self, input):
        return (
            self.__sigmoid(dot(input, self.layer2_weights[0])),
            self.__sigmoid(dot(input, self.layer2_weights[1]))
        )

    def __layer_3(self, input):
        return self.__sigmoid(dot(input, self.layer3_weights))

    def representation(self):
        return self.weights

    def think(self, params):
        """The input should be the distance to the borders."""
        layer_1_out = self.__layer_1(params)
        layer_2_out = self.__layer_2(layer_1_out)
        layer_3_out = self.__layer_3(layer_2_out)
        return layer_3_out
