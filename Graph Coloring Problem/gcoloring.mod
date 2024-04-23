param n;  #vertices
param m;  #aristas

set V := 1..n;  #conjunto de vertices
set E within V cross V;  #conjunto de aristas

param max_colors;  #num max de colores

var x{V, 1..max_colors} binary;  #variable de decision

s.t. one_color_per_vertex {v in V}:
  sum{j in 1..max_colors} x[v, j] = 1;  #cada vertice debe tener un solo color

s.t. adjacent_vertices_same_color {i in 1..max_colors, (u,v) in E}:
  x[u, i] + x[v, i] <= 1;  #cvertices adyacentes no pueden tener el mismo color

minimize num_colors: sum{i in 1..max_colors} sum{v in V} x[v, i];  #min el numero de colores utilizados


