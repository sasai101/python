# Produktregel

a = 1

while a<=9:
	b = 1
	while b<=a:
		print("%d*%d=%d\t"%(a,b,a*b), end=" ")  #\t==> Austichtung  \a ====> neue Zeile
		b += 1
	
	print("")
	a += 1
