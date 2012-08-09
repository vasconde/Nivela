# Classe para entrada e saida de dados

# pacote para calculo matricial
#import numpy

class IOData:
    
    def __init__ (self):
        self.obs = []

        self.readObsFromFile("./data/example1.txt")

        print(self.obs)

    def readObsFromFile (self, ObsFilePath):
        file = open(ObsFilePath)
        
        while 1:
            line = file.readline()
            if not line:
                break
            line_seg = line.split()
            self.obs.append(line_seg)
