# mit List verwalten die Namenkarte


#1. Funktion zeigen
print("="*50)
print("*** System der Namenverwaltung ***")
print("1. ein Name additieren")
print("2. ein Name loeschen")
print("3. ein Name verandern")
print("4. ein Name Suchen")
print("5. ausschlaten")
print("6. zeigen alle Namen")
print("="*50)


names =[]

while True:
	#2. Nimmt die Opption
	num = int(input("Bitte geben Sie ein Opption: "))

	#3. durch die genommenen Opption lauft die erfolgende Funtion.
	if num==1:
		newName = input("Bitte geben Sie einen Name: ")
		names.append(newName)
	elif num==2:
		newName = input("Bitte geben Sie einen Name, um der zu loschen : ")
		names.remove(newName)
	elif num==3:
		newName = input("Bitte geben Sie einen Name, um der zu verandern: ")
		if newName in names:
			names[names.index(newName)] = input("Bitte geben Sie eine neue Namen: ")
			print("Name wird schon geandert!!")
		else:
			print("der Name ist nicht in der Liste!!")
	elif num==4:
		newName = input("Bitte geben Sie einen Name, welchen Sie suchen moechten:  ")
		if newName in names:
			pos = names.index(newName)
			print("der ist gefunden, in Positon %d"%pos )
		else:
			print("nicht gefunden!!")
	elif num==6:
		print(names)
	
	elif num==5:
		break
	else:
		print("Bitte geben Sie richtige Opption ein!!")
