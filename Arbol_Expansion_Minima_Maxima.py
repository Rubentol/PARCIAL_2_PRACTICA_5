#Practica #5: Arbol de Expasion Minima y Maxima 

# Grafo representado como una lista de aristas (vértice1, vértice2, peso)
grafo = [(0, 1, 2), (0, 2, 3), (1, 2, 4), (1, 3, 1), (2, 3, 5)]

# Función para encontrar el conjunto al que un nodo pertenece
def encontrar(conjuntos, nodo):
    if conjuntos[nodo] != nodo:
        conjuntos[nodo] = encontrar(conjuntos, conjuntos[nodo])
    return conjuntos[nodo]

# Función para unir dos conjuntos
def unir(conjuntos, rango, nodo1, nodo2):
    raiz1 = encontrar(conjuntos, nodo1)
    raiz2 = encontrar(conjuntos, nodo2)
    if rango[raiz1] < rango[raiz2]:
        conjuntos[raiz1] = raiz2
    elif rango[raiz1] > rango[raiz2]:
        conjuntos[raiz2] = raiz1
    else:
        conjuntos[raiz1] = raiz2
        rango[raiz2] += 1

# Algoritmo para encontrar el MST de Kruskal
def kruskal_mst(grafo):
    grafo = sorted(grafo, key=lambda x: x[2])
    conjuntos = list(range(len(grafo)))
    rango = [0] * len(grafo)
    mst = []
    for arista in grafo:
        nodo1, nodo2, peso = arista
        if encontrar(conjuntos, nodo1) != encontrar(conjuntos, nodo2):
            mst.append(arista)
            unir(conjuntos, rango, nodo1, nodo2)
    return mst

# Algoritmo para encontrar el MXA de Kruskal
def kruskal_mxa(grafo):
    grafo = sorted(grafo, key=lambda x: -x[2])
    conjuntos = list(range(len(grafo)))
    rango = [0] * len(grafo)
    mxa = []
    for arista in grafo:
        nodo1, nodo2, peso = arista
        if encontrar(conjuntos, nodo1) != encontrar(conjuntos, nodo2):
            mxa.append(arista)
            unir(conjuntos, rango, nodo1, nodo2)
    return mxa

# Obtener el MST y MXA
mst = kruskal_mst(grafo)
mxa = kruskal_mxa(grafo)

print("Árbol de Expansión Mínima (MST) de Kruskal:")
print(mst)
print("Árbol de Expansión Máxima (MXA) de Kruskal:")
print(mxa)
