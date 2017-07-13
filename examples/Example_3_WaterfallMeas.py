from splot.splot import data_dict, Splot
import numpy as np

# plot axis setup: a single water fall plot
H = Splot()

for i in range (11):
    #load data: only the measured data will be plotted in this example,
    # so we don't load the Calculated or Diff curve data here.
    dataPath = "data/3/"+str(i*10)
    r = np.loadtxt(dataPath, skiprows = 4, usecols=(0,))
    gtrunc = np.loadtxt(dataPath, skiprows = 4, usecols=(1,))

    #Set up data to be plot
    G = data_dict((r, gtrunc),  samplename = "Measured", scan = "_"+str(i*10))
    
    #plot data: y offset is 0.5 unit below to the above curve 
    H.plot_data(**G, scal=1, offsety = i*-0.5, legend  = 'in')

#H.title("G(r) Plot", math = "off")
# See the figure
H.show()
# Save figure
H.save(name = "Example_3_WaterfallMeas", form = "pdf")
