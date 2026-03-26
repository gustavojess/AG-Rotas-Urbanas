#ALGORITMO GENÉTICO PARA ROTAS

import random
import numpy as np

pontos = np.array([(random.randint(0,100), random.randint(0,100)) for _ in range(5)])
matriz_distancia = []
for i in range(5):
    linha = []
    for j in range(5):
        dist = np.linalg.norm(pontos[i] - pontos[j])
        linha.append(dist)
    matriz_distancia.append(linha)
   

print(np.array(pontos))
print(np.array(matriz_distancia))

populacao = np.array([random.sample(range(5), 5) for _ in range(20)])

print(np.array(populacao))

def distancia (p1, p2):
    distancia = np.linalg.norm(p1 - p2)

    return distancia

def avaliar (populacao):
    origem = np.array([0,0])
    fitness_notas = []

    for individuo in populacao:
        custo_total = 0
        primeira_cidade = pontos[individuo[0]]
        custo_total += distancia(origem, primeira_cidade)

        for j in range(0, len(individuo) - 1):
            atual = individuo[j]
            proximo = individuo[j+1]
            custo_total += matriz_distancia[atual][proximo]
        
        ultima_cidade = pontos[individuo[-1]]
        custo_total += distancia(ultima_cidade, origem)

        fitness = 1/(1 + custo_total)
        fitness_notas.append(fitness)

    return fitness_notas

def selecao(populacao, fitness_notas):

    selecionados = []

    k = 3
    
    for i in range(len(populacao)):
        torneio = []
        maior_fitness = -999
        melhor_indice = -1
        escolhido = []  
        for j in range(k):
            indice_escolhido = random.randint(0, len(populacao) - 1)
            torneio.append(indice_escolhido)
        
        for x in range(len(torneio)):
            indice_individuo = torneio[x]
            if fitness_notas[indice_individuo] > maior_fitness:
                maior_fitness = fitness_notas[indice_individuo]
                melhor_indice = indice_individuo
        
        escolhido = populacao[melhor_indice]  
        selecionados.append(escolhido)
    return selecionados



fitness = avaliar(populacao)
pais = selecao(populacao, fitness)
print(np.array(fitness))
print(np.array(pais))


        
