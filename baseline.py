#Algoritmo baseline usando a técnica de busca por Vizinho Mais Próximo

import random
import numpy as np
import csv
import time

inicio = time.perf_counter()

#pontos = np.array([(random.randint(0,100), random.randint(0,100)) for _ in range(20)])

pontos = []

with open('20_pontos.csv', 'r') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)
    next(leitor_csv) 
    for linha in leitor_csv:
        ponto = (float(linha[0]), float(linha[1]))
        pontos.append(ponto)
pontos = np.array(pontos)

matriz_distancia = []
for i in range(20):
    linha = []
    for j in range(20):
        dist = np.linalg.norm(pontos[i] - pontos[j])
        linha.append(dist)
    matriz_distancia.append(linha)


print(np.array(pontos))
print(np.array(matriz_distancia))

def distancia (p1, p2):
    distancia = np.linalg.norm(p1 - p2)

    return distancia
def vizinho_mais_proximo(pontos, matriz_distancia):

    origem = np.array([0,0])
    cidade_inicial = distancia(origem, pontos).argmin()  # Encontra a cidade mais próxima da origem
    caminho = [cidade_inicial]
    nao_visitadas = set(range(len(pontos))) - {cidade_inicial} 
    cidade_atual = cidade_inicial
    custo_total = distancia(origem, pontos[cidade_inicial])

    while nao_visitadas:
        menor_distancia = float('inf')
        proxima_cidade = None

        for pontos in nao_visitadas:
            dist = matriz_distancia[cidade_atual][pontos]
            if dist < menor_distancia:
                menor_distancia = dist
                proxima_cidade = pontos

        if proxima_cidade is None:
            break

        caminho.append(proxima_cidade)
        nao_visitadas.remove(proxima_cidade)
        cidade_atual = proxima_cidade
        custo_total += menor_distancia

    return caminho, custo_total

caminho, custo_total = vizinho_mais_proximo(pontos, matriz_distancia)
print("Caminho encontrado:", caminho)
print("Custo total:", custo_total)
fim = time.perf_counter()
tempo_total = fim - inicio

meus_dados = [
    custo_total,
    tempo_total
]

with open('resultados_baseline.csv', 'w', newline='') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv)
    escritor_csv.writerow(['Custo Total', 'Tempo Total'])
    escritor_csv.writerow(meus_dados)




