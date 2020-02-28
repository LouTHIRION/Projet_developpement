#!/usr/bin/env python
# -*- coding: utf-8 -*-
import game

# Taille du plateau de jeu : 8 * 8
lignes = 8
colonnes = 8

def initialisePlateau(jeu):
	"""jeu -> void
		Prend un Plateau vierge et l'initialise pour le jeu Othello
	"""
	#on ajoute deux pions de chaque couleur au centre du Plateau
	jeu.plat.plateau[lignes//2-1][colonnes//2-1]=1
	jeu.plat.plateau[lignes//2-1][colonnes//2]=2
	jeu.plat.plateau[lignes//2][colonnes//2-1]=2
	jeu.plat.plateau[lignes//2][colonnes//2]=1

def getCoupsValides(jeu):
	"""jeu -> List[coup]
		Retourne la liste des coups valide a partir du plateau du jeu othello
	"""
	liste_coups = []
	for l in range(lignes):
		for c in range(colonnes):
			if (game.getCaseVal(jeu) == 0):
				liste_coups.append(game.coup(l,c))
	return liste_coups

def updatePlateau(jeu, coup):
	"""jeu -> void
		met à jour le plateau à partir d'un coup à jouer
	"""
	ligne_coup = coup.ligne
	colonne_coup = coup.colonne
	#On place le pion
	jeu.plat.plateau[ligne_coup][colonne_coup] = jeu.joueur
	#On fait les eventuels changements de couleur
	for l in range(lignes):
		for c in range(colonnes):
			if (game.getCaseVal(jeu, l, c) == jeu.joueur):
				if (l == ligne_coup and c != colonne_coup):
					liste_coord_pion = []
					C = min(c, colonne_coup)
					while(C < max(c, colonne_coup)):
						if (game.getCaseVal(jeu, l, c) != jeu.joueur):
							C = max(c, colonne_coup)
						else:
							liste_coord_pion.append((l, C))
							if (C == max(c, colonne_coup)):
								for p in liste_coord_pion:
									jeu.plat.plateau[p[0]][p[1]] = jeu.joueur
							C += 1
							
					#for C in range (min(c, colonne_coup)+1,max(c, colonne_coup)):
				"""or (c == colonne_coup and l != ligne_coup) or (l-ligne_coup == c-colonne_coup):"""
				
