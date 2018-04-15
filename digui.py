# Jiecheng de suanfa


def jie(num):
	if num>1:
		return num * jie(num-1)
		#num * jie(num-1)
	else:
		return num

result = jie(4)
print(result)
	
