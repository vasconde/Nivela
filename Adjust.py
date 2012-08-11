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

class Adjust:
    """Ajustamento por minimos quadrados
    para modelo parametrico linear"""

    # construtor
    def __init__ (self, l = numpy.matrix([]), WorCl = numpy.matrix([]), isW = False, A = numpy.matrix([])):
        """Args:
        l - observations matrix [n x 1]
        WorCl - weight matrix (W) or var and covar of obs (Cl) [n x n]
        isW - WorCl is W?
        A - design matrix [n x n_par]"""
        self.l = l      # matriz de obsevacoes
        self.A = A      # design matrix
        self.var = 1.0  # variancia de referencia apriori
        self.var_ = 1.0 # variancia de referencia aposteriori
        self.df = self.A.shape[0] - self.A.shape[1] # degrees of freedom       
        
        self.W = numpy.matrix([])
        self.Cl = numpy.matrix([])

        if isW:
            self.W = WorCl
        else:
            self.Cl = WorCl
            self.W = self.weights() 

    # retorna os pesos em funcao de Cl e var
    def weights(self):
        return self.var * numpy.linalg.inv(self.Cl)
        
    # calculo do ajustamento
    def computation (self):
        # a = numpy.matrix([[1., 2.], [3., 4.]])
        # inv_a = numpy.linalg.inv(a)
        # a_t = numpy.transpose(a)

        A_t = numpy.transpose(self.A)
        
        N_inv = numpy.linalg.inv(A_t * self.W * self.A)
        
        self.x = N_inv * A_t * self.W * self.l

        self.v = self.A * self.x - self.l

        self.l_ = self.l + self.v

        self.Cx_ = self.var * N_inv

        self.var_ = (numpy.transpose(self.v) * self.W * self.v)/self.df
        self.var_ = self.var_[0,0]
        
        self.C_x_ = self.var_ * N_inv
