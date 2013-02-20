
import itertools
import pdb

def hamming_distance(s1, s2):
	#ref: http://en.wikipedia.org/wiki/Hamming_distance
    return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))

def majority(neighbours):
	#Returns the maximum occuring label
	nlist = [x[1] for x in neighbours]
#	print nlist
	return max(set(nlist), key=nlist.count)

def find_neighbours(k, t, tset):
	# Returns sorted list of tuples of (hamming distance, label) of k neighbours
	hd  = [] 
	for i in tset:
		hd.append((hamming_distance(t[1:], i[1:]), i[0]))
	return sorted(hd)[:k+1]

def train(trainset):
	k = len(trainset)/2 #maximum number of neighbours
	klist = [0] * k #stores the accuracy for various values of k
	for t in trainset:
	#	pdb.set_trace()
		tset = trainset[:]
		tset.remove(t)
		ns = find_neighbours(k, t, tset)
	#	print "neighbours", ns
		for i in range(k, 0, -1):
		#	print  "majority: %s label: %s neighbours: %s" %  (majority(ns[:i]), t[0], ns[:i])
			if majority(ns[:i]) == t[0]:
			#	print  majority(ns[:i]), t[0], True, i
				klist[i-1] += 1		
#	print klist					
	return klist.index(max(klist)) + 1


def test(trainset, testset, k):
	correct = 0
	for t in testset:
		ns = find_neighbours(k, t, trainset)
		if majority(ns) == t[0]: correct += 1
	print correct/float(len(testset))*100	


def main(filename):
	instances = open(filename).read().splitlines()
	#Split of 2/3 and 1/3
	split = int((2/3.0) * len(instances))
	trainset = instances[:split]
	testset = instances[split:]	
	k = train(trainset)	
	print k
	test(trainset, testset, k)




if __name__ == "__main__":
	main('mintest.txt')