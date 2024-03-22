# -*- coding: utf-8 -*-
"""neural networks.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/199iTWPbEgI-a00fPBq7l6-pSd1Ul9nQN
"""

Explain the architecture of Spark?

Apache Spark Architecture
Spark works in a master-slave architecture where the master is called the “Driver” and slaves are called “Workers”. When you run a Spark application, Spark Driver creates a context that is an entry point to your application, and all operations (transformations and actions) are executed on worker nodes, and the resources are managed by Cluster Manager.

Explain activation function?

Activation functions in Neural Networks.

In the process of building a neural network, one of the choices you get to make is what Activation Function to use in the hidden layer as well as at the output layer of the network. This article discusses some of the choices.

Elements of a Neural Network
Input Layer: This layer accepts input features. It provides information from the outside world to the network, no computation is performed at this layer, nodes here just pass on the information(features) to the hidden layer.

Hidden Layer: Nodes of this layer are not exposed to the outer world, they are part of the abstraction provided by any neural network. The hidden layer performs all sorts of computation on the features entered through the input layer and transfers the result to the output layer.

Output Layer: This layer bring up the information learned by the network to the outer world.



List different types of activation function with their formula?

Linear Function
Equation : Linear function has the equation similar to as of a straight line i.e. y = x
No matter how many layers we have, if all are linear in nature, the final activation function of last layer is nothing but just a linear function of the input of first layer.
Range : -inf to +inf
Uses : Linear activation function is used at just one place i.e. output layer.
Issues : If we will differentiate linear function to bring non-linearity, result will no more depend on input “x” and function will become constant, it won’t introduce any ground-breaking behavior to our algorithm.

Sigmoid Function
It is a function which is plotted as ‘S’ shaped graph.
Equation : A = 1/(1 + e-x)
Nature : Non-linear. Notice that X values lies between -2 to 2, Y values are very steep. This means, small changes in x would also bring about large changes in the value of Y.
Value Range : 0 to 1
Uses : Usually used in output layer of a binary classification, where result is either 0 or 1, as value for sigmoid function lies between 0 and 1 only so, result can be predicted easily to be 1 if value is greater than 0.5 and 0 otherwise.

Tanh Function

The activation that works almost always better than sigmoid function is Tanh function also known as Tangent Hyperbolic function. It’s actually mathematically shifted version of the sigmoid function. Both are similar and can be derived from each other.
Equation :-f(x)= tanh(x)=2/1+e^-2x-1
Value Range :- -1 to +1
Nature :- non-linear
Uses :- Usually used in hidden layers of a neural network as it’s values lies between -1 to 1 hence the mean for the hidden layer comes out be 0 or very close to it, hence helps in centering the data by bringing mean close to 0. This makes learning for the next layer much easier.

RELU Function
It Stands for Rectified linear unit. It is the most widely used activation function. Chiefly implemented in hidden layers of Neural network.
Equation :- A(x) = max(0,x). It gives an output x if x is positive and 0 otherwise.
Value Range :- [0, inf)
Nature :- non-linear, which means we can easily backpropagate the errors and have multiple layers of neurons being activated by the ReLU function.
Uses :- ReLu is less computationally expensive than tanh and sigmoid because it involves simpler mathematical operations. At a time only a few neurons are activated making the network sparse making it efficient and easy for computation


What is a neural network?
Neural Networks are computational models that mimic the complex functions of the human brain. The neural networks consist of interconnected nodes or neurons that process and learn from data, enabling tasks such as pattern recognition and decision making in machine learning. The article explores more about neural networks, their working, architecture and more.

Working of a Neural Network
Forward Propagation
Input Layer: Each feature in the input layer is represented by a node on the network, which receives input data.
Weights and Connections: The weight of each neuronal connection indicates how strong the connection is. Throughout training, these weights are changed.
Hidden Layers: Each hidden layer neuron processes inputs by multiplying them by weights, adding them up, and then passing them through an activation function. By doing this, non-linearity is introduced, enabling the network to recognize intricate patterns.
Output: The final result is produced by repeating the process until the output layer is reached.
Backpropagation
Loss Calculation: The network’s output is evaluated against the real goal values, and a loss function is used to compute the difference. For a regression problem, the Mean Squared Error (MSE) is commonly used as the cost function.
Gradient Descent: Gradient descent is then used by the network to reduce the loss. To lower the inaccuracy, weights are changed based on the derivative of the loss with respect to each weight.
Adjusting weights: The weights are adjusted at each connection by applying this iterative process, or backpropagation, backward across the network.
Training: During training with different data samples, the entire process of forward propagation, loss calculation, and backpropagation is done iteratively, enabling the network to adapt and learn patterns from the data.
Actvation Functions: Model non-linearity is introduced by activation functions like the rectified linear unit (ReLU) or sigmoid. Their decision on whether to “fire” a neuron is based on the whole weighted input.

Types of Neural Networks
Feedforward Neteworks
Multilayer Perceptron (MLP)
Convolutional Neural Network (CNN)
Recurrent Neural Network (RNN)
Long Short-Term Memory (LSTM)

# Python program to demonstrate
# hybrid inheritance


class School:
    def func1(self):
        print("This function is in school.")


class Student1(School):
    def func2(self):
        print("This function is in student 1. ")


class Student2(School):
    def func3(self):
        print("This function is in student 2.")


class Student3(Student1, School):
    def func4(self):
        print("This function is in student 3.")


# Driver's code
object = Student3()
object.func1()
object.func2()

This function is in school.
This function is in student 1.