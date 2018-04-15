def test(a, b, c=33, *args, **kwargs):
	print(a)
	print(b)
	print(c)
	print(args)
	print(kwargs)

#test(11,22,34,12,32,34,53,44,task=55,done=99)

A = (44, 55, 66)
name ={"name":"laowang", "age":12}
test(12,23,423,A,name)
test(12,32,3213,*A,**name)
