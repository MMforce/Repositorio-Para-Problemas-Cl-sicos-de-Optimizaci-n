using Random
using Printf

function generar_grafo(num_ciudades, distancia_minima, distancia_maxima)
    grafo = zeros(Int, num_ciudades, num_ciudades)#se crea una matriz vacia para representar el grafo
    for i in 1:num_ciudades#itera sobre todas las posibles conexiones entre ciudades
        for j in i+1:num_ciudades
            distancia = rand(distancia_minima:distancia_maxima)#se genera una distancia aleatoria entre las ciudades
            grafo[i, j] = distancia#se asigna la distancia entre la ciudad i y la ciudad j
            grafo[j, i] = distancia#la matriz es simétrica, se asigna la misma distancia entre la ciudad j y la ciudad i
        end
    end
    return grafo#retorna el grafo generado
end

function tsp(num_ciudades)
    Random.seed!(42)#una semilla aleatoria para reproducir experimento

    #se definen de los lpimites para la generación de distancias aleatorias
    distancia_minima = 1
    distancia_maxima = Int((num_ciudades * (num_ciudades - 1)) / 2)

    grafo = generar_grafo(num_ciudades, distancia_minima, distancia_maxima)#se genera un grafo aleatorio completo que representa las distancias entre ciudades
    ciudades_visitadas = falses(num_ciudades)#se inicia un arreglo para registrar las ciudades visitadas
    ruta_optima = Int[]#se iniciauna lista para almacenar la ruta óptima encontrada

    ciudad_actual = 1  #se elige la ciudad 1 como punto de partida
    while length(ruta_optima) < num_ciudades#mientras no se hayan visitado todas las ciudades
        ciudades_visitadas[ciudad_actual] = true #se marca la ciudad actual como visitada
        push!(ruta_optima, ciudad_actual)#se agrega la ciudad actual a la ruta óptima

        ciudad_mas_cercana = nothing
        distancia_minima = Inf

        #se busca la ciudad más cercana que no haya sido visitada
        for i in 1:num_ciudades
            if !ciudades_visitadas[i] && grafo[ciudad_actual, i] < distancia_minima
                distancia_minima = grafo[ciudad_actual, i]
                ciudad_mas_cercana = i
            end
        end

        ciudad_actual = ciudad_mas_cercana #se actualiza la ciudad actual
    end

    #agrega la ciudad de partida al final para completar el ciclo
    push!(ruta_optima, 1)
    
    #retorna la ruta óptima encontrada
    return ruta_optima
end

#almacena los datos en listas
tiempos_ejecucion = Float64[]
ram_utilizada_mb = Float64[]

#mide el tiempo de ejecucion para diferentes num de ciudades
for num_ciudades in 500:500:2000#se lee como: "comienza en 500, se le suma 500 hasta alcanzar los 2000"
    #println("num de ciudades:", num_ciudades)
    tiempo = @elapsed begin
        tsp(num_ciudades)
    end
    push!(tiempos_ejecucion, tiempo)
    ram = Base.summarysize(tsp(num_ciudades)) / (1024^2)
    push!(ram_utilizada_mb, ram)
end

#impresion de la lista con los datos resultantes
println("Tiempos de ejecución (segundos):")
for tiempo in tiempos_ejecucion
    @printf("%.6f\n", tiempo)
end

println("RAM utilizada (MB):", ram_utilizada_mb)

