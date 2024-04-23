import random
import pulp
import time
import psutil

inicio = time.time()#inicia contador de tiempo
process = psutil.Process()
random.seed(42)#semilla para replicar experimento
num_ciudades = 10000  #cantidad de ciudades
num_conjuntos = 20  #cantidad de subconjuntos 

N = range(1, num_ciudades + 1)
M = range(1, num_conjuntos + 1)

#costo asociado a cada conjunto 
C = {j: random.randint(1, 10) for j in M}

#matriz de asig binaria aleatoria 
a = {(i, j): random.randint(0, 1) for i in N for j in M}

#general el problema
prob = pulp.LpProblem("SetCoveringProblem", pulp.LpMinimize)

#variablerss de decision binarias
X = {j: pulp.LpVariable("X%d" % j, cat=pulp.LpBinary) for j in M}

#fun objetivo
prob += sum(C[j] * X[j] for j in M), "Cost"

#restricciones de cobertura
for i in N:
    prob += sum(a[i, j] * X[j] for j in M) >= 1, "Covering_%d" % i

#resolver el problema
prob.solve()

#resultados
print("Estado:", pulp.LpStatus[prob.status])
print("Costo mínimo:", pulp.value(prob.objective))
print("Asignación de conjuntos:")
for j in M:
    if X[j].varValue == 1:
        print("Conjunto", j)
termino = time.time()#terminan el contador de tiempo
memory_used = process.memory_info().rss / (1024 * 1024) 
cpu_usage = psutil.cpu_percent()
tiempoEjecucion = termino - inicio
print("Tiempo de es de: {:.7f} segundos".format(tiempoEjecucion))
print(f"Uso de CPU: {cpu_usage}%")
print(f"Memoria utilizada: {memory_used} MB")