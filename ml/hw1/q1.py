

import arff
import sys
import random

def main(instances):
	#data = [[1,2,'a'], [3, 4, 'john']]
	data = []
	attrs = 10
	for i in range(instances):
		attr = []
		for j in range(attrs):		
			a = random.randint(0,1)
			attr.append(a)
		prob = int(random.random()*10) #prob = 0.7
		c = (attr[0] and attr[1]) or int((not attr[1] and attr[2]))			
		if prob > 7: attr.append(int(not c))
		else: attr.append(c)		
		data.append(attr)
	names = []	
	for i in range(attrs):
		names.append('a' + str(i))
	names.append('result')		

	arff.dump('result.arff', data, relation="boolean", names = names)	


if __name__ == "__main__":
	main(600)