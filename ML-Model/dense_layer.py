import numpy as np
from base_layer import Layer

class Dense(Layer):
    def __init__(self, input_size, output_size):   #initializing input and output neurons
        self.weights = np.random.randn(output_size, input_size) #initializing bias and weights as random numbers (will change in the future)
        self.bias = np.random.randn(output_size, 1)

    def forward(self, input):
        self.input = input
        return np.dot(self.weights, self.input) + self.bias

    def backward(self, output_gradient, learning_rate): #calculates the derivative of the error wrt the weights
        weights_gradient = np.dot(output_gradient, self.input.T)   #derivative of error wrt to the basis
        input_gradient = np.dot(self.weights.T, output_gradient)    #the derivative of the error wrt to the input(for other)
        self.weights -= learning_rate * weights_gradient    #updating the paramenters with gradient decent
        self.bias -= learning_rate * output_gradient
        return input_gradient   #returns the derivative of the error wrt the input
    