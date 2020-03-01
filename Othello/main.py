#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append("..")
import game
import othello
game.game=othello
sys.path.append("./Joueurs")
import joueur_humain
game.joueur1=joueur_humain
game.joueur2=joueur_humain

#test
JEU = game.initialiseJeu()
"""JEU.plat.plateau[1][1] = 25
print (game.getCaseVal(JEU, 1, 1))"""
#print (othello.getCoupsValides(JEU.plat))

print ("BIENVENUE sur le jeu OTHELLO !!!\n")
jeu = game.initialiseJeu()

# Boucle principal du jeu
while (not game.finJeu(jeu)):
	game.affiche(jeu)
	game.getCoupsValides(jeu)
	game.joueCoup(jeu, game.saisieCoup(jeu))


print ("C'est la fin du jeu et c'est", end="")
gagnant = game.getGagnant(jeu)
if (gagnant == 0):
	print ("un MATCH NUL !!!")
else:
	print("le JOUEUR", gagnant,"qui gagne, BRAVO a lui !!!")



