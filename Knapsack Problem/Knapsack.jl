using Pkg
#Pkg.add("JuMP")
#Pkg.add("GLPK")
#Pkg.add("BenchmarkTools")
using JuMP
using GLPK
using Printf
using BenchmarkTools

#esta funcion resuelve el problema Knapsack y devuelve el tiempo de ejecucion
function resolver_knapsack(num_elementos)
    PESOMAX = 100
    VALOR = Dict(i => rand(1:20) for i in 1:num_elementos)
    PESO = Dict(i => rand(1:10) for i in 1:num_elementos)
    ELEMENTOS = 1:num_elementos

    model = Model(optimizer_with_attributes(GLPK.Optimizer))
    @variable(model, take[ELEMENTOS], binary=true)
    @objective(model, Max, sum(VALOR[i] * take[i] for i in ELEMENTOS))
    @constraint(model, sum(PESO[i] * take[i] for i in ELEMENTOS) <= PESOMAX)

    time = @elapsed optimize!(model)
    return time
end

#almacena los tiempos para diferentes numeros de elementos
tiempos = Dict()
ram_utilizada_mb = Float64[]

for num_elementos in 10000:10000:100000
    tiempo_ejecucion = resolver_knapsack(num_elementos)
    tiempos[num_elementos] = tiempo_ejecucion

    #medir la RAM utilizada
    ram = Base.summarysize(resolver_knapsack(num_elementos)) / (1024^2)
    push!(ram_utilizada_mb, ram)
end

#imprime los tiempos almacenados
for (num_elementos, tiempo) in tiempos
    
    println("Elementos: $num_elementos - Tiempo: $tiempo segundos")
end

println("RAM utilizada (MB):", ram_utilizada_mb)