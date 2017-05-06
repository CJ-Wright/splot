import sys  
sys.path.append('../splot')
from splot1Py3 import *

#### Load Data Set 1:
lc1 = "../data/examples/f2/sub_20161114-235343_Ag0_ct_180_2c77c1_0001.gr"
r1 = np.loadtxt(lc1, skiprows=27, usecols=(0,))
G1 = np.loadtxt(lc1, skiprows=27, usecols=(1,))

# Load Data Set 2:
lc2 = "../data/examples/f2/sub_20161115-002440_Ag100_ct_180_c73701_0001.gr"    
r2 = np.loadtxt(lc2, skiprows=27, usecols=(0,))
G2 = np.loadtxt(lc2, skiprows=27, usecols=(1,))

#Setup Data for the plot:
g1 = Data( (r1, G1), samplename ='G1', scan = 'Data', color = c[6], marker = '')
g2 = Data( (r2, G2), samplename ='G2', scan = 'Data', color = c[4], marker = '', line = "--")


# plot axis setup: only a sinlge plot
H = Splot()

# plot data
H.plotData(g1)    
H.plotData(g2, diff = True)    

#Add Title, label
H.title("G(r) Plot", math = "off")

#Save figure:
#H.save(name = "myfigure", form = "pdf")