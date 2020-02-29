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

#game.changeJoueur(JEU)
JEU.plat.plateau[4][2] = 2
JEU.plat.plateau[5][1] = 2
game.affiche(JEU)
othello.updatePlateauScore(JEU, game.coup(6,0))
game.affiche(JEU)
"""for c in game.getCoupsValides(JEU):
	game.afficheCoup(c)"""



