# -*- coding: utf-8 -*-

import numpy as np  # utilisation des calculs matriciels
# import pandas as pd #générer les fichiers csv
import random as rd  # génération de nombre aléatoire
from random import randint  # génération des nombres aléatoires
import matplotlib.pyplot as plt
import msvcrt as m



def cal_fitness(solution,distances,NOMBRE_DE_VILLES):
    eval_fitness=0
    for i in range (len(solution)):
        origine,destination=solution[i],solution[(i+1)%NOMBRE_DE_VILLES]
        eval_fitness+= 1 / distances[origine][destination]
    return eval_fitness

def selection(fitness, nbr_parents, population):
    fitness = list(fitness)
    parents = np.empty((nbr_parents, population.shape[1]))
    for i in range(nbr_parents):
        indice_max_fitness = np.where(fitness == np.max(fitness))
        parents[i,:] = population[indice_max_fitness[0][0], :]
        fitness[indice_max_fitness[0][0]] = -999999
    return parents

def croisement(parents, nbr_enfants):
    enfants = np.empty((nbr_enfants, parents.shape[1]))
    point_de_croisement = int(parents.shape[1]/2) #croisement au milieu
    taux_de_croisement = 0.8
    i=0
    while (i < nbr_enfants): #parents.shape[0]
        indice_parent1 = i%parents.shape[0]
        indice_parent2 = (i+1)%parents.shape[0]
        x = rd.random()
        if x > taux_de_croisement: # parents stériles
            continue
        indice_parent1 = i%parents.shape[0]
        indice_parent2 = (i+1)%parents.shape[0]
        enfants[i,0:point_de_croisement] = parents[indice_parent1,0:point_de_croisement]
        enfants[i,point_de_croisement:] = parents[indice_parent2,point_de_croisement:]
        i+=1
    return enfants

# La mutation consiste à inverser le bit
def mutation(enfants):
    print("enfants.shape",enfants)
    mutants = np.empty((enfants.shape))
    print("mutants",mutants)
    taux_mutation = 0.5
    for i in range(mutants.shape[0]):
        random_valeur = rd.random()
        print("ENFANTS: ",enfants)
        mutants[i,:] = enfants[i,:]
        if random_valeur > taux_mutation:
            continue
        int_random_valeur = randint(0,enfants.shape[1]-1) #choisir aléatoirement le bit à inverser   
        if mutants[i,int_random_valeur] == 0 :
            mutants[i,int_random_valeur] = 1
        else :
            mutants[i,int_random_valeur] = 0
    return mutants  

def optimize(solution, distances, taille_tab, nbr_generations):
    sol_opt, historique_fitness = [], []
    nbr_parents = pop_size[0]//2
    nbr_enfants = pop_size[0] - nbr_parents 
    for i in range(nbr_generations):
        fitness = cal_fitness(solution,distances,NOMBRE_DE_VILLES)
        historique_fitness.append(fitness)
        parents = selection(fitness, nbr_parents, solution)
        enfants = croisement(parents, nbr_enfants)
        mutants = mutation(enfants)
        solution[0:parents.shape[0], :] = parents
        solution[parents.shape[0]:, :] = mutants
    print('Voici la dernière génération de la population: \n{}\n'.format(solution)) 
    fitness_derniere_generation = cal_fitness(solution, distances, taille_tab, nbr_generations)      
    print('Fitness de la dernière génération: \n{}\n'.format(fitness_derniere_generation))
    max_fitness = np.where(fitness_derniere_generation == np.max(fitness_derniere_generation))
    sol_opt.append(population[max_fitness[0][0],:])
    return sol_opt, historique_fitness


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
NOMBRE_DE_VILLES = 10
distances = np.zeros((NOMBRE_DE_VILLES, NOMBRE_DE_VILLES))
MAX_DISTANCE=2000
for ville in range(NOMBRE_DE_VILLES):
    villes = [ i for i in range(NOMBRE_DE_VILLES) if not i == ville ]
    for vers_la_ville in villes:
        distances[ville][vers_la_ville] =rd.randint(50, MAX_DISTANCE)
        distances[vers_la_ville][ville] =distances[ville][vers_la_ville]
print('voici la matrice des distances entres les villes \n',distances)

# Créer la population initiale
population_initiale = np.zeros((NOMBRE_DE_VILLES, NOMBRE_DE_VILLES))
for i in range(NOMBRE_DE_VILLES):
        population_initiale[i] = rd.sample(range(NOMBRE_DE_VILLES),NOMBRE_DE_VILLES)    
population_initiale = population_initiale.astype(int)
print(population_initiale)

for i in range(NOMBRE_DE_VILLES):
    nouv_sol=voisinage(population_initiale[i]*1,NOMBRE_DE_VILLES)
    cout0=cal_distance(population_initiale[i],distances,NOMBRE_DE_VILLES)
    cout_min_sol=cout0
    cout1=cal_distance(nouv_sol,distances,NOMBRE_DE_VILLES)
    if cout1<cout0:
        cout0=cout1
        population_initiale[i]=nouv_sol
    if cout1<cout_min_sol:
        cout_min_sol=cout1
        min_sol=population_initiale[i]
nbr_generations = 100 # nombre de générations
#lancement de l'algorithme génétique
sol_opt, historique_fitness = optimize(population_initiale, distances,(10,10), nbr_generations)



        




