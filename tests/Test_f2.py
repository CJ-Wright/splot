import sys  
sys.path.append('../splot')
from splot1Py3 import *

#### Load Data Set 1:
dataPath1 = "../data/examples/f2/sub_20161114-235343_Ag0_ct_180_2c77c1_0001.gr"
r1 = np.loadtxt(dataPath1, skiprows=27, usecols=(0,))
G1 = np.loadtxt(dataPath1, skiprows=27, usecols=(1,))

# Load Data Set 2:
dataPath2 = "../data/examples/f2/sub_20161115-002440_Ag100_ct_180_c73701_0001.gr"    
r2 = np.loadtxt(dataPath2, skiprows=27, usecols=(0,))
G2 = np.loadtxt(dataPath2, skiprows=27, usecols=(1,))

#Setup Data for the plot:
g1 = Data( (r1, G1), samplename ='G1', scan = 'Data')
g2 = Data( (r2, G2), samplename ='G2', scan = 'Data')

# plot axis setup: only a sinlge plot
H = Splot()

# plot data
H.plotData(g1)
#H.setLine(g2, color = c[4], marker = '')
H.plotData(g2)
H.diffC() #Same as H.diffC(0,0) since there is only one plot