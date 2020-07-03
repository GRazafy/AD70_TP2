# -*- coding: utf-8 -*-

import numpy as np  # utilisation des calculs matriciels
# import pandas as pd #générer les fichiers csv
import random as rd  # génération de nombre aléatoire
from random import randint  # génération des nombres aléatoires
import matplotlib.pyplot as plt
import msvcrt as m


NOMBRE_DE_VILLES = 10
distances = np.zeros((NOMBRE_DE_VILLES, NOMBRE_DE_VILLES))
MAX_DISTANCE=2000
for ville in range(NOMBRE_DE_VILLES):
    villes = [ i for i in range(NOMBRE_DE_VILLES) if not i == ville ]
    for vers_la_ville in villes:
        distances[ville][vers_la_ville] =rd.randint(50, MAX_DISTANCE)
        distances[vers_la_ville][ville] =distances[ville][vers_la_ville]
print('voici la matrice des distances entres les villes \n',distances)



def cal_distance(solution,distances,NOMBRE_DE_VILLES):
    eval_distance=0
    for i in range (len(solution)):
        origine,destination=solution[i],solution[(i+1)%NOMBRE_DE_VILLES]
        eval_distance+=distances[origine][destination]
    return eval_distance


def voisinage(solution,NOMBRE_DE_VILLES):
    echange=rd.sample(range(NOMBRE_DE_VILLES),2)
    sol_voisine=solution
    (sol_voisine[echange[0]],sol_voisine[echange[1]])=(sol_voisine[echange[1]],sol_voisine[echange[0]])
    return sol_voisine
# Données du problème (générées aléatoirement)
solution=rd.sample(range(NOMBRE_DE_VILLES),NOMBRE_DE_VILLES)
cout0=cal_distance(solution,distances,NOMBRE_DE_VILLES)
T=1000
facteur=0.99
T_intiale=MAX_DISTANCE/2
min_sol=solution
cout_min_sol=cout0
for ville in range(NOMBRE_DE_VILLES):
    villes = [ i for i in range(NOMBRE_DE_VILLES) if not i == ville ]
    for vers_la_ville in villes:
        distances[ville][vers_la_ville] =rd.randint(50, MAX_DISTANCE)
        distances[vers_la_ville][ville] =distances[ville][vers_la_ville]
print('voici la matrice des distances entres les villes \n',distances)

tab_for_res = []
for i in range(100):
    print('la ',i,'ème solution = ',solution,' distance totale= ',cout0,' température actuelle =',T)
    T=T*facteur
    for j in range(50):
        nouv_sol=voisinage(solution*1,NOMBRE_DE_VILLES)
        cout1=cal_distance(nouv_sol,distances,NOMBRE_DE_VILLES)
        if cout1<cout0:
            cout0=cout1
            solution=nouv_sol
            if cout1<cout_min_sol:
                cout_min_sol=cout1
                min_sol=solution
        else:
            x=np.random.uniform()
            if x<np.exp((cout0-cout1)/T):
                cout0=cout1
                solution=nouv_sol
    tab_for_res.append(cout0)
def affichage(tab_for_res):
    plt.plot(list(range(100)),tab_for_res,label = 'cout_solution')
    plt.legend()
    plt.title('Evolution du cout de la solution')
    plt.xlabel('nb solutions')
    plt.ylabel('Cout')
    plt.show()
affichage(tab_for_res)



        




