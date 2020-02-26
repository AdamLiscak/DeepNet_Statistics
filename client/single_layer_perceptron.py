'''
 000 1
 001 1
 010 0
 011 0
 100 1
 101 1
 110 0
 111 0

'''
import numpy as np

should_results = np.array([0,0,0,0,0,0,1,1])
inputs = np.array([
        [0,0,0],
        [0,0,1],
        [0,1,0],
        [0,1,1],
        [1,0,0],
        [1,0,1],
        [1,1,0],
        [1,1,1]
        ])
class Perceptron:

    weights = np.array([ 0.4 , -0.2, 0.7 ])
    alpha = 0.1

    def predict(self,input):
        return np.dot(self.weights,input)

    def getDelta(self,prediction,goal_prediction):
        return prediction-goal_prediction

    def getError(self,delta):
        return delta**2

    
    def learn(self, inputs,should_results):
        error_sum = 0
        for i in range(len(should_results)):
            input = inputs[i]
            should_result = should_results[i]
            prediction = np.dot(input,self.weights)
            delta = prediction-should_result 
            error = self.getError(delta)
            print("delta "+str(input*delta))
            error_sum += error 
            self.weights = self.weights  - (self.alpha * (input * delta) )
        print(error_sum)
class meth:
    def relu(x):
        return( x > 0 ) * x
    def reluderiv(x):
        return( x > 0 )
        
class DeepNet2:
    alpha = 0.05
    weights = np.array(
            [
            np.array([[0.4,-0.2,0.7,0.4],[-0.5,-0.9,0.1,0],[1,-0.4,0.3,0.2]]),
            np.array([[0.3],[0.6],[-0.2],[0.8]])
            ]
            )
    def predict(self,input):
        print(layer_0)
    def learn(self,inputs,should_results):
        layer_2_err = 0
        for i in range(len(should_results)):
            should_result = should_results[i:i+1]
            layer_0 = inputs[i:i+1]
            layer_1 = meth.relu(np.dot(layer_0,self.weights[0]))
            layer_2 = np.dot(layer_1,self.weights[1])
         #   print(layer_2)
            layer_2_delta = layer_2 -should_result
            layer_2_err += layer_2_delta**2

            layer_1_delta  = np.dot(layer_2_delta,self.weights[1].T)*meth.reluderiv(layer_1)

            self.weights[1] -= self.alpha * layer_1.T.dot(layer_2_delta)
            self.weights[0] -= self.alpha * layer_0.T.dot(layer_1_delta)

        print(self.weights)


#n = Perceptron()
'''
for i in range (30):
    n.learn(inputs,should_results)
    print(n.weights)
'''
m = DeepNet2()
for j in range (60):
    m.learn(inputs, should_results)

