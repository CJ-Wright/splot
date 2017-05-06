import sys  
sys.path.append('../splot')
from splot1Py3 import *

# plot axis setup: a single water fall plot 
H = Splot()
r = [0, 20, 50, 80, 100]
for i in r:
    lc = "../data/examples/f27/"+str(i)
    r = np.loadtxt(lc, skiprows = 4, usecols=(0,))
    gtrunc = np.loadtxt(lc, skiprows = 4, usecols=(1,))
#    gdiff = np.loadtxt(lc, skiprows = 4, usecols=(2,))    #will not be plotted 
    gcalc = np.loadtxt(lc, skiprows = 4, usecols=(3,))    
    
    #Set up data
    G = Data((r, gtrunc),  samplename = "Gtrunc"+"_"+str(i), \
                scan = 'Data', color = c[i/10], marker = '', line = '-')
    Gcalc = Data((r, gtrunc),  samplename = "Gtrunc"+"_"+str(i), \
                scan = 'Calculated', color = c[i/10+2], marker = '', line = ':')

    #plot data: y offset is set to be same as the file name, x offset is -1. 
    H.plotData(G, offsetx = -1, offsety = i)
    #plot calculated curve at the same position 
    H.plotData(Gcalc, offsetx = -1, offsety = i,)