#!/usr/bin/env python
"""
@Author: Primal Pappachan
@email: primal1@umbc.edu
K Nearest Neighbour Algorithm
Dataset used: Mushroom dataset from UCI ML repository
http://archive.ics.uci.edu/ml/machine-learning-databases/mushroom/agaricus-lepiota.data
"""

def hamming_distance(s1, s2):
	#ref: http://en.wikipedia.org/wiki/Hamming_distance
    return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))

def majority(neighbours):
	#Returns the maximum occuring label
	nlist = [x[1] for x in neighbours]
	return max(set(nlist), key=nlist.count)

def find_label(k, t, tset):
	hd  = [] 
	for i in tset:
		hd.append((hamming_distance(t[1:], i[1:]), i[0]))
	return majority(sorted(hd)[:k+1])

def train(trainset, k):	
	count = 0
	for t in trainset:
		tset = trainset[:]
		tset.remove(t)
		label = find_label(k, t, tset)
		if label == t[0]:
			count +=1				
	return count


def test(trainset, testset, k):
	correct = 0
	for t in testset:
		label = find_label(k, t, trainset)
		if label == t[0]: correct += 1
	return correct/float(len(testset))	


def partition_set(instances):
	ed, po = [], []
	for i in xrange(len(instances)):
   		if instances[i][0] == 'e':
			ed.append(instances[i])
		else: po.append(instances[i])
#	random.shuffle(ed)
#	random.shuffle(po)
	edsplit, posplit = int((2/3.0) * len(ed)), int((2/3.0) * len(po))	
	trainset = ed[:edsplit] + po[:posplit]
	testset = ed[edsplit:] + po[posplit:]	
	return trainset, testset

def main(filename):
	instances = open(filename).read().splitlines()
	#Split of 2/3 and 1/3
	trainset, testset = partition_set(instances)
	trainacc = []
	k = 100
	for i in range(k, 1, -5):
		trainacc.append(train(trainset, k))
	print [x/float(len(trainset)) for x in trainacc]
	testacc = []
	for k in range(100, 1, -5):
		testacc.append(test(trainset, testset, k))
	print testacc
	
		
if __name__ == "__main__":
	main('mintest.txt')