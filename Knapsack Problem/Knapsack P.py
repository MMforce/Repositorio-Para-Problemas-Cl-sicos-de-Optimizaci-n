import random
import pulp
import psutil
import time

inicio = time.time()
process = psutil.Process()
random.seed(0) 
#numero de elementos 
num_elementos = 50000 

PESOMAX = 100  #peso max permitido


#generar valores y pesos aleatorios para cada elemento
VALOR = {i: random.randint(1, 20) for i in range(1, num_elementos + 1)}
PESO = {i: random.randint(1, 20) for i in range(1, num_elementos + 1)}

#conjunto que indica el rango para cada elemento
ELEMENTOS = range(1, num_elementos + 1)

#crea un problema de optimizacion de max
prob = pulp.LpProblem("Knapsack", pulp.LpMaximize)

#variable binaria que indica si el objeto es tomado o no
take = pulp.LpVariable.dicts("Take", ELEMENTOS, cat=pulp.LpBinary)

#func objetivo que maximiza el valor total de objetos
prob += pulp.lpSum(VALOR[i] * take[i] for i in ELEMENTOS)

#rest de peso
prob += pulp.lpSum(PESO[i] * take[i] for i in ELEMENTOS) <= PESOMAX

#resolver el problema
prob.solve()

#impresion el resultado
if pulp.LpStatus[prob.status] == "Optimal":
    print("Solución óptima encontrada:")
    for i in ELEMENTOS:
        if take[i].value() == 1:
            print(f"Elemento {i} - Valor: {VALOR[i]}, Peso: {PESO[i]}")
else:
    print("No se encontró una solución óptima.")


memory_used = process.memory_info().rss / (1024 * 1024) 
cpu_usage = psutil.cpu_percent()
termino = time.time()
tiempoEjecucion = termino - inicio
print(f"Memoria utilizada: {memory_used} MB")
print(f"Uso de CPU: {cpu_usage}%")
print(f"tiempo de ejecución: {tiempoEjecucion:.10}  segundos")