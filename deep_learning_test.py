# -*- coding: utf-8 -*-
"""deep learning test.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lXzZ5yGEO4_5LmpkKi7bdjoD1TZ7khvY
"""



"""1. What is the fundamental difference between shallow and deep learning
Shallow networks typically have only one or two hidden layers, while deep networks can have dozens or even hundreds of layers. The increased depth allows deep neural networks to capture more complex patterns in the input data, leading to improved accuracy and performance.

2. Can you explain the concept of backpropagation and its significance in training neural networks?
In machine learning, backpropagation is an effective algorithm used to train artificial neural networks, especially in feed-forward neural networks. Backpropagation is an iterative algorithm, that helps to minimize the cost function by determining which weights and biases should be adjusted.

3. What is the vanishing gradient problem, and how does it affect training in deep neural networks?
The vanishing gradient problem can severely impact the training process of a neural network. Since the weights in the earlier layers receive minimal updates, these layers learn very slowly, if at all. This can result in a network that does not perform well on the training data, leading to poor generalization to new, unseen data.


4. Describe the purpose and function of activation functions in neural networks.
The purpose of activation functions in neural networks is:
Introduce non-linearity into the output of a neuron.
Determine the output of a neural network model.
Affect the neural network’s ability to converge and the convergence speed.
Prevent neural networks from converging in some cases.
Output a small value for small inputs, and a larger value if its inputs exceed a threshold.
"Fire" if the inputs are large enough, otherwise do nothing.


5. What are some common activation functions used in deep learning, and when would you choose one over another?
ReLU. The ReLU function is another non-linear activation function that has gained popularity in the deep learning domain

 Sigmoid Function
The sigmoid function is also known as the squashing function, as it takes the input from the previously hidden layer and squeezes it between 0 and 1. So a value fed to the sigmoid function will always return a value between 0 and 1, no matter how big or small the value is fed.

tanh function:
The tanh function is a smooth and continuous function, meaning that its derivatives are well-defined and continuous. This property can facilitate gradient-based optimization algorithms like backpropagation, leading to more stable and efficient training of neural networks2.

Leaky ReLU, is a type of activation function based on a ReLU, but it has a small slope for negative values instead of a flat slope. The slope coefficient is determined before training, i.e. it is not learnt during training. This type of activation function is popular in tasks where we may suffer from sparse gradients, for example training generative adversarial netwo

6. Explain the concept of overfitting in deep learning models and methods to prevent it.
There are two ways to approach an overfit model: Reduce overfitting by training the network on more examples. Reduce overfitting by changing the complexity of the network. A benefit of very deep neural networks is that their performance continues to improve as they are fed larger and larger datasets.

7. What is dropout regularization, and how does it work to prevent overfitting?
Dropout is a regularization technique which involves randomly ignoring or “dropping out” some layer outputs during training, used in deep neural networks to prevent overfitting. Dropout is implemented per-layer in various types of layers like dense fully connected, convolutional, and recurrent layers, excluding the output layer.

8. What is the role of convolutional layers in convolutional neural networks (CNNs), and how do they differ from fully connected layers?
The Convolutional layer applies filters to the input image to extract features, the Pooling layer downsamples the image to reduce computation, and the fully connected layer makes the final prediction. The network learns the optimal filters through backpropagation and gradient descent.

9. What is the purpose of pooling layers in CNNs, and how do they help in feature extraction?
Pooling layers are used to reduce the dimensions of the feature maps. Thus, it reduces the number of parameters to learn and the amount of computation performed in the network. The pooling layer summarises the features present in a region of the feature map generated by a convolution layer

10. Describe the architecture of a recurrent neural network (RNN) and its applications in sequential data analysis.
A recurrent neural network (RNN) is a network architecture for deep learning that predicts on time-series or sequential data. RNNs are particularly effective for working with sequential data that varies in length and solving problems such as natural signal classification, language processing, and video analysis.


11. Explain YoLo Algorithm in depth along with it's real life applications

YOLO is an algorithm that uses neural networks to provide real-time object detection. This algorithm is popular because of its speed and accuracy. It has been used in various applications to detect traffic signals, people, parking meters, and animals.
"""