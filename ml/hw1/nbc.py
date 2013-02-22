#!/usr/bin/env python
"""
@Author: Primal Pappachan
@email: primal1@umbc.edu
Naive Bayes Classifier
Dataset used: Mushroom dataset from UCI ML repository
http://archive.ics.uci.edu/ml/machine-learning-databases/mushroom/agaricus-lepiota.data
Accuracy of the Classifier:  0.95
Parameters estimated by NB: printout attached
Predicted class probabilities: printout attached
"""
import random

class AutoVivification(dict):
	#Ref: http://stackoverflow.com/questions/651794/whats-the-best-way-to-initialize-a-dict-of-dicts-in-python
    def __getitem__(self, item):
        try:
            return dict.__getitem__(self, item)
        except KeyError:
            value = self[item] = type(self)()
            return value


def add_category(categories, category):
	if categories.has_key(category):
		categories[category] += 1
	else: categories[category] = 1	
	return categories

def add_attribute(a, category, attr, value):
	if a[category][attr].has_key(value):
		a[category][attr][value] += 1
	else: a[category][attr][value] = 1
	return a

def cond_probability(a, category, attr, value, categories):
#	pdb.set_trace()
	if a[category][attr].has_key(value):
		x = a[category][attr][value] + 1
	else: x = 1	
	return x/float(categories[category] + len(a[category][attr].values()))

def estimate_parameters(categories, a):
	#Function to estimate parameters
	for c in categories.keys(): #cat
	#	print a
		for i in xrange(0, 22): #attr;
			for v in xrange(len(a[c][i].values())): #value
				print "%s;%d;%s;%f" %(c, i, a[c][i].keys()[v], cond_probability(a, c, i, v, categories))

def partition_set(instances):
	#Function to enforce similar class distribution
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


def main(filename):
	instances = open(filename).read().splitlines()
	trainset, testset = partition_set(instances)
	categories = dict()
	a = AutoVivification() #data-store for [category][attribute][value] counts
	flag = True #flag to check if attribute has been added once
	for t in trainset:
		sample = t.split(',')		
		category, attributes = sample[0], sample[1:] #First element of instance = category, Rest = Attributes
		categories = add_category(categories, category)
		for i in range(len(attributes)):
			value = attributes[i]
			if flag:
				a[category][i][value] = 1	
			else:	
				a = add_attribute(a, category, i, value)				
		flag = False


	p = e = acc = 0
	for t in testset:
		sample = t.split(',')
		label, attributes = sample[0], sample[1:]
		max = 0.0
		for k in categories.keys():
			product = 1
			for i in range(len(attributes)):
				value = attributes[i]
				product *= cond_probability(a, k, i, value, categories) 
			arg = product * (categories[k]/float(len(trainset)))
			if arg > max: 
				max = arg
				predicted = k							
		if predicted == label: acc+= 1
 		
	print acc/float(len(testset))

if __name__ == "__main__":
	main('agaricus-lepiota.data')
