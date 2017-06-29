import sys  
sys.path.append('../splot')
from splot import *

# plot axis setup: a single water fall plot
H = Splot()

r = [0, 20, 50, 80, 100]
for i in r:
    dataPath = "../data/examples/f27/"+str(i)
    r = np.loadtxt(dataPath, skiprows = 4, usecols=(0,))
    gtrunc = np.loadtxt(dataPath, skiprows = 4, usecols=(1,))
    
    #The diff curve will not be plotted
#    gdiff = np.loadtxt(dataPath, skiprows = 4, usecols=(2,))    
    
    gcalc = np.loadtxt(dataPath, skiprows = 4, usecols=(3,))

    #Set up data
    G = data_dict((r, gtrunc),  samplename = "Gtrunc"+"_"+str(i), \
                scan = 'Data', marker = 'o', linestyle = '')
    Gcalc = data_dict((r, gtrunc),  samplename = "Gtrunc"+"_"+str(i), \
                scan = 'Calculated')

    #plot data: y offset is set to be same as the file name, no use of x offset. 
    H.plot_data(**G, offsety = i)
    #plot calculated curve at the same position
    H.plot_data(**Gcalc, offsety = i, legend = 'out')

# Resize the figure aspec ratio
H.figure_size(6, 8)