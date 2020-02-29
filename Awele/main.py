#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append("..")
import game
import awele
game.game=awele
sys.path.append("./Joueurs")
import joueur_humain
game.joueur1=joueur_humain
game.joueur2=joueur_humain

"""
JEU = game.initialiseJeu()
for i in range(6):
	JEU.plat.plateau[0][i] = 0
game.affiche(JEU)
game.getCoupsValides(JEU)
for c in JEU.coups_possibles:
	game.afficheCoup(c)
print("j1",JEU.joueur)
game.joueCoup(JEU, game.coup(0,0))
print("j2",JEU.joueur)
game.affiche(JEU)
game.getCoupsValides(JEU)
print("j3",JEU.joueur)
for c in JEU.coups_possibles:
	game.afficheCoup(c)"""


print ("BIENVENUE sur le jeu AWELE !!!\n")
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




