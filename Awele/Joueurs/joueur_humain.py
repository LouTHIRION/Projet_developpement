#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append("../..")
import game


def saisieCoup(jeu):
	""" jeu -> coup
		Retourne un coup a jouer
	"""
	colonne = int(input("Entrez votre coup : "))
	Coup = game.coup(jeu.joueur-1,colonne)
	while (not game.coupValide(jeu, Coup)):
		print("Le coup que vous voulez effectuer est impossible !!!\nVeuillez reessayer : ")
		colonne = int(input("Entrez votre coup : "))
		Coup.colonne = colonne
	return Coup
