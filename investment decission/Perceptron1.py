import numpy as np

class Perceptron(object):
    def __init__(self,no_of_inputs,threshold=10000,learning_rate=.001):
    
        self.threshold=threshold
        self.learning_rate=learning_rate
        self.weights=np.zeros(no_of_inputs + 1)
    
    def predict(self,inputs):
        summation=np.dot(inputs,self.weights[1:])+self.weights[0]           #w.x+b
        if summation > 0:
            activation = 1
        else:
            activation = 0
        if(activation == 1):
            print("should invest")
        else:
            print("shouldn't invest")
        return activation
    
    def train(self,training_inputs,labels):
        print("Threshold \t Prediction \t\t Weights")
        print("=================================================================")
       
        for _ in range(self.threshold):
            test = []
            L = []
            for inputs,label in zip(training_inputs,labels):
                prediction=self.predict(inputs)
                self.weights[1:]+=self.learning_rate*(label-prediction)*inputs
                self.weights[0]+=self.learning_rate*(label-prediction)
                test.append(prediction)
                L.append(label)
                print(_,end=" \t\t\t ")
                print(prediction, end= " \t\t\t ")
                print(self.weights)

                if (len(test) == len(L)):
                    count = 0
                    if(test == L):
                        count += 1
            if(count>0):
                break    
                     
        print("threshold stoped:",end= " " )
        print(_)
        
        print("=================================================================")