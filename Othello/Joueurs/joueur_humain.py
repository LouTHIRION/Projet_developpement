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
	coord_x = input("quel ligne ? ")
	coord_y = input("quelle colonne ? ")
    
