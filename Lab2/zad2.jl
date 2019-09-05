import Pkg
# Pkg.add("DataFrames")
# Pkg.add("CSV")
# Pkg.add("Plots")
# Pkg.add("StatsBase")
using DataFrames
using CSV
using Plots
using StatsBase
df1 = DataFrame()
input = "csv.csv"
df1 = CSV.read(input, delim = ","; datarow=1, transpose=true)
#show(describe(df1))
var(df1[:N1V25000000])
