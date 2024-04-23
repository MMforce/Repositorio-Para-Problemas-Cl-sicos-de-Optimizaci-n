set N;   # Conjunto de elementos a cubrir

set M;   # Conjunto de subconjuntos disponibles

param C{j in M};  # Costo asociado al conjunto j

param a{i in N, j in M};  # Matriz de asignación binaria

var X{j in M} binary;  # Variables de decisión binarias

minimize Cost: sum{j in M} C[j] * X[j];  # Función objetivo

subject to Covering{i in N}:  # Restricción de cobertura
    sum{j in M} a[i, j] * X[j] >= 1;

