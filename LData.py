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

# Classe para ajustamento parametrico linear

# pacote para calculo matricial
import numpy
import math

class LData:
    """Estrutura de dados do nivelamento"""

    def __init__ (self, obs, bmarks, distance = False, kilometer_error = []):

        self.obs = obs
        self.benchmarks = bmarks

        self.get_benchmarks_names()
        self.get_parameters_names() # depende da anterior
        self.ref_numbers () # depende da anterior

        self.gen_design_matrix ()
        self.gen_obs_matrix ()

        if distance:
            if kilometer_error == []:
                self.gen_Pl_matrix ()
            else:
                self.gen_Cl_matrix_from_dist (kilometer_error)
        else:
            self.gen_Cl_matrix ()


        

    # define lista com os nomes dos pontos fixos
    def get_benchmarks_names(self):

        self.benchmarks_names = []

        for ben in self.benchmarks:
            self.benchmarks_names.append(ben[0])

    # define lista com o nome dos parametros (pontos a determinar a altitude)
    # depende de get_benchmarks_names()
    def get_parameters_names (self):

        self.param_names = []

        for ob in self.obs:
            if not(self.param_names.__contains__(ob[0])) and not(self.benchmarks_names.__contains__(ob[0])):
                self.param_names.append(ob[0])
            if not(self.param_names.__contains__(ob[1])) and not(self.benchmarks_names.__contains__(ob[1])):
                self.param_names.append(ob[1])

    # define o numero de observacoes, pontos fixos e parametros
    # depende de get_parameters_names ()
    def ref_numbers (self):
        self.n_obs = len(self.obs)
        self.n_ben = len(self.benchmarks)
        self.n_param = len(self.param_names)

    # gera a matrix A
    # para cada observacao verifica e para cada from e to
    # verifica se nao eh ponto fixo e a seguir coloca -1 ou 1
    # consuante a posicao na lista de nomes dos param
    def gen_design_matrix (self):

        self.A = numpy.zeros((self.n_obs,self.n_param))

        i = 0
        for ob in self.obs:
            if not(self.benchmarks_names.__contains__(ob[0])):
                self.A[i,self.param_names.index(ob[0])] = -1
            if not(self.benchmarks_names.__contains__(ob[1])):
                self.A[i,self.param_names.index(ob[1])] = 1
            i += 1

    # gera a matrix de aobservacoes. A esta eh somada o valores dos pontos fixos que sao considerados de constantes
    def gen_obs_matrix (self):

        self.L = numpy.zeros((self.n_obs,1))

        i = 0
        for ob in self.obs:
            self.L[i,0] = ob[2]
            if self.benchmarks_names.__contains__(ob[0]):
                self.L[i,0] += self.benchmarks[self.benchmarks_names.index(ob[0])][1]
            if self.benchmarks_names.__contains__(ob[1]):
                self.L[i,0] -= self.benchmarks[self.benchmarks_names.index(ob[1])][1]
            i += 1


    # gera matriz de variancia e covariancia das observacoes
    # a partir das incertezas
    def gen_Cl_matrix (self):
        
        self.Cl = numpy.zeros((self.n_obs,self.n_obs))

        i = 0
        for ob in self.obs:
            self.Cl[i,i] = ob[3] * ob[3]
            i += 1

    # gera matriz de pesos das observacoes
    # a partir dos valores dados
    def gen_Pl_matrix (self):
        
        self.Pl = numpy.zeros((self.n_obs,self.n_obs))

        i = 0
        for ob in self.obs:
            self.Pl[i,i] = 1/ob[3]
            i += 1

    # gera matriz de variancia e covariancia das observacoes
    # a partir das distancias e erro kilometrico
    def gen_Cl_matrix_from_dist (self, eKm):
        
        self.Cl = numpy.zeros((self.n_obs,self.n_obs))

        i = 0
        for ob in self.obs:
            self.Cl[i,i] = math.pow(0.001 * eKm * math.sqrt(0.001 * ob[3]), 2);
            i += 1
            

#    ########## DATA EXAMPLE #############
#                  from | to | elev   | error
#        self.obs = [['A','B',10.509,0.006],
#                    ['B','C',5.36,0.004],
#                    ['C','D',-8.523,0.005],
#                    ['D','A',-7.348,0.003],
#                    ['B','D',-3.167,0.004],
#                    ['A','C',15.881,0.012]]
#        
#        self.benchmarks = [['A',437.596]]
