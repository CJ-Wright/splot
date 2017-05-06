import sys  
sys.path.append('../splot')
from splot1Py3 import *

# plot axis setup: a single water fall plot 
H = Splot()

for i in range (11):
    #load data:
    lc = "../data/examples/f11/"+str(i*10)
    r = np.loadtxt(lc, skiprows = 4, usecols=(0,))
    gtrunc = np.loadtxt(lc, skiprows = 4, usecols=(1,))
    
    #Set up data to be plot: every curve is shiftted down by 5 units
    G = Data((r, gtrunc),  samplename = "Gtrunc"+"_"+str(i*10), \
    scan = 'Data', color = c[i], marker = '')
    
#plot data: x offset is 10 units right to the previous curve, y offset is 10 units above the previous 
    H.plotData(G, scal=1, offsetx = i*10, offsety = i*10,)
    
#Title is default to be empty, lable is default: G v.s r 
#H.title("G(r) Plot", math = "off")