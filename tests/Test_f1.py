import sys  
sys.path.append('../splot')
from splot1 import *

# Load Data Set 1:
r1 = np.loadtxt("../data/examples/f1/80", skiprows=4, usecols=(0,))
Gtrunc1 = np.loadtxt("../data/examples/f1/80", skiprows=4, usecols=(1,))
Gdiff1 = np.loadtxt("../data/examples/f1/80", skiprows=4, usecols=(2,))
Gcalc1 = np.loadtxt("../data/examples/f1/80", skiprows=4, usecols=(3,))

# Load Data Set 2:
r2 = np.loadtxt("../data/examples/f1/10", skiprows=4, usecols=(0,))
Gtrunc2 = np.loadtxt("../data/examples/f1/10", skiprows=4, usecols=(1,))
Gdiff2 = np.loadtxt("../data/examples/f1/10", skiprows=4, usecols=(2,))
Gcalc2 = np.loadtxt("../data/examples/f1/10", skiprows=4, usecols=(3,))

#Setup Data for the plot:
g1 = Data( (r1, Gtrunc1), samplename ='G1', scan = 'Orginal', color = c[0], marker = '+')
g1calc = Data( (r1, Gcalc1), samplename  = 'G1', scan = 'Calc', color = c[4], line='--', marker = "")
g1diff = Data( (r1, Gdiff1-8), samplename = 'G1', scan = 'Diff', color = 'r', marker = "")

g2 = Data( (r2, Gtrunc2), samplename ='G2', scan = 'Orginal', color = c[1], marker = "o")
g2calc = Data( (r2, Gcalc2), samplename = 'G2', scan = 'Calc2', color = c[3], line='--', marker = "")
g2diff = Data( (r2, Gdiff2-8), samplename = 'G2', scan = 'Diff', color = 'r', marker = "")

# plot axis setup: 2 rows x 1 col
H = Splot(2,1)

# plot data 
H.plotData(g1, 0, 0)    
H.plotData(g1calc, 0, 0, diff = True)
H.plotData(g1diff, 0, 0)

H.plotData(g2, 1, 0)
H.plotData(g2calc, 1, 0, diff = True)
H.plotData(g2diff, 1, 0)

#Add Title, label
H.title("G(r) Plot", math = 'on')
H.label(x = "hello", xunit = 'delta', y = 'world', yunit = 'epsilon', math = 'on')

#Save figure:
#H.save(name = "myfigure", form = "pdf")
plt.show()