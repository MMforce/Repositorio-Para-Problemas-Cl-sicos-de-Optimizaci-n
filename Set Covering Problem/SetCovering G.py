import random
import gurobipy as gp
from gurobipy import GRB
import time
import psutil

#param
inicio = time.time()
process = psutil.Process()
random.seed(42)
num_ciudades = 2000 #ciudades 
num_conjuntos = 20  #subconjuntos

N = range(1, num_ciudades + 1)
M = range(1, num_conjuntos + 1)

#costo asociado a cada conjunto 
C = {j: random.randint(1, 10) for j in M}

#matriz de asigna binaria aleatoria 
a = {(i, j): random.randint(0, 1) for i in N for j in M}

#crear modelo
model = gp.Model("SetCoveringProblem")

#variables decisi binarias
X = model.addVars(M, vtype=GRB.BINARY, name="X")

#funcion objetivo
model.setObjective(sum(C[j] * X[j] for j in M), GRB.MINIMIZE)

#rest de cobertura
for i in N:
    model.addConstr(sum(a[i, j] * X[j] for j in M) >= 1, f"Covering_{i}")

#resolver el modelo
model.optimize()

#resultados
print("Costo mínimo:", model.objVal)
memory_used = process.memory_info().rss / (1024 * 1024)
cpu_usage = psutil.cpu_percent()
termino = time.time()
tiempoEjecucion = termino - inicio
print("Tiempo de es de: {:.7f} segundos".format(tiempoEjecucion))
print(f"Uso de CPU: {cpu_usage}%")
print(f"Memoria utilizada: {memory_used} MB")
