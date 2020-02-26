import numpy as np
results = np.array([0,0,0,0,0,0,1,1])
results2 = np.array([[0,0],[1,0],[1,0],[0,0],[0,0],[1,0],[1,1],[0,1]])
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
#np.random.shuffle(inputs)
print(inputs)
class Perceptron:

    weights = np.array([-0.7,-0.2,0.9])
    alpha = 0.1

    def predict(self,input):
        return np.dot(input,self.weights)
    
    def learn(self,inputs,results):
        collective_error = 0
        for i in range(len(results)):
            input = inputs[i]
            result = results[i]
            prediction = self.predict(input)
            delta = prediction - result
            error = delta**2
            collective_error += error
            self.weights -= self.alpha * (input*delta)
        
class DeepNet2:

    weights = np.array(
            [
               np.array([[0.3,-0.8,0.2,0.7],[0.9,0.5,-0.2,-0.1],[0.4,0.6,0.9,0.2]]),
                np.array([[0.3],[0.7],[-0.8],[0.4]])
            ])
    alpha = 0.1

    def predict(self,input):
        input = np.array([input])
        layer_1 = Meth.relu(np.dot(input,self.weights[0]))
        layer_2 = np.dot(layer_1,self.weights[1])
        return layer_2[0][0]

    def learn(self,inputs,results):
        collective_error_2 = 0
        for i in range(len(results)):
            result = results[i:i+1]
            layer_0 = inputs[i:i+1]
            layer_1 = Meth.relu(np.dot(layer_0,self.weights[0]))
            layer_2 = np.dot(layer_1,self.weights[1])
            
           # print("layer_0:"+str(layer_0))
            #print("layer_1:"+str(layer_1))
            #print("layer_2:"+str(layer_2))

            delta_2 = layer_2 - result
            error_2 = delta_2**2

            print("delta_2:"+str(delta_2))
             
            delta_1  = np.dot(delta_2,self.weights[1].T)*Meth.reluD(layer_1)
            ''' 
            print("delta_1:"+str(delta_1))
            print("dot:"+str(np.dot(layer_1.T,delta_2)))
            print("doto:"+str(np.dot(layer_0.T,delta_1)))
            print("layero:"+str(layer_0.T))
            '''
            self.weights[1] -= self.alpha*np.dot(layer_1.T,delta_2)
            #print(layer_0.T)
           # print(delta_1)
            self.weights[0] -= self.alpha*np.dot(layer_0.T,delta_1)
           # print(d.weights[1])
           # print(d.weights[0])
class DeepNet21:
    
    weights = np.array(
            [
               np.array([[0.3,-0.8,0.2,0.7],[0.9,0.5,-0.2,-0.1],[0.4,0.6,0.9,0.2]]),
                np.array([0.3,0.7,-0.8,0.4])
            ])
    alpha = 0.1
    
    def predict(self,input):
        layer_1 = Meth.relu(np.dot(input,self.weights[0]))
        layer_2 = np.dot(layer_1,self.weights[1])
        return layer_2
    def learn(self,inputs,results):
        for i in range(len(results)):
            input = inputs[i]
            result = results[i]
            layer_1 = Meth.relu(np.dot(input,self.weights[0]))
            layer_2 = np.dot(layer_1,self.weights[1])

            delta_2 = layer_2 - result
            #print(delta_2)
            error_2 = delta_2**2
            delta_1 = np.dot(delta_2, self.weights[1].T)*Meth.reluD(layer_1) 
            #print(delta_1)
            self. weights[1] -= self.alpha*(np.dot(layer_1.T,delta_2))
            self.weights[0] -= self.alpha*(np.dot(np.array([input]).T,[delta_1]))
            #print(self.weights[1])

class DeepNet22:
    weights = np.array(
            [
               np.array([[0.3,-0.8,0.2,0.7],[0.9,0.5,-0.2,-0.1],[0.4,0.6,0.9,0.2]]),
                np.array([[0.3,0.7,-0.8,0.4],[0.2,0.4,0.6,-0.2]])
            ])
    alpha = 0.1
    def predict(self,input):
        layer_1 = Meth.relu(np.dot(input,self.weights[0]))
        layer_21 = np.dot(layer_1,self.weights[1][0])
        layer_22 = np.dot(layer_1,self.weights[1][1])
        layer_2 = [layer_21,layer_22]
        return layer_2
    def learn(self,inputs,results): 
        print(inputs)
        for i in range(len(results)): 
            input = inputs[i]
            result = results[i]
            print(result)
            layer_1 = Meth.relu(np.dot(input,self.weights[0]))
            #print(layer_1)
            layer_2_1 = np.dot(layer_1,self.weights[1][0])
            layer_2_2 = np.dot(layer_1,self.weights[1][1])
        
            delta_2_1 = layer_2_1 - result[0]
            delta_2_2 = layer_2_2 - result[1]
            #print(delta_2)
            error_2_1 = delta_2_1**2
            error_2_2 = delta_2_2**2
            error_2 = error_2_1+error_2_2
            
            delta_1 = np.dot(delta_2_1, self.weights[1][0].T)*Meth.reluD(layer_1)
            delta_1 += np.dot(delta_2_2, self.weights[1][1].T)*Meth.reluD(layer_1)
            #print(delta_2_1)
            self.weights[1][0] -= self.alpha*(np.dot(layer_1.T,delta_2_1))
            self.weights[1][1] -= self.alpha*(np.dot(layer_1.T,delta_2_2))
            self.weights[0] -= self.alpha*(np.dot(np.array([input]).T,[delta_1]))
            #print(self.weights[1])



class Meth:

    def relu(x):
        return (x>0)*x

    def reluD(x):
        return x>0

p = Perceptron()
for i in range(100):
    p.learn(inputs,results)
    #print(p.weights)

d = DeepNet22()
for j in range(1000):
    d.learn(inputs,results2)
    #print(d.weights[1])
   # print(d.weights[0])

print(p.predict(inputs[6]))
print(d.predict(inputs[6]))
print(d.weights)
