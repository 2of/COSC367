
def construct_perceptron(weights, bias):
    """Returns a perceptron function using the given paramers."""
    def perceptron(input):
        # Complete (a line or two)
        a = sum([ (x*w) for x,w in zip(weights,input)])+bias
        return 1 if a >= 0 else  0
    
    return perceptron # this line is fine



def accuracy(classifier, inputs, expected_outputs):
    corr = 0
    for candidate,target in zip(inputs, expected_outputs):
        if classifier(candidate) == target:
            corr += 1
        
    return (corr/len(expected_outputs))
    




perceptron = construct_perceptron([-1, 3], 2)
inputs = [[1, -1], [2, 1], [3, 1], [-1, -1]]
targets = [0, 1, 1, 0]
print(accuracy(perceptron, inputs, targets))