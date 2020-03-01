#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append("../..")
import game

def saisieCoup(jeu):
	""" jeu -> coup
		Retourne un coup a jouer
	"""
	print ("Entrez les coordonnées de votre coups.")
	ligne = int(input("quel ligne ? "))
	colonne = int(input("quelle colonne ? "))
	Coup = game.coup(ligne, colonne)
	while (not game.coupValide(jeu, Coup)):
		print("Le coup que vous voulez effectuer est impossible !!!\nVeuillez reessayer : ")
		Coup.ligne = int(input("quel ligne ? "))
		Coup.colonne = int(input("quelle colonne ? "))
	return Coup
