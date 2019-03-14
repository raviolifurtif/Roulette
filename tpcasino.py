# -*-coding: utf-8 -*

import os
import random

sommedepart=500
argent=sommedepart
continuer = True
print("Vous disposez de ",argent," euros, et entamez avec confiance une session de roulette au casino")

while continuer == True :
	
	mise=-1
	while mise<=0 or mise>argent:
		try:
			mise=input("Combien désirez-vous miser ? \n")
			mise=float(mise)
		except ValueError:
			print("Vous n'avez pas entré un nombre ! Note : la virgule s'écrit ici avec un point.")
			mise=-1
			continue
		if mise<=0:
			print("Soyez raisonnable, vous ne pouvez pas miser une somme négative ou nulle :) Reprenez-vous, bon sang ^^")
			mise=-1
		elif mise>argent:
			print("Vous pensiez que cela aurait pu passer crème, mais... clairement, je vois que vous ne disposez pas d'autant d'argent. Il va falloir se montrer raisonnable ! ")
			mise=-1
		
	
	pari=-1
	while pari<0 or pari>49:
		try:
			pari=input("Sur quel numéro entre 0 et 49 voulez-vous miser ? \n")
			pari=int(pari)
		except ValueError:
			print("Vous n'avez pas entré un numéro, pourtant la consigne était diablement claire !")
			pari=-1
			continue
		if pari<0 or pari>49:
			print("Le numéro choisi n'est pas compris entre 0 et 49, allez un petit effort :)")
			pari=-1
	
	
	resultat=random.randrange(50)
	print("\nEt le numéro vainqueur est le...",resultat, " !! \n")
	
	if pari==resultat:
		argent=argent+3*mise
		print("Bravo, vous êtes tombé sur le bon numéro et remportez trois fois votre mise, soit ",3*mise, "euros. \n   --- \n")
	elif pari%2 == resultat%2:
		argent=argent+round(mise*0.5,2)
		print("Bravo, vous êtes tombé sur la bonne couleur, et remportez la moitié de votre mise, soit ",round(0.5*mise,2), "euros. \n   --- \n")
	else:
		argent=argent-mise
		print("Pas de chance cette fois-ci ! Vous perdez votre mise.  \n   --- \n")
	
	if argent<=0:
		print("Oh, ben c'est pas votre jour, vous êtes à sec... Il est temps de quitter le casino !")
		continuer = False
	else:
		print("Il vous reste à présent ",argent," euros.")
		suite=input("Voulez-vous quitter le casino avec cette somme ? (o/n)\n")
		if suite=="O" or suite=="o" or suite=="Oui" or suite=="oui":
			gain=argent-sommedepart
			if gain<0:
				gain= 0-gain
				print("vous quittez le casino avec ",argent," euros, soit une perte nette de ",gain," euros") 
			elif gain>0:
				print("vous quittez le casino avec ",argent," euros, soit un gain net de ",gain," euros") 
			else:
				print("vous quittez le casino avec ",argent," euros, soit la même somme qu'en arrivant, quelle constance !") 
			continuer = False
		
os.system("pause")			
		
	
	

