#!/Users/Shuyue/mc/envs/py27/bin/python
import sys  
sys.path.append('../splot')
from splot1Py3 import *

#get the dataPaths:
dataPath1 = "../data/examples/f1/80"
dataPath2 = "../data/examples/f1/10"

#### Load Data Set 1:
r1 = np.loadtxt(dataPath1, skiprows=4, usecols=(0,))
Gtrunc1 = np.loadtxt(dataPath1, skiprows=4, usecols=(1,))
Gdiff1 = np.loadtxt(dataPath1, skiprows=4, usecols=(2,))
Gcalc1 = np.loadtxt(dataPath1, skiprows=4, usecols=(3,))

# Load Data Set 2:
r2 = np.loadtxt(dataPath2, skiprows=4, usecols=(0,))
Gtrunc2 = np.loadtxt(dataPath2, skiprows=4, usecols=(1,))
Gdiff2 = np.loadtxt(dataPath2, skiprows=4, usecols=(2,))
Gcalc2 = np.loadtxt(dataPath2, skiprows=4, usecols=(3,))

#Setup Data for the plot: User can set line style
g1 = Data( (r1, Gtrunc1), samplename ='G1', scan = 'Orginal', line='', \
		marker = 'o')
g1diff = Data( (r1, Gdiff1-8), samplename = 'G1', scan = 'Diff')
g1calc = Data( (r1, Gcalc1), samplename  = 'G1', scan = 'Calc', color = c[8])

#Setup Data for the plot: user can use the group style sheet
g2 = Data( (r2, Gtrunc2), samplename ='G2', scan = 'Orginal')
g2calc = Data( (r2, Gcalc2), samplename = 'G2', scan = 'Calc2')
g2diff = Data( (r2, Gdiff2-8), samplename = 'G2', scan = 'Diff')

# plot axis setup: here we have 2 rows x 1 col
H = Splot(2,1)

# plot data
H.plotData(g1, 0, 0)    
H.plotData(g1calc, 0, 0, diff = True)
H.plotData(g1diff, 0, 0)

#g2 data uses default set from the group style sheet 
H.plotData(g2, 1, 0)
H.plotData(g2calc, 1, 0, diff = True)
H.plotData(g2diff, 1, 0)

#Add Title, label
H.title("G(r) Plot", math = "off")
#H.label(x = "hello", xunit = 'delta', y = 'world', yunit = 'epsilon', math = 'on')

#Save figure:
#H.save(name = "myfigure", form = "pdf")