set nodos;
param demanda{nodos} >= 0;
param capacidad >= 0;
param distancia{nodos, nodos};

var x{i in nodos, j in nodos} binary;  # 1 si el vehiculo viaja de i a j, 0 en caso contrario
var u{i in nodos} >= 0;                # Variable auxiliar para la carga de los vehiculos

minimize DistanciaTotal: #funcion objetivo, minimizar gastos
    sum {i in nodos, j in nodos} distancia[i, j] * x[i, j];

subject to RestriccionDemanda {i in nodos}:
    sum {j in nodos: j != i} x[i, j] = 1;

subject to RestriccionCapacidad {i in nodos}:#vehiculos poseen restriccion de carga
    sum {j in nodos: j != i} demanda[j] * x[j, i] <= u[i];

subject to CapacidadVehiculo {i in nodos}:#el vehiculo en una sola entrega debe ser capaz de satisfacer cliente
    u[i] <= capacidad;

subject to EliminacionSubTour {i in nodos, j in nodos: i != j and i != 1 and j != 1}:
    u[i] - u[j] + capacidad * x[i, j] <= capacidad - demanda[j];




