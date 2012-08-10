#  _   _ _           _                              
# | \ | (_)         | |           /\                
# |  \| |___   _____| | __ _     /  \   _ __  _ __  
# | . ` | \ \ / / _ \ |/ _` |   / /\ \ | '_ \| '_ \ 
# | |\  | |\ V /  __/ | (_| |  / ____ \| |_) | |_) |
# |_| \_|_| \_/ \___|_|\__,_| /_/    \_\ .__/| .__/ 
#                                      | |   | |    
#                                      |_|   |_|
# Leveling computation and adjustment
#
# Author: Vasco Conde (vasconde)

# Nivela Modules
import IOData
import LData
import Adjust

# Others Modules
import numpy

print("*** Nivela ***")

# recolhe os dados de um ficheiro
idados = IOData.IOData("./data/obs2.txt","./data/bmarks1.txt")

# cria a estrutura de dados para o ajustamento
#dados = LData.LData(idados.obs,idados.bmarks)

dados = LData.LData(idados.obs,idados.bmarks,True,8.0)

# ajustamento dos dados
aj = Adjust.Adjust(numpy.asmatrix(dados.L),numpy.asmatrix(dados.Cl),False,numpy.asmatrix(dados.A))
aj.computation()


# resultados
print("Parametros:")
print (aj.x)
print("Residuos:")        
print (aj.v)
print("var aposteriori:")
print (aj.var_)
