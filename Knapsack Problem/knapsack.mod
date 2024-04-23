#Conjunto de objetos
set ELEMENTOS;

#Peso permitido
param PESOMAX integer, >= 1;
#valor para cada objeto
param VALOR {ELEMENTOS} >= 0;
#Peso de cada objeto
param PESO {ELEMENTOS} >= 0;

#parámetro que almacena el valor del peso de los objetos seleccionados
param acum_peso default 0;
#acumula el valor de los objetos seleccionados
param accum_valor default 0;

#variable binaria que indica si el objeto es tomado o no  (1 - 0, respectivamente)
var take{ELEMENTOS} binary;
#Funcion objetivo que maximiza el valor total de objetos
maximize MaxVal:
		sum {i in ELEMENTOS} VALOR[i] * take[i];

#restriccion de peso
s.t. WEIGHT:
		sum {i in ELEMENTOS} PESO[i] * take[i] <= PESOMAX;

	
