from splot.splot import data_dict, Splot
import numpy as np

# plot axis setup: a single water fall plot
H = Splot()

r = [0, 20, 50, 80, 100]
for i in r:
    # load the data: only the measured and calculated data will be ploted in
    # this fugre, so we don't load the diff data.
    dataPath = "data/4/"+str(i)
    r = np.loadtxt(dataPath, skiprows = 4, usecols=(0,))
    gtrunc = np.loadtxt(dataPath, skiprows = 4, usecols=(1,))
    gcalc = np.loadtxt(dataPath, skiprows = 4, usecols=(3,))

    #Set up data
    G = data_dict((r, gtrunc),  samplename = "Measured", scan = '_'+str(i),
                  marker = 'o', linestyle = '')
    Gcalc = data_dict((r, gcalc),  samplename = "Calculated", scan = '_'+str(i),
                      color = 'r')

    #plot data: y offset is set to be same as the file name, no use of x offset. 
    H.plot_data(**G, offsety = i)
    #plot calculated curve at the same position, add an outside legend for
    # the figure
    H.plot_data(**Gcalc, offsety = i, legend = 'out')

# Show figure
H.show()
# Save
H.save(name = 'Example_4_MultipleMeasCalc', form = 'pdf')