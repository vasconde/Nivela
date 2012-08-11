#  _   _ _           _                              
# | \ | (_)         | |           /\                
# |  \| |___   _____| | __ _     /  \   _ __  _ __  
# | . ` | \ \ / / _ \ |/ _` |   / /\ \ | '_ \| '_ \ 
# | |\  | |\ V /  __/ | (_| |  / ____ \| |_) | |_) |
# |_| \_|_| \_/ \___|_|\__,_| /_/    \_\ .__/| .__/ 
#                                      | |   | |    
#                                      |_|   |_|

#  Nivela -- Leveling computation and adjustment
#  Copyright (C) 2012  Vasco Conde <vasconde@gmail.com>
#
#  This file is part of the Nivela.
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA	

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
