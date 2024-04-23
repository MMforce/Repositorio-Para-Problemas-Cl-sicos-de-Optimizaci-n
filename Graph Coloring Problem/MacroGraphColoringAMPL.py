import random
import subprocess
import time
import psutil
random.seed(2)


def generate_random_graph_data(num_vertices, num_edges, max_colors):
    vertices = list(range(1, num_vertices + 1))
    edges = []
    for i in range(num_edges):
        u = random.choice(vertices)
        v = random.choice(vertices)
        if u != v and (u, v) not in edges and (v, u) not in edges:
            edges.append((u, v))

    return vertices, edges, max_colors

def write_dat_file(filename, num_vertices, num_edges, edges, max_colors):
    with open(filename, 'w') as file:
        file.write("param n := {};\n".format(num_vertices))
        file.write("param m := {};\n".format(num_edges))
        file.write("set E := ")
        for edge in edges:
            file.write("({}, {}) ".format(edge[0], edge[1]))
        file.write(";\n")
        file.write("param max_colors := {};\n".format(max_colors))

if __name__ == "__main__":
    inicio = time.time()
    process = psutil.Process()
    num_vertices = 1000 
    num_edges = 100000#random.randint(num_vertices - 1, (num_vertices*(num_vertices-1)) // 2)
    max_colors = random.randint(3, (num_vertices-1)) 

    vertices, edges, max_colors = generate_random_graph_data(num_vertices, num_edges, max_colors)

    write_dat_file("gcoloring.dat", num_vertices, num_edges, edges, max_colors)
    cmd = 'ampl gcoloring.run'
    output = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    memory_used = process.memory_info().rss / (1024 * 1024) 
    cpu_usage = psutil.cpu_percent()
    termino = time.time()
    tiempoEjecucion = termino - inicio
    print("Tiempo de AMPL: {:.7f} segundos".format(tiempoEjecucion))
    print(f"Uso de CPU: {cpu_usage}%")
    print("Memoria utilizada: {:.2f} MB".format(memory_used))