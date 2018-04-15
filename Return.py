def messen_terperatur():
	temper = 22
	print("der momentare Raumtemperatur ist: %d"%temper)
	return temper

def get_temperatur_hau(temper):
	temper += 3
	print("der monentare Raumtemperatur ist: %d"%temper)

result = messen_terperatur()
get_temperatur_hau(result)
