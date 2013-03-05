import pandas as pd
import numpy as np
import pdb

def sigmoid(x):
	return 1.0 / (1.0 + np.exp(-x))	

def dot_product(x, w):
	return sum(a * b for a, b in zip(x, w))	


def main(theta=0.001):

	df = pd.read_csv("http://www.ats.ucla.edu/stat/data/binary.csv")

	df.columns = ["admit", "gre", "gpa", "prestige"]

	#Normalizing the data frame

	df_norm = (df - df.min()) / (df.max() - df.min())

	nor_colums = ['admit', 'gre', 'gpa']

	#Dealing with discrete/categorical value 'prestige'
	#Indicator variables - prestige1, prestige2 etc

	for elem in df['prestige']:
		df['prestige'+str(elem)] = df['prestige'] == elem

	#Adding them back to other normalized columns
	prestige_vals = ['prestige1', 'prestige2', 'prestige3', 'prestige4']	
	data = df_norm[nor_colums].join(df.ix[:, prestige_vals])
	
	#Converting Boolean values {T, F} to {1, 0}
	for p in prestige_vals:
		data[p] = data[p].map(lambda x: int(x))

#	print data.head()

	#Preprocessing of data done

	train_cols = data.columns[1:]	
	label_cols = data.columns[0]
	#print train_cols, len(train_cols)
	
	vlen = len(train_cols) #Number of attributes
	N = data.count()[0] #Number of training samples

	w = np.zeros(vlen) #Weight Vector
	count = 0
	while(count<100000):
		gvector = np.zeros(vlen)
		for row in data.values[:200]:
		#	print row
			x = row[1:]
		#	print "x: ", x
			prob = sigmoid(dot_product(x, w))
			error = row[0] - prob
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
	for row in data.values[200:]:
		if row[0] == 1:
				c_ones = c_ones + 1
		else: c_zeros = c_zeros + 1 	
		x = row[1:]
		if dot_product(x, w) > 0:	
			if row[0] == 1:
					p_ones = p_ones + 1

	print p_ones, c_ones, c_zeros
	print "accuracy: ", p_ones/float(c_ones)				

if __name__ == "__main__":
	main()	