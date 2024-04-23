import random
import gurobipy as gp
from gurobipy import GRB
import psutil
import time

inicio = time.time()
process = psutil.Process()
random.seed(0)

#num de elementos 
num_elementos = 100

#peso max permitido
PESOMAX = 100

#generar valores y pesos aleatorios para cada elemento
VALOR = {i: random.randint(1, 20) for i in range(1, num_elementos + 1)}
PESO = {i: random.randint(1, 20) for i in range(1, num_elementos + 1)}

#conjunto que indica el rango para cada elemento
ELEMENTOS = range(1, num_elementos + 1)

#crear un nuevo modelo
modelo = gp.Model("Knapsack")

#crear variables
take = modelo.addVars(ELEMENTOS, vtype=GRB.BINARY, name="Take")

#establecer la funcion objetivo que maximiza el valor total de objetos
modelo.setObjective(sum(VALOR[i] * take[i] for i in ELEMENTOS), GRB.MAXIMIZE)

#establecer la restricción de peso
modelo.addConstr(sum(PESO[i] * take[i] for i in ELEMENTOS) <= PESOMAX)

#resolver el modelo
modelo.optimize()

#imprimir el resultado
if modelo.status == GRB.OPTIMAL:
    print("Solución óptima encontrada:")
    for i in ELEMENTOS:
        if take[i].x == 1:
            print(f"Elemento {i} - Valor: {VALOR[i]}, Peso: {PESO[i]}")
else:
    print("No se encontró una solución óptima.")

#calcular memoria utilizada, uso de CPU y tiempo de ejecucion
memory_used = process.memory_info().rss / (1024 * 1024)
cpu_usage = psutil.cpu_percent()
termino = time.time()
tiempoEjecucion = termino - inicio
print(f"Memoria utilizada: {memory_used} MB")
print(f"Uso de CPU: {cpu_usage}%")
print("Tiempo de ejecución: ", tiempoEjecucion, "segundos")
