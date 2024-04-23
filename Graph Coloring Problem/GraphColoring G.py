import gurobipy as gp
from gurobipy import GRB
import networkx as nx
import random
import time
import psutil


def solve_graph_coloring(graph):
    
    #crear el modelo
    model = gp.Model('graph_coloring')

    #variables de decision
    nodes = list(graph.nodes())
    num_colors = len(nodes)
    colors = range(num_colors)
    x = model.addVars(nodes, colors, vtype=GRB.BINARY, name='x')

    #rest cada nodo tiene exactamente un color asignado
    model.addConstrs((x.sum(node, '*') == 1 for node in nodes), name='assign_one_color')

    #rest dos nodos adyacentes no pueden tener el mismo color
    model.addConstrs((x[node1, color] + x[node2, color] <= 1
                     for node1, node2 in graph.edges() for color in colors), name='different_colors')

    #funcion objt minimizar el num de colores utilizados
    model.setObjective(x.sum(), GRB.MINIMIZE)

    #resolver el modelo
    model.optimize()

    #obtener la solucion
    if model.status == GRB.OPTIMAL:
        solution = {}
        for node in nodes:
            for color in colors:
                if x[node, color].x > 0.5:
                    solution[node] = color
                    break
        return solution
    else:
        return None

#func base
if __name__ == '__main__':
    inicio = time.time()
    process = psutil.Process()
    random.seed(42)

    #genera los arcos aleatorios, utilizando como referencia el num de vertices
    numero_vertices = 500
    numero_arcos = int((numero_vertices - 1) * numero_vertices / 2)
    graph = nx.gnm_random_graph(numero_vertices, numero_arcos)


    #resolver el problema de coloracion de grafos
    solution = solve_graph_coloring(graph)

    #calcula el tiempo de ejec
    termino = time.time()
    tiempoEjecucion = termino - inicio

    #imprime en consola el grafo, la solucion y el tiempo de ejecucion
    print('Arcos:', graph.edges())
    memory_used = process.memory_info().rss / (1024 * 1024) 
    cpu_usage = psutil.cpu_percent()
    print(f"Memoria utilizada: {memory_used} MB")
    print(f"Uso de CPU: {cpu_usage}%")
    print('Solución:', solution)
    print('Tiempo de ejecución:', tiempoEjecucion, 'segundos')
    
