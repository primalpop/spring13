#!/usr/bin/env python
"""
@Author: Primal Pappachan
@email: primal1@umbc.edu
2 class Logistic Regression
Dataset used: Breast Cancer Wisconsin
http://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+(Diagnostic)
Dataset Information:
	Number of instances: 569 
	Number of attributes: 32 (ID, diagnosis, 30 real-valued input features)
File used: bc.csv - Contains Dataset with ID removed and diagnosis = {0, 1}
Accuracy: 90%(averaged)
Required Python Libraries:
	pandas - for preprocessing data using data frames
	numpy - for arrays
	pylab - for plotting graphs
"""

import pandas as pd
import numpy as np
import pylab as pl

def sigmoid(x):
	return 1.0 / (1.0 + np.exp(-x))	

def dot_product(x, w):
	return sum(a * b for a, b in zip(x, w))	

def shuffle(df):
	#Randomizes the dataframe
	#Reference: http://stackoverflow.com/questions/13395725/efficient-way-of-doing-permutations-with-pandas-over-a-large-dataframe
	ind = df.index
	sampler = np.random.permutation(df.shape[0])
	new_vals = df.take(sampler).values
	df = pd.DataFrame(new_vals, index=ind)
	return df	

def train(data, theta, vlen, tlen, limit=50):
	w = np.zeros(vlen) #Weight Vector
	count = 0
	while(count<limit):
		gvector = np.zeros(vlen)
		for row in data.values[:tlen]:
			x = row[:vlen]
			label = row[vlen]
			prob = sigmoid(dot_product(x, w))
			error = label - prob 
			for j in xrange(vlen):
				gvector[j] = gvector[j] + error * x[j]		
		w = w + theta * gvector
		count = count + 1	
	return w

def test(data, w, vlen, tlen):
	p_ones = c_ones = c_zeros = 0
	for row in data.values[tlen:]:
		#pdb.set_trace()
		x = row[:vlen]
		if row[vlen] == 1:
			c_ones = c_ones + 1
			if dot_product(x, w) >= 0:
				p_ones = p_ones + 1	
		else: c_zeros = c_zeros + 1 	
	return p_ones, c_ones	

def main(theta=0.001):
	df = pd.read_csv('bc.csv', na_values=['?'])
	attrs = []
	for i in xrange(len(df.values[1])-1):
		attrs.append('a_'+str(i-1))
	attrs.append("label")

	df.columns = attrs	#Initializing the attribute names
	
	#Normalizing the data frame
	data = (df - df.min()) / (df.max() - df.min())
	#Randomizing the values
	data = shuffle(data)

	#Preprocessing of data done

	vlen = df.shape[1] - 1 #Number of attributes
	N = df.shape[0] #Number of training samples
	tlen = int(N * 2/3.0)
	accuracy = []
	limits = [50, 100, 1000, 5000, 10000]
	for limit in limits:
		w = train(data, theta, vlen, tlen,limit)	
		p, c = test(data, w, vlen, tlen)
		accuracy.append(p/float(c))			


	print limits
	print accuracy	
	pl.plot(limits, accuracy)	
	pl.title("Number of Iterations v/s accuracy")
	pl.ylabel("Accuracy")
	pl.xlabel("Number of Iterations")
	pl.show()

if __name__ == "__main__":
	main()	