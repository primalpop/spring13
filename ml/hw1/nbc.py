import pdb
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
	if a[category][attr].has_key(value):
		x = a[category][attr][value] + 1
	else: x = 1	
	return x/float(categories[category]+sum(categories.values()))	

def main(filename):
	instances = open(filename).read().splitlines()
	random.shuffle(instances) #Randomizes the instances so as to improve distribution
	split = int((2/3.0) * len(instances)) #Split of 2/3 and 1/3
	trainset = instances[:split]
	testset = instances[split:]	
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

#	print categories, a
	p = e = acc = 0
	for t in testset:
		sample = t.split(',')
	#	print sample	
		label, attributes = sample[0], sample[1:]
		max = 0.0
		for k in categories.keys():
			product = 1
			for i in range(len(attributes)):
				value = attributes[i]
				product *= cond_probability(a, k, i, value, categories) 
	#		print product * categories[k], k
	#		print "max", max
			arg = product * (categories[k]/float(split))
			if arg > max: 
				max = arg
				predicted = k
		#	print "max", max	
		#print "predicted", predicted		
		if predicted == 'e': e+=1 
		else: p+=1						
		if predicted == label: acc+= 1	
	print e, p 	 		
	print acc/float(len(testset))

if __name__ == "__main__":
	main('testfile.txt')
