from splot.splot import data_dict, Splot
import numpy as np

#get the dataPaths:
dataPath1 = "data/1/80"
dataPath2 = "data/1/10"

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
g1 = data_dict( (r1, Gtrunc1), samplename ='G1', scan = 'Measured')
g1calc = data_dict( (r1, Gcalc1), samplename  = 'G1', scan = 'Calc', \
                    color = 'r')
g1diff = data_dict( (r1, Gdiff1), samplename = 'G1', scan = 'Diff', \
                    color = 'g')

# Setup Data for the plot: user can use the group style sheet
g2 = data_dict( (r2, Gtrunc2), samplename ='G2', scan = 'Measured')
g2calc = data_dict( (r2, Gcalc2), samplename = 'G2', scan = 'Calc', color = 'r')
g2diff = data_dict( (r2, Gdiff2), samplename = 'G2', scan = 'Diff')

# plot axis setup: here we have 2 rows x 1 col
H = Splot(2, 1)

# plot data set 1 at top panel, plot diff curve from the data set
H.plot_data(**g1, r=0, c=0)
H.plot_data(**g1calc, r=0, c=0)
H.plot_data(**g1diff, r=0, c=0, offsety = -4) # shift the diff curve manually

# plot data set 2 at bottom pane, the diff curve is generated by splot
H.plot_data(**g2, r=1, c=0)
# add legend for all curves in the last step
H.plot_data(**g2calc, r=1, c=0, diff = True, legend = 'in')

# See the figure
H.show()

# Save figure
H.save(name = 'Example_1_MeasCalcDiff', form ='pdf')