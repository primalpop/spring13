import pdb

class AutoVivification(dict):
    """Implementation of perl's autovivification feature."""
    def __getitem__(self, item):
        try:
            return dict.__getitem__(self, item)
        except KeyError:
            value = self[item] = type(self)()
            return value

def train(sample):
	"""Increment category no in a list whose len = no of categories
		Increment attr value w.r.t category no, cat[attr1] = [v1, v2, ........., vn]
	"""
	pass



def classify(sample, default):	

	#for each class label: compute p(yk)
	#	for each attribute: compute p(ai) and the product
	#	multiply and store in the list [c1, c2, ............., cn]
	#return index of maximum value in the list	
	pass

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

def cond_probability(a, category, attr, value):
	s = 0
	if a[category][attr].has_key(value):
		x = a[category][attr][value]
	else: x = 1	
	for key in a[category][attr].keys():
		s = s + a[category][attr][key]
	return x/float(s)	

def main(filename):
	instances = open(filename).read().splitlines()
	#Split of 2/3 and 1/3
	split = int((2/3.0) * len(instances))
	trainset = instances[:split]
	testset = instances[split:]	
	categories = dict()
	a = AutoVivification() #data-store for [category][attribute][value] counts
	flag = True #flag to check if attribute has been added once
	for t in trainset:
		sample = t.split(',')		
		category = sample[0]
		categories = add_category(categories, category)
		attributes = sample[1:]
		for i in range(len(attributes)):
			value = attributes[i]
			if flag:
				a[category][i][value] = 1	
			else:	
				a = add_attribute(a, category, i, value)				
		flag = False

	#Estimate probability for a class label
	for k in categories.keys():
		prob_k = categories[k]/float(split)
		categories[k] = prob_k

#	print categories, a

	max = 0.0
	for t in testset:
		sample = t.split(',')
		print sample	
		label = sample[0]
		attributes = sample[1:]
		for k in categories.keys():
			product = 1
			for i in range(len(attributes)):
				value = attributes[i]
				product *= cond_probability(a, k, i, value) 
			if product * categories[k] > max: 
				max = product * categories[k]
				predicted = k
		print predicted	
		 		

if __name__ == "__main__":
	main('testfile.txt')
