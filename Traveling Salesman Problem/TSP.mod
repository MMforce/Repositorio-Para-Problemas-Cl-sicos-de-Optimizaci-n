set Ciudades;
param Distancia {Ciudades, Ciudades} >= 0;

var x {Ciudades, Ciudades} binary;

minimize DistanciaTotal:
    sum{i in Ciudades, j in Ciudades} Distancia[i,j] * x[i,j];

subject to VisitarCiudad {i in Ciudades}:
    sum{j in Ciudades: j != i} x[i,j] = 1;

subject to DejarCiudad {j in Ciudades}:
    sum{i in Ciudades: i != j} x[i,j] = 1;

