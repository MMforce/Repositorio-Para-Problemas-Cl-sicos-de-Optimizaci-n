import random
import subprocess
import time
import psutil

random.seed(1)#semilla para replicar experimento
inicio = time.time()#inicia contador de tiempo
process = psutil.Process()

#genera la data de forma aleatoria (similar a matriz NxM)
def generate_random_data(N, M):
    C = {j: random.randint(1, 10) for j in range(1, M + 1)}
    a = {(i, j): random.randint(0, 1) for i in range(1, N + 1) for j in range(1, M + 1)}
    return C, a

#edita archivo AMPL llamado "setcovering.dat"
def write_dat_file(N, M, C, a):
    with open('setcovering.dat', 'w') as f:
        f.write('set N := {};\n'.format(' '.join(map(str, range(1, N + 1)))))
        f.write('set M := {};\n'.format(' '.join(map(str, range(1, M + 1)))))
        f.write('param C :=\n')
        for j, c in C.items():
            f.write('\t{} {}\n'.format(j, c))
        f.write(';\n')
        f.write('param a :')
        for j in range(1, M + 1):
            f.write(' {}'.format(j))
        f.write(' :=\n')
        for i in range(1, N + 1):
            f.write('{}\t'.format(i))
            for j in range(1, M + 1):
                f.write('{} '.format(a[(i, j)]))
            f.write('\n')
        f.write(';\n')

#generar datos aleatorios para N y M
N = 2000
M = 2000

#generar datos aleatorios
C, a = generate_random_data(N, M)

#escribe los datos en archivo .dat
write_dat_file(N, M, C, a)

#ejecuta ampl a traves de cmd
cmd = 'ampl setcovering.run'
output = subprocess.run(cmd, shell=True, capture_output=True, text=True)

#medir el tiempo luego de la ejecucion
memory_used = process.memory_info().rss / (1024 * 1024) 
cpu_usage = psutil.cpu_percent()
termino = time.time()
#calcular tiempo
tiempoEjecucion = termino - inicio
print("Tiempo de AMPL: {:.7f} segundos".format(tiempoEjecucion))
print(f"Uso de CPU: {cpu_usage}%")
print(f"Memoria utilizada: {memory_used} MB")