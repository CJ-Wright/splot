import sys
sys.path.append('../RefacotringTest')
from RefactoringTest import *

#get the dataPaths:
dataPath1 = "data/examples/f1/80"
dataPath2 = "data/examples/f1/10"

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

# Setup Data for the plot: User can set line style
g1 = dataDict( (r1, Gtrunc1), samplename ='G1', scan = 'Orginal', color = c[1], marker = 'o', linestyle = ":")
g1diff = dataDict( (r1, Gdiff1), samplename = 'G1', scan = 'Diff', color = 'r', linestyle = "--")
g1calc = dataDict( (r1, Gcalc1), samplename  = 'G1', scan = 'Calc', color = c[0])

# Setup Data for the plot: user can use the group style sheet
g2 = dataDict( (r2, Gtrunc2), samplename ='G2', scan = 'Orginal', color = c[2], marker = 'o', linestyle = "--")
g2calc = dataDict( (r2, Gcalc2), samplename = 'G2', scan = 'Calc2', color = 'r')
g2diff = dataDict( (r2, Gdiff2), samplename = 'G2', scan = 'Diff', color = c[0])

# plot axis setup: here we have 2 rows x 1 col
H = Splot(2, 1)

# plot data
H.plotData(g1, 0, 0)
H.plotData(g1calc, 0, 0)
#Test the diffC() offset:
H.diffC(0,0, offset = 0)
H.plotData(g1diff, 0, 0, offsety = -4)

H.plotData(g2, 1, 0)
H.plotData(g2calc, 1, 0, diff = True)
#H.plotData(g2calc, 1, 0, diff = False)
H.plotData(g2diff, 1, 0, offsety = -6, legend = 'in')

H.figureSize(6, 8)
