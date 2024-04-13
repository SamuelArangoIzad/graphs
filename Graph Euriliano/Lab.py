import numpy as np
import random

#Matriz y sus conexiones
grafo = np.array([
    #A  B  C  D  E  F
    [0, 1, 1, 1, 1, 0], #A
    [1, 0, 0, 1, 0, 0], #B
    [1, 0, 0, 1, 1, 1], #C
    [1, 1, 1, 0, 0, 1], #D
    [1, 0, 1, 0, 0, 0], #E
    [0, 0, 1, 1, 0, 0]  #F
])

"""Creamos el grafo a partir de la matriz, parametros: guia_matriz , que es la
representacion de la matriz de adyacencia y retorna grafo que es lista de 
adyacencia del grafo"""
def creacion_del_grafo(guia_matriz):
    conservacion = len(guia_matriz)#Obtenemos el numero de nodos del grafo con len, por medio de fila o columnas
    #es una matriz cuadrada entonces sera la misma su columna a su fila de nodo
    grafo = [[]for _ in range(conservacion)]#creamos una lista vacia para cada nodo
    for ii in range(conservacion):#Itera sobre todos los pares de nodos en la matriz de adyacencia
        for jj in range(ii+1, conservacion):#Evitamos recorrer la matriz diagonal y elementos que ya se recorrieron
            if guia_matriz[ii][jj]==1:#si hay una arista entre los nodos ii y jj añade
                #jj a la lista de adyacencia de ii y viceversa, ya que esto es simetrico
                grafo[ii].append(jj)
                grafo[jj].append(ii)
    return grafo#Retornamos la lista del grafo creado
"""Realizamos una busqueda en el grafo ´para encontrar el ciclo euriliano, parametros: grafo, lista de
adyacencia del grafo , conservacion: nodo actual, nodovisitado: lista de nodos visitados, aristavisitada: conjunto de aristas
visitadas , ciclo_ lista que almacenara el ciclo euriliano. Retorna modifica el ciclo """
def buscar_grafo(grafo, conservacion, nodovisitado, aristavisitada, ciclo):
    nodovisitado[conservacion] = True #Marcamos el actual como visitado , y conservacion
    #xse vuelve el indice de nodo actual en la lista de adyacencia grafo y marcamos el nodo
    #como ya visto
    ciclo.append(chr(conservacion + 65))#pasamos de numero a letra y agregamos el nodo al ciclo euriliano
    #conservacion de suma a 65 y se convierte en el correspondiente en letra mayuscula
    for ii in grafo[conservacion]:#iteramos en los nodos adyacentes al nodo actual
        if(conservacion, ii) not in aristavisitada:# Si la arista no ha sido visitada
            aristavisitada.add((conservacion,ii))# Agregamos la arista al conjunto de aristas visitadas
            aristavisitada.add((ii, conservacion))# Agregamos la arista inversa también
            buscar_grafo(grafo, ii, nodovisitado, aristavisitada, ciclo)# Llamada recursiva para explorar el nodo adyacente

#Aun no hemos usado numpy o random
""" Encontramos el respectivo ciclo eurilianos variables grafo,retorna ciclo de lista que representa e ciclo euriliano"""
def encontrarCicloEuriliano(grafo):
    gradosimpares = sum(len(guiacontador)%2 for guiacontador in grafo)
    if gradosimpares != 0:# Si hay nodos con grado impar, no hay ciclo euleriano
        return None
    visitado = [False]*len(grafo)#creamos una lista que se llama visitado con la misma longitud
    #del grafo cada elemento de esta lista se inicializa como false, y es de apoyo para buscar que ya
    #ha sido visitado
    empezar_nodo = random.randint(0, len(grafo)-1)#generamos un inicio aleatorio entre a y b
    #es decir entre 0 y la cantidad maxima del grafo -1 ya que 0 es 1
    ciclo = []#aca almacenamos el ciclo euriliano
    buscar_grafo(grafo, empezar_nodo, visitado, set(), ciclo)#buscamos grafos para inicia su busqueda
    #en profundidad desde el nodo inicial seleciconado de forma aleatoria y se pasan como argumento
    ciclo.append(chr(empezar_nodo + 65))
    return ciclo

"""________________________________________________________________"""
grafo = creacion_del_grafo(grafo)
ciclo = encontrarCicloEuriliano(grafo)
print ("\n RUTA DEL GRAFO ")
if ciclo:
    print("IT IS EURILIANOOOOOOOOOOOOOOO")
    print(ciclo)
else:
    print("NO HAY CICLO EURILIANO WTF!")

    #Y los nodos adyacentes son los q están directamente conectados a un nodo dado en un grafo.
    #Usamos set que crea un conjunto vacio se usa para utilizar la inicializacion de un conjunto vacio
    #ese conjunto se pasa como argumento en buscar_grafo

    #COMO FUNCIONA ESO DE CHR +65 SI QUEREMOS QUE SALGA SOLO NUMEROS DEJAMOS CICLO.APPEND(EMPEZAR_NODO)
    #chr +65 devuelve A es algo interno de python

    #grafo = [[] for _ in range(conservacion)]  la linea significa inicializar una lista de listas
    """[[] for _ in range(conservacion)]: 
    Esto crea una lista que contiene conservacion sublistas vacías. Cada sublista vacía
     representa los nodos adyacentes de un nodo en el grafo."""