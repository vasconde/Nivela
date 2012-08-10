# Classe para entrada e saida de dados

# pacote para calculo matricial
#import numpy

class IOData:
    
    def __init__ (self, obsFilePath, benchmarksFilePath):
        self.obs = []
        self.bmarks = []

        self.readObsFromFile(obsFilePath)
        self.readBenchmarksFile (benchmarksFilePath)


    def readObsFromFile (self, obsFilePath):
        file = open(obsFilePath)
        
        while 1:
            line = file.readline()
            if not line:
                break
            line_seg = line.split()
            self.obs.append(line_seg)

        # convert string to double
        for ob in self.obs:
            ob[2] = float(ob[2])
            ob[3] = float(ob[3])

    def readBenchmarksFile (self, benchmarksFilePath):

        file = open(benchmarksFilePath)
        
        while 1:
            line = file.readline()
            if not line:
                break
            line_seg = line.split()
            self.bmarks.append(line_seg)

        # convert string to double
        for bmark in self.bmarks:
            bmark[1] = float(bmark[1])
