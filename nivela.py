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
import LData
import Adjust

# Others Modules
import numpy

print("*** Nivela ***")


dados = LData.LData()

aj = Adjust.Adjust(numpy.asmatrix(dados.L),numpy.asmatrix(dados.Cl),False,numpy.asmatrix(dados.A))
aj.computation()


print("Parametros:")
print (aj.x)
print("Residuos:")        
print (aj.v)
print("var aposteriori:")
print (aj.var_)
