#Algoritmo baseline usando a técnica de busca por Vizinho Mais Próximo

import random
import numpy as np

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




