using Pkg
#Pkg.add("JuMP")
#Pkg.add("GLPK")
#Pkg.add("BenchmarkTools")
using JuMP
using GLPK
using Random
using BenchmarkTools

Random.seed!(2)
#funcion para resolver el problema y medir el tiempo
function resolver_tiempo(num_ciudades)
    num_conjuntos = 20  #cantidad de subconjuntos 
    
    N = 1:num_ciudades
    M = 1:num_conjuntos
    
    #costo asociado a cada conjunto 
    C = Dict(j => rand(1:10) for j in M)
    
    #matriz de asign binaria aleatoria 
    a = Dict((i, j) => rand(0:1) for i in N, j in M)
    
    #crear el modelo de opti
    model = Model(optimizer_with_attributes(GLPK.Optimizer, "msg_lev" => GLPK.GLP_MSG_OFF))
    
    #variables des binarias
    @variable(model, X[j = M], Bin)
    
    #func objetivo
    @objective(model, Min, sum(C[j] * X[j] for j in M))
    
    #restricciones de cobertura
    for i in N
        @constraint(model, sum(a[i, j] * X[j] for j in M) >= 1)
    end
    
    #resolver el problema y medir el tiempo
    tiempo = @elapsed optimize!(model)
    
    return tiempo, objective_value(model)
end

#vectores para almacenar los tiempos y costos min
tiempos = Float64[]
costos_minimos = Float64[]
ram_utilizada_mb = Float64[]

#ejecutar para diferentes valores de num_ciudades
for num_ciudades in 1000:1000:10000
    tiempo, costo_minimo = resolver_tiempo(num_ciudades)
    push!(tiempos, tiempo)
    push!(costos_minimos, costo_minimo)
    push!(ram_utilizada_mb, Base.summarysize((num_ciudades, resolver_tiempo(num_ciudades))) / (1024^2))
    println("Para $num_ciudades ciudades - Tiempo: $tiempo segundos - Costo mínimo: $costo_minimo")
end

#resultados finales
println("Tiempos: ", tiempos)
println("Costos mínimos: ", costos_minimos)
println("RAM utilizada (MB):", ram_utilizada_mb)
