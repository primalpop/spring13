#!/usr/bin/env python
"""
@Author: Primal Pappachan
@email: primal1@umbc.edu
K Nearest Neighbour Algorithm
Dataset used: Mushroom dataset from UCI ML repository
http://archive.ics.uci.edu/ml/machine-learning-databases/mushroom/agaricus-lepiota.data
"""

import sys
import random

def hamming_distance(s1, s2):
	#ref: http://en.wikipedia.org/wiki/Hamming_distance
    return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))

def majority(neighbours):
	#Returns the maximum occuring label
	nlist = [x[1] for x in neighbours]
	return max(set(nlist), key=nlist.count)

def find_neighbours(k, element, trainset):
	# Returns sorted list of tuples of (hamming distance, label) of k neighbours
	ns = []
	for t in trainset:
		ns.append((hamming_distance(element[1:], t[1:]), t[0], t))
	return sorted(ns)[:k]

def train(trainset, k):
	kacc = 0
	for t in trainset:
		tset = trainset[:]
		tset.remove(t)
		ns = find_neighbours(k, t, tset)
		if majority(ns) == t[0]:
			kacc += 1		
	return kacc/float(len(trainset))

def test(trainset, testset, k):
	correct = 0.0
	for t in testset:
		ns = find_neighbours(k, t, trainset)
		if majority(ns) == t[0]: correct += 1
	return correct/len(testset)		

def partition_set(instances):
	ed, po = [], []
	for i in xrange(len(instances)):
   		if instances[i][0] == 'e':
			ed.append(instances[i])
		else: po.append(instances[i])
	random.shuffle(ed)
	random.shuffle(po)
	edsplit, posplit = int((2/3.0) * len(ed)), int((2/3.0) * len(po))	
	trainset = ed[:edsplit] + po[:posplit]
	testset = ed[edsplit:] + po[posplit:]	
	return trainset, testset

def main(filename, k):
	instances = open(filename).read().splitlines()
	trainset, testset = partition_set(instances)
	trainacc = []
	for i in range(k, 1, -5):
		trainacc.append(train(trainset, i))
	print trainacc
	testacc = []
	for i in range(k, 1, -5):
		testacc.append(test(trainset, testset, i))
	print testacc

if __name__ == "__main__":
	if len(sys.argv) == 2:
		k = eval(sys.argv[1])
		main('agaricus-lepiota.data', k)
	else: 
		print "missing maximum k(eg:100) parameter"	