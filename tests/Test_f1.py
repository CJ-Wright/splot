import sys  
sys.path.append('../splot')
from splot1Py3 import *

#### Load Data Set 1:
r1 = np.loadtxt("../data/examples/f1/80", skiprows=4, usecols=(0,))
Gtrunc1 = np.loadtxt("../data/examples/f1/80", skiprows=4, usecols=(1,))
Gdiff1 = np.loadtxt("../data/examples/f1/80", skiprows=4, usecols=(2,))
Gcalc1 = np.loadtxt("../data/examples/f1/80", skiprows=4, usecols=(3,))

# Load Data Set 2:
"../data/examples/f1/10"
r2 = np.loadtxt("../data/examples/f1/10", skiprows=4, usecols=(0,))
Gtrunc2 = np.loadtxt("../data/examples/f1/10", skiprows=4, usecols=(1,))
Gdiff2 = np.loadtxt("../data/examples/f1/10", skiprows=4, usecols=(2,))
Gcalc2 = np.loadtxt("../data/examples/f1/10", skiprows=4, usecols=(3,))

#Setup Data for the plot:
#g1 = Data( (r1, Gtrunc1), samplename ='G1', scan = 'Orginal', color = c[0], marker = '+')
g1 = Data2( (r1, Gtrunc1), samplename ='G1', scan = 'Orginal', color = c[1])
#g1calc = Data( (r1, Gcalc1), samplename  = 'G1', scan = 'Calc', color = c[4], line='--', marker = "")
g1calc = Data2( (r1, Gcalc1), samplename  = 'G1', scan = 'Calc', color = 'r')
g1diff = Data2( (r1, Gdiff1-8), samplename = 'G1', scan = 'Diff', color = c[0])

g2 = Data2( (r2, Gtrunc2), samplename ='G2', scan = 'Orginal', color = c[2])
g2calc = Data2( (r2, Gcalc2), samplename = 'G2', scan = 'Calc2', color = 'r')
g2diff = Data2( (r2, Gdiff2-8), samplename = 'G2', scan = 'Diff', color = c[0])

#Example of not reseting the marker / color / linestyle, unless the user wants to
g1 = Data2( (r1, Gtrunc1), samplename ='G1', scan = 'Orginal')
#g1 = Data( (r1, Gtrunc1), samplename ='G1', scan = 'Orginal', color = c[0], marker = '+')
g1diff = Data2( (r1, Gdiff1-8), samplename = 'G1', scan = 'Diff')
#g1diff = Data( (r1, Gdiff1-8), samplename = 'G1', scan = 'Diff', color = c[0])
g1calc = Data2( (r1, Gcalc1), samplename  = 'G1', scan = 'Calc', color = 'r')
#g1calc = Data( (r1, Gcalc1), samplename  = 'G1', scan = 'Calc', color = c[4], line='--', marker = "")
#g1calc = Data( (r1, Gcalc1), samplename  = 'G1', scan = 'Calc', color = c[4])

# plot axis setup: here we have 2 rows x 1 col
H = Splot(2,1)

# plot data
H.plotData(g1, 0, 0)    
H.plotData(g1calc, 0, 0, diff = True)
#H.plotData(g1diff, 0, 0)

H.plotData(g2, 1, 0)
H.plotData(g2calc, 1, 0, diff = True)
#H.plotData(g2diff, 1, 0)

#Add Title, label
#H.title("G(r) Plot", math = "off")
#H.label(x = "hello", xunit = 'delta', y = 'world', yunit = 'epsilon', math = 'on')

#Save figure:
H.save(name = "myfigure", form = "pdf")