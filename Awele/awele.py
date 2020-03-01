#!/usr/bin/env python
# -*- coding: utf-8 -*-
import game 

#Taille du plateau de jeu : 6 * 2
lignes = 2 
colonnes = 6 

def initialiseJeu(jeu):
	"""jeu -> void
		Prend un Plateau vierge et l'initialise pour le jeu awele
	"""
	#Chaque trous contient 4 graines
	for l in range(lignes):
		for c in range(colonnes):
			jeu.plat.plateau[l][c] = 4

def updatePlateauScore(jeu, coup):
	"""jeu -> void
		met à jour le plateau à partir d'un coup à jouer
	"""
	ligne_coup = coup.ligne
	colonne_coup = coup.colonne
	#nbGraine = game.getCaseVal(ligne_coup, colonne_coup)
	nbGraine = jeu.plat.plateau[ligne_coup][colonne_coup]
	jeu.plat.plateau[ligne_coup][colonne_coup] = 0
	L = ligne_coup
	C = colonne_coup
	# Boucle qui parcourt le plateau dans le sens anti-horaire
	while(nbGraine > 0):
		if (L == 1):
			if (C < 5):
				C += 1
			else:
				L = 0
		else:
			if (C > 0):
				C -= 1
			else:
				L = 1
		# saute la case choisit par le joueur
		if (L != ligne_coup or C != colonne_coup):
			jeu.plat.plateau[L][C] += 1
			nbGraine -= 1
	# Mis a jour du score et du plateau si necessaire
	if (L != jeu.joueur-1):
		while (C < colonnes and C >= 0 and (jeu.plat.plateau[L][C] == 2 or jeu.plat.plateau[L][C] == 3)):
			jeu.scores[jeu.joueur-1] += jeu.plat.plateau[L][C]
			jeu.plat.plateau[L][C] = 0
			if (L == 1):
				C -= 1
			else:
				C += 1
	


def getCoupsValides(jeu):
	"""jeu -> List[coup]
		etourne la liste des coups valide a partir du plateau du jeu awele
	"""
	liste_coups_valides = []
	camp_joueur = jeu.joueur-1
	# Boucle qui parcourt chaque trou du joueur qui va jouer
	for t in range(colonnes):
		# Si il y a des graines
		if (jeu.plat.plateau[camp_joueur][t] > 0):
			# test si le coup affame l'autre joueur
			jeu_test = game.getCopieJeu(jeu)
			Coup = game.coup(camp_joueur, t)
			updatePlateauScore(jeu_test, Coup)
			game.changeJoueur(jeu_test)
			LautreCamp = jeu_test.joueur-1
			C = 0
			compteur = 0
			while (C < colonnes and jeu_test.plat.plateau[LautreCamp][C] == 0):
				compteur += 1
				C += 1
			# si il ne l'affame pas alors c'est un coup valide
			if (compteur != colonnes):
				liste_coups_valides.append(Coup)
	return liste_coups_valides
				

def finJeu(jeu):
	""" jeu -> bool
		Retourne vrai si c'est la fin du jeu
    	"""
    #test si un des deux camps n'est pas vide
	res = [0,0]
	for l in range(lignes):
		for c in range(colonnes):
			res[l] += jeu.plat.plateau[l][c]
	return not(res[0] and res[1])









