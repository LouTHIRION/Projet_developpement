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
			if (jeu.plat.plateau[l][c] == 0):
				liste_coups.append(game.coup(l,c))
	return liste_coups

def updatePlateauScore(jeu, coup):
	"""jeu -> void
		met à jour le plateau à partir d'un coup à jouer
	"""
	ligne_coup = coup.ligne
	colonne_coup = coup.colonne
	#On place le pion
	jeu.plat.plateau[ligne_coup][colonne_coup] = jeu.joueur
	#On fait les eventuels changements de couleur en parcourant le damier a la recherche de pions de meme couleur
	for l in range(lignes):
		for c in range(colonnes):
			if (jeu.plat.plateau[l][c] == jeu.joueur):
				# test si il y a des pions de meme couleur sur la meme ligne,
				# colonne ou diagonales que celui qui vient d'etre pose :
				# sur la meme ligne (a peu pres le meme schema est repete 4 fois)
				if (l == ligne_coup and (c > colonne_coup+1 or c < colonne_coup-1)):
					# si c'est le cas cherche si il y a des pions de l'adversaire entre ces pions
					liste_coord_pion = []
					C = min(c, colonne_coup)+1 
					while(C < max(c, colonne_coup)):
						# si il y en a, on les change de couleur, sinon on sort de la boucle 
						if (jeu.plat.plateau[l][C] != game.getLautreJoueur(jeu)):
							C = max(c, colonne_coup)
						else:
							liste_coord_pion.append((l, C))
							if (C == max(c, colonne_coup)-1):
								for p in liste_coord_pion:
									jeu.plat.plateau[p[0]][p[1]] = jeu.joueur
							C += 1
				# sur la meme colonne
				elif (c == colonne_coup and (l > ligne_coup+1 or l < ligne_coup-1)):
					liste_coord_pion = []
					L = min(l, ligne_coup)+1
					while(L < max(l, ligne_coup)):
						if (jeu.plat.plateau[L][c] != game.getLautreJoueur(jeu)):
							L = max(l, ligne_coup)
						else:
							liste_coord_pion.append((L, c))
							if (L == max(l, ligne_coup)-1):
								for p in liste_coord_pion:
									jeu.plat.plateau[p[0]][p[1]] = jeu.joueur
							L += 1
				# sur la meme diagonale
				elif (c-colonne_coup == ligne_coup-l and (c != colonne_coup and l != ligne_coup)):
					liste_coord_pion = []
					C = min(c, colonne_coup)+1
					L = max(l, ligne_coup)-1
					while(C < max(c, colonne_coup) and L > min(l, ligne_coup)):
						if (jeu.plat.plateau[L][C] != game.getLautreJoueur(jeu)):
							L = min(l, ligne_coup)
						else:
							liste_coord_pion.append((L, C))
							if (C == max(c, colonne_coup)-1 and L == min(l, ligne_coup)+1):
								for p in liste_coord_pion:
									jeu.plat.plateau[p[0]][p[1]] = jeu.joueur
							C += 1
							L -= 1
				elif (c-colonne_coup == l-ligne_coup and (c != colonne_coup and l != ligne_coup)):
					liste_coord_pion = []
					C = min(c, colonne_coup)+1
					L = min(l, ligne_coup)+1
					while(C < max(c, colonne_coup) and L < max(l, ligne_coup)):
						if (jeu.plat.plateau[L][C] != game.getLautreJoueur(jeu)):
							L = max(l, ligne_coup)
						else:
							liste_coord_pion.append((L, C))
							if (C == max(c, colonne_coup)-1 and L == max(l, ligne_coup)-1):
								for p in liste_coord_pion:
									jeu.plat.plateau[p[0]][p[1]] = jeu.joueur
							C += 1
							L += 1
							
	






			
