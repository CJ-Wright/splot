from splot.splot import data_dict, Splot, c
import numpy as np

# plot axis setup: a single water fall plot
H = Splot()
#mpl.rcParams['lines.linewidth'] = 2

for i in range (11):
    #load data:
    dataPath = "data/3/"+str(i*10)
    r = np.loadtxt(dataPath, skiprows = 4, usecols=(0,))
    gtrunc = np.loadtxt(dataPath, skiprows = 4, usecols=(1,))

    #Set up data to be plot
    G = data_dict((r, gtrunc),  samplename = "Gtrunc"+"_"+str(i*10), 
    scan = 'Data')
    
    #plot data: y offset is 0.5 unit below to the above curve 
    H.plot_data(**G, scal=1, offsety = i*-0.5, legend  = 'in')

#H.title("G(r) Plot", math = "off")
#H.save(name = "myfigure", form = "pdf")
# See the figure
H.show()