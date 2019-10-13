
def construct_perceptron(weights, bias):
    """Returns a perceptron function using the given paramers."""
    def perceptron(input):
        # Complete (a line or two)
        a = sum([ (x*w) for x,w in zip(weights,input)])+bias
        return 1 if a >= 0 else  0
    
    return perceptron # this line is fine




def learn_perceptron_parameters(weights, bias, training_examples, learning_rate, max_epochs):
    flag = 0
    for epoch in range(max_epochs):
        if flag:
            break
        flag = 1
        for candidate,expect in training_examples:
            perceptron = construct_perceptron(weights,bias)
            output = perceptron(candidate)
            if output != expect:
                flag = 0
                for i in range(len(weights)):
                    weights[i] += learning_rate*candidate[i]*(expect-output)
           #     print(weights)
                bias += learning_rate*(expect - output)
            print(f"{epoch} : {weights}, {bias}")
    
    
    
    
    
    return [weights,bias]



# weights = [2, -4]
# bias = 0
# learning_rate = 0.5
# examples = [
#   ((0, 0), 0),
#   ((0, 1), 0),
#   ((1, 0), 0),
#   ((1, 1), 1),
#   ]
# max_epochs = 50

# weights, bias = learn_perceptron_parameters(weights, bias, examples, learning_rate, max_epochs)
# print(f"Weights: {weights}")
# print(f"Bias: {bias}\n")

# perceptron = construct_perceptron(weights, bias)

# print(perceptron((0,0)))
# print(perceptron((0,1)))
# print(perceptron((1,0)))
# print(perceptron((1,1)))
# print(perceptron((2,2)))
# print(perceptron((-3,-3)))
# print(perceptron((3,-1)))


# weights = [2, -4]
# bias = 0
# learning_rate = 0.5
# examples = [
#   ((0, 0), 0),
#   ((0, 1), 1),
#   ((1, 0), 1),
#   ((1, 1), 0),
#   ]
# max_epochs = 50

# weights, bias = learn_perceptron_parameters(weights, bias, examples, learning_rate, max_epochs)
# print(f"Weights: {weights}")
# print(f"Bias: {bias}\n")


''' This is a question that is manually done! '''
weights = [-0.5, 0.5]
bias = -0.5
learning_rate = 0.5

examples = [
    ([1, 1],   0),    # index 0 (first example)
    ([2, 0],   1),
    ([1, -1],  0),
    ([-1, -1], 1),
    ([-2, 0],  0),
    ([-1, 1],  1),

]
weights, bias = learn_perceptron_parameters(weights, bias, examples, learning_rate, 50)
print(weights,bias)