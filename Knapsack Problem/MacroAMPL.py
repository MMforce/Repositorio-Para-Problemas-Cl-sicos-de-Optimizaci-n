import random
import subprocess
import time
import psutil

inicio = time.time()
random.seed(1)


process = psutil.Process()

def generar_datos_knapsack(num_elementos, peso_max):
    #generar valores y pesos aleatorios para los elementos
    valores = {f'objeto_{i}': random.randint(1, 20) for i in range(1, num_elementos+1)}
    pesos = {f'objeto_{i}': random.randint(1, 20) for i in range(1, num_elementos+1)}

#escribir los datos en un archivo
    with open('knapsack.dat', 'w') as f:
        f.write("param PESOMAX := {};\n".format(peso_max))
        f.write("set ELEMENTOS := " + ' '.join([f'objeto_{i}' for i in range(1, num_elementos+1)]) + ";\n")
        f.write("param VALOR :=\n")
        for objeto, valor in valores.items():
            f.write("\t{} {}\n".format(objeto, valor))
        f.write(";\n")
        f.write("param PESO :=\n")
        for objeto, peso in pesos.items():
            f.write("\t{} {}\n".format(objeto, peso))
        f.write(";\n")

#num de elementos
num_elementos = 100000

#peso max permitido
peso_max = 100
generar_datos_knapsack(num_elementos, peso_max)


#ejecutar AMPL
subprocess.run(["python", "generar_datos_knapsack.py", str(num_elementos), str(peso_max)])

#lee el archivo cvrp.dat y mostrar su contenido
with open("knapsack.dat", "r") as f:
    datos_cvrp = f.read()

#terminar mediciones e impriomir resultados
Memoria_usada = process.memory_info().rss / (1024 * 1024) 
cpu_usada = psutil.cpu_percent()
termino = time.time()
tiempoEjecucion = termino - inicio
print("Tiempo de ejecución de AMPL: {:.7f} segundos".format(tiempoEjecucion))
#print(datos_cvrp) #EVITAR UTILIZAR PARA num_elementos >= 50
print(f"Uso de CPU: {cpu_usada}%")
print(f"Memoria utilizada: {Memoria_usada} MB")

