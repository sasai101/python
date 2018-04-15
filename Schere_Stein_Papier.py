#Schere Stein and Papier. Gluckspiel
import random

SSP = int(input("Bitte eingeben: Schere(1) Stein(2) Papier(3) "))
com = random.randint(1,3)

if (SSP==1 and com==2) or (SSP==2 and com==3) or (SSP==3 and com==1):
	print ("Sie haben gewonnen")
elif SSP==com:
	print ("Das Spiel ist unentscheides")
else:
	print ("Sie haben verloren")
