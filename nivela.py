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

l = numpy.matrix([[448.105,5.360,-8.523,-444.944,-3.167,453.477]])
l = numpy.transpose(l)

l_e = numpy.matrix([[0.006**2,0.004**2,0.005**2,0.003**2,0.004**2,0.012**2]])
Cl = numpy.zeros((6,6)) 
numpy.fill_diagonal(Cl,l_e)

A = numpy.matrix([[1.0,0,0],[-1,1,0],[0,-1,1],[0,0,-1],[-1,0,1],[0,1,0]])

print(A)
print(Cl)
print(l)

a = Adjust.Adjust(l,Cl,False,A)

a.computation()

print("LData")

b = LData.LData()
