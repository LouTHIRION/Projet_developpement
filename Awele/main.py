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

JEU = game.initialiseJeu()
JEU.plat.plateau[0][0] = 2
game.affiche(JEU)
game.joueCoup(JEU,game.coup(0,4))
game.affiche(JEU)


