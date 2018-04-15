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


name =[]

while True:
	#2. Nimmt die Opption
	num = int(input("Bitte geben Sie ein Opption: "))

	#3. durch die genommenen Opption lauft die erfolgende Funtion.
	if num==1:
		info = {}
		newName = input("Bitte geben Sie einen Name: ")
		newNumer = input("Bitte geben Sie eine Nr: ")
		info["name"] = newName
		info["Nummer"] = newNumer
		name.append(info)
	elif num==2:
		newName = input("Bitte geben Sie einen Name, um der zu loschen : ")
		for temp in name:
			#print(temp["name"])
			i = 0
			if newName==temp["name"]:
				#print(name.index(temp["name"]=newName))
				i += 1
				del temp["name"]
				del temp["Nummer"]
				name.remove({})
				break
		else:
			print("nicht gefunden")
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
		print("name\t\tNummer") 
		for temp in name:
			print("%s\t\t%s"%(temp["name"],temp["Nummer"]))	
	elif num==5:
		break
	else:
		print("Bitte geben Sie richtige Opption ein!!")
