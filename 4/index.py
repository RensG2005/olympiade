import sys
from random import randint
line = sys.stdin.readline()

def getWorp(begin, eind):
	return line[begin:eind]

punten = 0
algepakt = []

def regenworm(begin, eind, punten):
	worp = getWorp(begin, eind)
	latenliggen = 0
	while latenliggen in algepakt:
		latenliggen = randint(begin, eind)
		if(latenliggen == 'w'):
			return
	punten += str(latenliggen * worp.count(latenliggen))
	algepakt.append(latenliggen)
	begin += eind
	eind += eind - worp.count(latenliggen)
	regenworm(begin, eind, punten)

regenworm(0, 8, punten)
