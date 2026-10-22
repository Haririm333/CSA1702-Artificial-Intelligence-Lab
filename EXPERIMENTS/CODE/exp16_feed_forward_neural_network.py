import math
import random

def sigmoid(x):
    return 1.0 / (1.0 + math.exp(-x))

def sigmoid_derivative(output):
    return output * (1.0 - output)

random.seed(42)

# XOR Dataset
X = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
]
y = [0, 1, 1, 0]

# Network architecture: 2 Inputs, 2 Hidden Neurons, 1 Output Neuron
weights_input_hidden = [[random.uniform(-1, 1) for _ in range(2)] for _ in range(2)]
bias_hidden = [random.uniform(-1, 1) for _ in range(2)]

weights_hidden_output = [random.uniform(-1, 1) for _ in range(2)]
bias_output = random.uniform(-1, 1)

learning_rate = 0.5
epochs = 10000

for epoch in range(epochs):
    total_loss = 0
    for inputs, target in zip(X, y):
        # Forward pass
        hidden_inputs = [
            sum(inputs[i] * weights_input_hidden[i][h] for i in range(2)) + bias_hidden[h]
            for h in range(2)
        ]
        hidden_outputs = [sigmoid(val) for val in hidden_inputs]

        final_input = sum(hidden_outputs[h] * weights_hidden_output[h] for h in range(2)) + bias_output
        final_output = sigmoid(final_input)

        error = target - final_output
        total_loss += error ** 2

        # Backward pass
        output_delta = error * sigmoid_derivative(final_output)

        hidden_deltas = [
            output_delta * weights_hidden_output[h] * sigmoid_derivative(hidden_outputs[h])
            for h in range(2)
        ]

        # Update weights and biases
        for h in range(2):
            weights_hidden_output[h] += learning_rate * output_delta * hidden_outputs[h]
        bias_output += learning_rate * output_delta

        for i in range(2):
            for h in range(2):
                weights_input_hidden[i][h] += learning_rate * hidden_deltas[h] * inputs[i]
            bias_hidden[h] += learning_rate * hidden_deltas[h]

print("Trained Feedforward Neural Network on XOR:")
for inputs, target in zip(X, y):
    hidden_inputs = [
        sum(inputs[i] * weights_input_hidden[i][h] for i in range(2)) + bias_hidden[h]
        for h in range(2)
    ]
    hidden_outputs = [sigmoid(val) for val in hidden_inputs]
    final_input = sum(hidden_outputs[h] * weights_hidden_output[h] for h in range(2)) + bias_output
    pred = sigmoid(final_input)
    print(f"Input: {inputs} -> Target: {target} | Predicted: {pred:.4f} -> Round: {round(pred)}")
