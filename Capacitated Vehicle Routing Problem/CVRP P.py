import random
import time
import psutil

random.seed(1)#semilla que permite replicar experimento
inicio = time.time()#inicia contador de tiempo
process = psutil.Process()

num_nodos = 19#num de nodos que se puede modificar
nodos = list(range(1, num_nodos + 1))
capacidad = 20#define la capacidad de los vehiculos
demanda = {i: random.randint(1, 5) for i in nodos}#genera de forma aleatoria la demanda de cada nodo
distancia = {i: {j: random.randint(1, 10) for j in nodos} for i in nodos}#genera de forma aleatoria la distancia de cada nodo

#func para calcular la distancia total de una ruta
def calcular_distancia_ruta(ruta):
    distancia_total = 0
    for i in range(len(ruta) - 1):
        distancia_total += distancia[ruta[i]][ruta[i + 1]]
    return distancia_total

#func para generar una solu inicial
def generar_solucion_inicial():
    vehiculos = [[] for _ in range(capacidad)]
    nodos_restantes = nodos.copy()
    nodos_restantes.remove(1) #elimina ek deposito
    random.shuffle(nodos_restantes)
    for nodo in nodos_restantes:
        asignado = False
        for v in vehiculos:
            if sum(demanda[i] for i in v) + demanda[nodo] <= capacidad:
                v.append(nodo)
                asignado = True
                break
        if not asignado:
            vehiculos.append([nodo])
    return vehiculos

#fun para calcular la distancia total de una ruta
def calcular_distancia_ruta(ruta):
    distancia_total = 0
    for i in range(len(ruta) - 1):
        distancia_total += distancia[ruta[i]][ruta[i + 1]]
    return distancia_total

#fun para fusionar dos rutas
def fusionar_rutas(ruta1, ruta2):
    #combinar dos rutas eliminando los duplicados
    nueva_ruta = ruta1[:-1] + ruta2[1:]
    #verifica si la nueva ruta cumple con la capacidad
    capacidad_actual = 0
    for nodo in nueva_ruta:
        capacidad_actual += demanda[nodo]
        if capacidad_actual > capacidad:
            return None  #nueva ruta excede la capacidad
    return nueva_ruta

#fun de dividir y conquistar
def dividir_conquistar(vehiculos):
    if len(vehiculos) == 1:
        return vehiculos
    else:
        #dividir la lista de vehiculos en dos partes
        mitad = len(vehiculos) // 2
        parte_izquierda = vehiculos[:mitad]
        parte_derecha = vehiculos[mitad:]

        #llama recursivamente a la func para cada mitad
        parte_izquierda = dividir_conquistar(parte_izquierda)
        parte_derecha = dividir_conquistar(parte_derecha)

        #fusionar las soluciones de las dos partes
        solucion_combinada = fusionar_rutas(parte_izquierda[-1], parte_derecha[0])
        if solucion_combinada:
            return parte_izquierda[:-1] + [solucion_combinada] + parte_derecha[1:]
        else:
            return parte_izquierda + parte_derecha

#genera solucion inicial
solucion_inicial = generar_solucion_inicial()

#mejora la solucion mediante algoritmo
mejor_solucion = dividir_conquistar(solucion_inicial)

#calcula la distancia total, buscando la optima
mejor_distancia = calcular_distancia_ruta([1] + sum(mejor_solucion, []) + [1])

memory_used = process.memory_info().rss / (1024 * 1024)#obtiene la cantidad de MB utilizados por la RAM
cpu_usage = psutil.cpu_percent()#porcentaje de cpu
termino = time.time()#termino de tiempo
tiempoEjecucion = termino - inicio#calcula tiempo real

#resultados
print("Distancia total:", mejor_distancia)
print("Tiempo de ejecución: {:.7f} segundos".format(tiempoEjecucion))
print(f"Uso de CPU: {cpu_usage}%")
print(f"Memoria utilizada: {memory_used} MB")


