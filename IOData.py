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
