import numpy as np
from Perceptron1 import Perceptron 

training_inputs=[]
#training_inputs.append(np.array([1,1,1]))
#training_inputs.append(np.array([1,0,1]))
#training_inputs.append(np.array([1,1,0]))
training_inputs.append(np.array([0,0,0]))
training_inputs.append(np.array([1,0,0]))
training_inputs.append(np.array([0,1,0]))
training_inputs.append(np.array([0,1,1]))
training_inputs.append(np.array([0,0,1]))

labels = np.array([0,0,0,0,0])

perceptron = Perceptron(3)
perceptron.train(training_inputs,labels)

inputs = np.array([1,1,0])
print(perceptron.predict(inputs))
if (perceptron.predict(inputs)  == 1):
    print("should buy")
else:
    print("shouldn't buy")
print(perceptron.weights)
