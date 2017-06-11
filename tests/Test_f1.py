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
#Gdiff2 = np.loadtxt(dataPath2, skiprows=4, usecols=(2,))
Gcalc2 = np.loadtxt(dataPath2, skiprows=4, usecols=(3,))

#Setup Data for the plot:
#g1 = data( (r1, Gtrunc1), samplename ='G1', scan = 'Orginal', color = c[0], marker = '+')
g1 = data( (r1, Gtrunc1), samplename ='G1', scan = 'Orginal', color = c[1], marker = 'o')
#g1calc = data( (r1, Gcalc1), samplename  = 'G1', scan = 'Calc', color = c[4], line='--', marker = "")
g1calc = data( (r1, Gcalc1), samplename  = 'G1', scan = 'Calc', color = 'r')
#g1diff = data2( (r1, Gdiff18), samplename = 'G1', scan = 'Diff', color = c[0])

g2 = data( (r2, Gtrunc2), samplename ='G2', scan = 'Orginal', color = c[2], marker = 'o')
g2calc = data( (r2, Gcalc2), samplename = 'G2', scan = 'Calc2', color = 'r')
#g2diff = data2( (r2, Gdiff2), samplename = 'G2', scan = 'Diff', color = c[0])

#Example of not reseting the marker / color / linestyle, unless the user wants to
g3 = data( (r1, Gtrunc1), samplename ='G3', scan = 'Orginal')
g1calc = data( (r1, Gcalc1), samplename  = 'G1', scan = 'Calc', color = 'r')

# plot axis setup: here we have 2 rows x 1 col
H = Splot(2,1)

# plot data
H.plotData(g1, 0, 0)
H.plotData(g1calc, 0, 0, diff = True)
#Test the diffC() offset = 0:
H.diffC(0,0, offset = 0)
H.plotData(g1diff, 0, 0, offsety = -6)

#g2 data uses default set from the group style sheet
H.plotData(g2, 1, 0)
H.plotData(g2calc, 1, 0, diff = True)
H.plotData(g2diff, 1, 0, offsety = -6, legend = 'in') # Add legend for all curves

#Adjust the plot to be taller and less wide
H.figureSize(6, 8)
#H.save(name = "myplot13", form = "pdf")

#Add Title, label
#H.title("G(r) Plot", math = "off")
#H.label(x = "hello", xunit = 'delta', y = 'world', yunit = 'epsilon', math = 'on')

#Save figure:
#H.save(name = "myfigure", form = "pdf")