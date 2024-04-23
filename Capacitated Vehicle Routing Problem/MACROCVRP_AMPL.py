import random
import subprocess
import time
import psutil

random.seed(1)#semilla para replicar experimento
inicio = time.time()#inicia contador de tiempo
process = psutil.Process()

#genera datos aleatorios
def generar_datos(num_nodos):
    capacidad = 20#define la capacidad maxima de los vehiculos
    demandas = {i: random.randint(1, 5) for i in range(1, num_nodos + 1)}#genera demandas aleatorias para cada nodo
    distancia = {(i, j): random.randint(1, 10) for i in range(1, num_nodos + 1) for j in range(1, num_nodos + 1)}#genera distancias aleatorias entre nodos
    return num_nodos, capacidad, demandas, distancia

#edita ek archivo cvrp.dat
def editar_archivo_cvrp(num_nodos, capacidad, demandas, distancia):
    with open("cvrp.dat", "w") as f:
        f.write("set nodos := {};\n".format(" ".join(map(str, range(1, num_nodos + 1)))))
        f.write("param capacidad := {};\n\n".format(capacidad))

        f.write("param demanda :=\n")
        for nodo, demanda in demandas.items():
            f.write("\t{} {}\n".format(nodo, demanda))
        f.write(";\n\n")

        f.write("param distancia :\n\t")
        f.write(" ".join(map(str, range(1, num_nodos + 1))) + " :=\n")
        for i in range(1, num_nodos + 1):
            f.write("\t{}".format(i))
            for j in range(1, num_nodos + 1):
                f.write(" {}".format(distancia[(i, j)]))
            f.write("\n")
        f.write(";\n")

num_nodos = 11 #número de nodos a editar
#llama a las funciones
num_nodos, capacidad, demandas, distancia = generar_datos(num_nodos)#genera los datos de forma aleatoria (demandas y distancia)
editar_archivo_cvrp(num_nodos, capacidad, demandas, distancia)#edita el archivo cvrp.dat

#ejecuta ampl a traves de cmd
cmd = 'ampl cvrp.run'
output = subprocess.run(cmd, shell=True, capture_output=True, text=True)

memoria_usada = process.memory_info().rss / (1024 * 1024)
cpu_usada = psutil.cpu_percent()#porcentaje de cpu utilizada
termino = time.time()#termino de tiempo
tiempoEjecucion = termino - inicio#calcula el tiempo real en segundos

#print(datos_cvrp) #EVITAR UTILLIZAR PARA GRANDES NUMEROS (desde 50 en adelante)
print("Tiempo de ejecución de AMPL: {:.7f} segundos".format(tiempoEjecucion))
print(f"Memoria utilizada: {memoria_usada} MB")
print(f"Uso de CPU: {cpu_usada}%")


