import random
import subprocess
import time
import psutil

random.seed(1)
inicio = time.time()
#genera los datos de forma aleatoria, en este caso las ciudades con su respectivas ciudadees
def generate_random_TSP_data(num_ciudades, distancia_max=20):
    Ciudades = list(range(1, num_ciudades + 1))
    Distancia = {}
    for i in Ciudades:
        for j in Ciudades:
            if i != j:
                Distancia[i, j] = random.randint(1, distancia_max)
    
    return Ciudades, Distancia

#edita el archivo TSP.dat
def EscribirTSP(num_ciudades, Distancia, filename="TSP.dat"):
    with open(filename, 'w') as file:
        file.write("set Ciudades := {};\n".format(' '.join(map(str, Ciudades))))
        file.write("param Distancia:\n")
        file.write("\t")
        for j in Ciudades:
            file.write("{} ".format(j))
        file.write(":=\n")
        for i in Ciudades:
            file.write("\t{} ".format(i))
            for j in Ciudades:
                if i != j:
                    file.write("{} ".format(Distancia[i, j]))
                else:
                    file.write("0 ")
            file.write("\n")
        file.write(";")

#define el num de ciudades que deseas generar
num_ciudades = 1000

#genera los datos aleatorios
Ciudades, Distancia = generate_random_TSP_data(num_ciudades)

#escribe los datos en el archivo "TSP.dat"
EscribirTSP(num_ciudades, Distancia)

process = psutil.Process()
#ejecuta AMPL y captura la salida

cmd = 'ampl TSP.run'
output = subprocess.run(cmd, shell=True, capture_output=True, text=True)

#impresion la salida de AMPL
print(output.stdout)


#mide el tiempo despues de la ejecucion
memory_used = process.memory_info().rss / (1024 * 1024) 
cpu_usage = psutil.cpu_percent()
termino = time.time()

#calcuña el tiempo transcurrido
tiempoEjecucion = termino - inicio
print("Tiempo de ejecución de AMPL: {:.7f} segundos".format(tiempoEjecucion))
print(f"Uso de CPU: {cpu_usage}%")
print(f"Memoria utilizada: {memory_used} MB")
