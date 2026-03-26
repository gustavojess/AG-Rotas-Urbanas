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
        
