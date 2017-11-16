from splot.splot import data_dict, Splot

#get the data file Paths:
data1Path = "data/1/80"
data2Path = "data/1/10"

# Load the 2 Data sets, call them g1 and g2: use open marker for the Meas data
g1 = data_dict(data1Path, samplename ='G', scan='80', marker='o', linestyle='')
g2 = data_dict(data2Path, samplename ='G', scan='10', marker='o', linestyle='')

# plot axis setup: here we have 2 rows x 1 col
myplot = Splot(2, 1)

# plot data set 1: g1 at top panel, g2 at the bottom 
myplot.plot_data(**g1, r=0, c=0, calc = True, diff = True)
myplot.plot_data(**g2, r=1, c=0, calc = True, diff = True)

# Figure configuration is always the last step
# Use 'context = manu', so no legend shown. 
# Leave it blank, then the legends come back. 
#myplot.config(context='manu')
myplot.config()

# See the figure and save
myplot.show()
myplot.save(name = 'Example_1_TwoPanMeasCalcDiff', form ='pdf')