#!/usr/bin/env python
from math import log
import random
import numpy as np
import pdb

DATASET = 'agaricus-lepiota.data'
ATTRIBUTES = 'agaricus-lepiota.names'

def most_common(lst):
    return max(set(lst), key=lst.count)

def knn(training_data,k,inputdata):
    trainingdistance = []
    for i in xrange(0,len(training_data)):
        trainingdistance.append(distance(training_data[i],inputdata))
    sortedDist = [i[0] for i in sorted(enumerate(trainingdistance), key=lambda x:x[1])]
    sortedTraining_data = [training_data[i] for i in sortedDist]
    topk = list(zip(*sortedTraining_data[:k])[0])
    pdb.set_trace()
    return most_common(topk)

def remove_values_from_list(the_list, val):
    return [value for value in the_list if value != val]

def distance(A,B):
    distance = 0
    for i in xrange(0,22):
        if A[1][i] != B[1][i]:
            distance = distance+1
    return distance

if __name__ == '__main__':
    k=5
    filename = "/home/primal/spring13/ml/hw1/testfile.txt"
    instances = open(filename).read().splitlines()
    formateddata = []
    for i in xrange(0,len(instances)):
        seperatedlist = remove_values_from_list(instances[i], ',')
        p = (seperatedlist[0],seperatedlist[1:])
        formateddata.append(p)

    split = int((2/3.0) * len(formateddata))
    training_data = formateddata[:split]
    test_data = formateddata[split:] 

    count =0.0
    for i in xrange(0,len(test_data)):
        pred = knn(training_data,k,test_data[i])
        if(pred == test_data[i][0]):
            count = count+1

    print "Accuracy"+ (str)(count/len(test_data))