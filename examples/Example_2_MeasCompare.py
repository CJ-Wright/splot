from splot.splot import data_dict, Splot, c
import numpy as np

# Load Data Set 1:
dataPath1 = "data/2/sub_20161114-235343_Ag0_ct_180_2c77c1_0001.gr"
r1 = np.loadtxt(dataPath1, skiprows=27, usecols=(0,))
G1 = np.loadtxt(dataPath1, skiprows=27, usecols=(1,))

# Load Data Set 2:
dataPath2 = "data/2/sub_20161115-002440_Ag100_ct_180_c73701_0001.gr"    
r2 = np.loadtxt(dataPath2, skiprows=27, usecols=(0,))
G2 = np.loadtxt(dataPath2, skiprows=27, usecols=(1,))

#Setup Data for the plot:
data_set1 = data_dict( (r1, G1), samplename ='Ag', scan = '0',
                       color = 'C4')
data_set2 = data_dict( (r2, G2), samplename ='Ag', scan = '100',
                       color = 'C6')

# plot axis setup: a sinlge plot
myplot = Splot()

# plot data, add legend in last plotting statemen
myplot.plot_data(**data_set1)
myplot.plot_data(**data_set2, diff = True, legend ='in')

# Show the figure
#myplot.show()

# Save figure
myplot.save(name = 'Example_2_MeasCompare', form ='pdf')