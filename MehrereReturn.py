def test():
	a = 10
	b = 12
	c = 13
	return a,b,c

#num = test()
#num[] = test()
print(test()[1])
i = 1
while i<=len(test()):
	print(test()[i-1])
	i+=1
