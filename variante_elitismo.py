#ALGORITMO GENÉTICO PARA ROTAS

import random
import numpy as np
import csv
import time
import os

inicio = time.perf_counter()

pontos = np.array([(random.randint(0,100), random.randint(0,100)) for _ in range(20)])
matriz_distancia = []
for i in range(20):
    linha = []
    for j in range(20):
        dist = np.linalg.norm(pontos[i] - pontos[j])
        linha.append(dist)
    matriz_distancia.append(linha)


print(np.array(pontos))
print(np.array(matriz_distancia))

populacao = np.array([random.sample(range(20), 20) for _ in range(100)])
print(populacao)

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
        maior_fitness = -float('inf')
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
        
        escolhido = populacao[melhor_indice].copy()
        selecionados.append(escolhido)
    return selecionados

def ox (pai1, pai2, ponto1, ponto2):

    filho = np.full(len(pai1), -1)
    filho[ponto1:ponto2] = pai1[ponto1:ponto2]

    pos = ponto2

    for j in range (len(pai2)):
        gene = pai2[(ponto2 + j) % len(pai2)]
                
        if gene not in filho:

            filho[pos % len(pai2)] = gene
            pos += 1

    return filho

def cruzamento (pais):

    filhos = []

    for i in range(0, len(pais), 2):

        if i+1 < len(pais):

            pai1 = pais[i]
            pai2 = pais[i+1]
            
            while True:
                ponto1, ponto2 = sorted(np.random.choice(len(pai1), 2, replace=False))
                if (ponto2 - ponto1 >= 3) and (ponto2 - ponto1 <= 5):
                    break

            filho1 = ox(pai1, pai2, ponto1, ponto2)
            filho2 = ox(pai2, pai1, ponto1, ponto2)

            filhos.append(filho1)
            filhos.append(filho2)

    return filhos

def mutacao (filhos):
    novos_filhos = []
    for individuo in filhos:
        novo = individuo.copy()
        if random.random() < 0.05:
            posicao1, posicao2 = sorted(np.random.choice(len(individuo), 2, replace=False))
            novo[posicao1], novo[posicao2] = novo[posicao2], novo[posicao1]
        novos_filhos.append(novo)

    return novos_filhos

for geracao in range(200):    

    fitness = np.array(avaliar(populacao))
    media_fitness = np.mean(fitness)

    indices_melhores = np.argsort(fitness)[-2:]
    elites = populacao[indices_melhores].copy()

    pais = selecao(populacao, fitness)
    filhos = cruzamento(pais)
    populacao = np.array(mutacao(filhos))

    nota_filhos = avaliar(populacao)
    
    indices_piores = np.argsort(nota_filhos)[:2]
    populacao[indices_piores] = elites

    melhor_elite = elites[np.argmax(fitness[indices_melhores])]
    custo_total = 1/(fitness[np.argmax(fitness[indices_melhores])]) - 1
    print(f'Melhor indivíduo da {geracao + 1} geração: {melhor_elite} | Melhor Fitness: {max(fitness)} | Fitness média: {media_fitness} | Custo total: {custo_total}')

fim = time.perf_counter()
tempo_total = fim - inicio
print(f'Tempo total de execução: {tempo_total:.2f} segundos')

meus_dados = [

    melhor_elite,
    media_fitness,
    custo_total,
    tempo_total
]

with open('resultados_elitismo.csv', 'a', newline='') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv)
    if os.stat('resultados_elitismo.csv').st_size == 0:
        escritor_csv.writerow(['Melhor Individuo', 'Fitness Media', 'Custo Total', 'Tempo Total'])
    escritor_csv.writerow(meus_dados)

