import pandas as pd
import numpy as np
import pdb

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

def main(theta=0.01):
	df = pd.read_csv('bc.csv', na_values=['?'])
#	print df.head()
	attrs = []
	for i in xrange(len(df.values[1])-1):
		attrs.append('a_'+str(i-1))
	attrs.append("label")

	df.columns = attrs	#Initializing the attribute names
	
	#Normalizing the data frame
	data = (df - df.min()) / (df.max() - df.min())
	#Randomizing the values
	data = shuffle(data)
	
#	print data.head()
	
	#Preprocessing of data done
	#pdb.set_trace()

	vlen = df.shape[1] - 1 #Number of attributes

	N = df.shape[0] #Number of training samples

	w = np.zeros(vlen) #Weight Vector
	tlen = int(N * 2/3.0)
	count = 0
	while(count<50):
		gvector = np.zeros(vlen)
		for row in data.values[:tlen]:
		#	print row, len(row), vlen
			x = row[:vlen]
			label = row[vlen]
		#	print "x: ", x
			prob = sigmoid(dot_product(x, w))
			error = label - prob 
			for j in xrange(vlen):
				gvector[j] = gvector[j] + error * x[j]
		#print "g", gvector
		#pdb.set_trace()		
		w = w + theta * gvector
		count = count + 1
		#print "w: ", w	
	print w	

	p_ones = 0
	c_ones = 0 
	c_zeros = 0
	for row in data.values[tlen:]:
		#pdb.set_trace()
		if row[vlen] == 1:
				c_ones = c_ones + 1
		else: c_zeros = c_zeros + 1 	
		x = row[:vlen]
		if dot_product(x, w) > 0:	
			if row[vlen] == 1:
					p_ones = p_ones + 1

	print p_ones, c_ones, c_zeros
	print "accuracy: ", p_ones/float(c_ones)				

if __name__ == "__main__":
	main()	