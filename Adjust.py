# Classe para ajustamento parametrico linear

# pacote para calculo matricial
import numpy

class Adjust:
    """Ajustamento por minimos quadrados
    para modelo parametrico linear"""

    # construtor
    def __init__ (self, l = numpy.matrix([]), Cl = numpy.matrix([]), A = numpy.matrix([])):
        self.l = l      # matriz de obsevacoes
        self.Cl = Cl    # v&c das observacoes
        self.A = A      # design matrix
        self.var = 1.0  # variancia de referencia apriori
        self.var_ = 1.0 # variancia de referencia aposteriori
        self.df = 3.0
        
        self.Pl = self.weights() 

    # retorna os pesos em funcao de Cl e var
    def weights(self):
        return self.var * numpy.linalg.inv(self.Cl)
        
    # calculo do ajustamento
    def computation (self):
        # a = numpy.matrix([[1., 2.], [3., 4.]])
        # inv_a = numpy.linalg.inv(a)
        # a_t = numpy.transpose(a)

        A_t = numpy.transpose(self.A)
        
        N_inv = numpy.linalg.inv(A_t * self.Pl * self.A)
        
        self.x = N_inv * A_t * self.Pl * self.l

        self.v = self.A * self.x - self.l

        self.l_ = self.l + self.v

        self.Cx_ = self.var * N_inv

        self.var_ = (numpy.transpose(self.v) * self.Pl * self.v)/self.df
        self.var_ = self.var_[0,0]
        
        self.C_x_ = self.var_ * N_inv

        print("*************")
        print (self.x)
        print("*************")        
        print (self.v)

        print (self.var_)