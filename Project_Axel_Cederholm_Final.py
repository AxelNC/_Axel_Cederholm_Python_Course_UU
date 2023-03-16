import numpy as np

# Define the sigmoid activation function to get an output between 0 and 1, enabling learning of non-linearly separable problems
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Define the derivative of the sigmoid function
def sigmoid_derivative(x):
    return x * (1 - x)

# Define the weights of the neural network with more conventional starting values
weights = {'node_0': np.array([0.2, 0.5, -0.1, 0.9]),
           'node_1': np.array([-0.2, 0.4, 0.6, -0.4]),
           'output': np.array([0.3, -0.7, 0.1, 0.8])}

# Generate some random input data
input_data = [np.random.randn(4) for _ in range(3)]

# Define the predict_with_network() function
def predict_with_network(input_data_row, weights):

    # Calculate the value of node 0
    node_0_input = (input_data_row * weights['node_0']).sum()
    node_0_output = sigmoid(node_0_input)

    # Calculate the value of node 1
    node_1_input = (input_data_row * weights['node_1']).sum()
    node_1_output = sigmoid(node_1_input)

    # Combine the node values into an array: hidden_layer_outputs
    hidden_layer_outputs = np.array([node_0_output, node_0_output, node_1_output, node_1_output])

    # Calculate the final model output
    input_to_final_layer = (hidden_layer_outputs * weights['output']).sum()
    model_output = sigmoid(input_to_final_layer)

    # Return the model output
    return model_output

# Create an empty list to store prediction results
results = []
for input_data_row in input_data:
    # Append the prediction to the results list
    results.append(predict_with_network(input_data_row, weights))

# Print the results
print(results)
