#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append("../..")
import game

def saisieCoup(jeu):
	""" jeu -> coup
		Retourne un coup a jouer
	"""
	return choisieCoup(jeu)

def choisieCoup(jeu):
	""" jeu -> coup
		Choisi le coup qui rapportera le plus de score
	"""
	# test tous les coups possibles avec une copie du jeu
	meilleur_score = 0
	jeu_test = game.getCopieJeu(jeu)
	joueur = game.getJoueur(jeu)
	for c in jeu.coups_possibles:
		game.joueCoup(jeu_test, c)
		if (game.getScore(jeu_test, joueur) >= meilleur_score):
			meilleur_score = game.getScore(jeu_test, joueur)
			meilleur_coup = c
		jeu_test = game.getCopieJeu(jeu)
	return meilleur_coup
