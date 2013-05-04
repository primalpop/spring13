

import arff
import sys
import random

def main(instances):
	#data = [[1,2,'a'], [3, 4, 'john']]
	data = []
	attrs = 7
	for i in range(instances):
		attr = []
		for j in range(attrs):		
			a = random.randint(0,1)
			attr.append(a)
		prob = int(random.random()*10) 
		c = (attr[0] and attr[2]) or int((not attr[2] and not attr[3]) or ( attr[6] and attr[4]))			
	#	if prob > 6: #attr.append(int(not c))
		#	attr[3] = int(not(attr[3]))
		#	attr[6] = int(not(attr[6])) #rob = 0.81
		#	attr[4] = int(not(attr[4]))
		#	attr[2] = int(not(attr[2]))
		#	attr[0] = int(not(attr[0])) 
		attr.append(c)		
		data.append(attr)
	names = []	
	for i in range(attrs):
		names.append('a' + str(i))
	names.append('result')		

	arff.dump('result.arff', data, relation="boolean", names = names)	


if __name__ == "__main__":
	main(100)	