
import itertools

def hamming_distance(s1, s2):
	"""
	ref: http://en.wikipedia.org/wiki/Hamming_distance
	"""
 	#print sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))
    return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))

def majority(neighbours):

	for n in neighbours

def find_neighbours(k, t, tset):
	hd  = [] 
	for i in tset:
		hd.append((hamming_distance(t[1:], i[1:]), i[0]))
	return sorted(hd)



def train(trainset):
	klist = [] #stores the accuracy for various values of k
	k = 20 #maximum number of neighbours

	for t in trainset:
		tset = trainset
		ns = find_neighbours(k, t, tset.remove(t))

		


	
"""
	Get training instances

	Leave 1 out and train on the rest and find out k

	train set = 2/3 of total instances

	for k = 20 to 1:
		for i in instances:
			for j in instances: 
				if not equal:
					Take i and find out its hamming distance to j
			choose lowest (randomly or majority of the group) to label the instance		
			assign label to the instance from
			check if label was right, if yes increase the count for that k value
			else: do nothing		
		karray++	

	Take the index of maximum value of k-array as the choice of k


"""



def main(filename):
	instances = open(filename).read().splitlines()
	#Split of 2/3 and 1/3
	split = int((2/3.0) * len(instances))
	trainset = instances[:split]
	testset = instances[split:]	




if __name__ == "__main__":
	main('testfile.txt')