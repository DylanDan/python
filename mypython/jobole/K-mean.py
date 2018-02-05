import pandas as pd
from sklearn.model_selection import train_test_split
import math
import operator

source_data= pd.read_csv('..\\mydata\\iris.data',header=None)

# print(source_data)

data = source_data[list(range(5))]

# print(data.shape)

train_data,test_data, = train_test_split(data,test_size=0.5)
train_data = train_data.values
test_data = test_data.values

# print(train_data.values[0][0])
# print(test_data.values)

def euclideanDistance(data1,data2,length):
    distance = 0
    for i in range(length):
        distance += pow((data1[i]-data2[i]),2)
    return math.sqrt(distance)

# def test1():
#     data1 = [2, 2, 2, 'a']
#     data2 = [4, 4, 4, 'b']
#     distance = euclideanDistance(data1, data2, 3)
#     print ('Distance: ' + repr(distance))

def findNeighbors(traindata,testdata,k):
    distance = []
    length = len(testdata) -1
    for i in range(len(traindata)):
        dist = euclideanDistance(testdata,traindata[i],length)
        distance.append((traindata[i],dist))
    distance.sort(key = operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(distance[x][0])
    return neighbors

def getResponse(ngber):
    classVotes = {}
    for x in range(len(ngber)):
        response = ngber[x][-1]
        if response in classVotes:
            classVotes[response] += 1
        else:
            classVotes[response] =1
    sortedVotes = sorted(classVotes.items(),key=operator.itemgetter(1),reverse=True)
    return sortedVotes[0][0]

def getAccuracy(test,predic):
    correct = 0;
    for x in range(len(test)):
        if test[x][-1] is predic[x]:
            correct += 1
        else:
            print("-----------> actul:"+test[x][-1]+" and predic:"+predic[x])
    return (correct/float(len(test)))*100

if __name__ == '__main__':
    prediction = []
    k = 3
    for x in range(len(test_data)):
        neighbors = findNeighbors(train_data,test_data[x],k)
        res = getResponse(neighbors)
        prediction.append(res)
        print('>>>> predicted=' + repr(res) + ', actual=' + repr(test_data[x][-1]))
    accuracy = getAccuracy(test_data, prediction)
    print('Accuracy: ' + repr(accuracy) + '%')