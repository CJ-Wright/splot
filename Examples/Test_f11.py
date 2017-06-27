import sys
sys.path.append('../splot')
from splot1Py3 import *

# plot axis setup: a single water fall plot
H = Splot()
#mpl.rcParams['lines.linewidth'] = 2

for i in range (11):
    #load data:
    dataPath = "../data/examples/f11/"+str(i*10)
    r = np.loadtxt(dataPath, skiprows = 4, usecols=(0,))
    gtrunc = np.loadtxt(dataPath, skiprows = 4, usecols=(1,))

    #Set up data to be plot
    G = data((r, gtrunc),  samplename = "Gtrunc"+"_"+str(i*10), \
    scan = 'Data')

#plot data: x offset is 10 units right to the previous curve, y offset is 10 units above the previous
#    H.plotData(G, scal=1, offsetx = i*10, offsety = i*10,)
    H.plotData(G, scal=1, offsety = i*-0.5, legend  = 'in')

#Title is default to be empty, lable is default: G v.s r
#H.title("G(r) Plot", math = "off")
#H.save(name = "myfigure", form = "pdf")
plt.show()