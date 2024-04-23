import random
import time
import psutil

random.seed(1) 


def generar_grafo(num_ciudades, distancia_minima, distancia_maxima):
    grafo = [[0] * num_ciudades for _ in range(num_ciudades)]

    for i in range(num_ciudades):
        for j in range(i+1, num_ciudades):
            distancia = random.randint(distancia_minima, distancia_maxima)
            grafo[i][j] = distancia
            grafo[j][i] = distancia

    return grafo

def main(num_ciudades, distancia_minima):
    distancia_maxima = num_ciudades * distancia_minima

    grafo = generar_grafo(num_ciudades, distancia_minima, distancia_maxima)

    ciudades_visitadas = [False] * num_ciudades
    ruta_optima = []
    ciudad_actual = 0  #ciudad inicial

    while len(ruta_optima) < num_ciudades:
        ciudades_visitadas[ciudad_actual] = True
        ruta_optima.append(ciudad_actual)

        ciudad_mas_cercana = None
        distancia_minima = float('inf')

        for i in range(num_ciudades):
            if not ciudades_visitadas[i] and grafo[ciudad_actual][i] < distancia_minima:
                distancia_minima = grafo[ciudad_actual][i]
                ciudad_mas_cercana = i

        ciudad_actual = ciudad_mas_cercana

    ruta_optima.append(0)  #agrega la ciudad de partida al final para completar el ciclo
    
    #resultados
    memory_used = (process.memory_info().rss) / (1024 * 1024) 
    cpu_usage = psutil.cpu_percent()
    termino = time.time()
    tiempoEjecucion = termino - inicio
    print("Ruta óptima:", ruta_optima)
    print("Tiempo de ejecución de: {:.7f} segundos".format(tiempoEjecucion))
    print(f"Uso de CPU: {cpu_usage}%")
    print(f"Memoria utilizada: {memory_used} MB")

if __name__ == '__main__':
    inicio = time.time()
    process = psutil.Process() 
    num_ciudades = 1000
    distancia_minima = 1
    main(num_ciudades, distancia_minima)






