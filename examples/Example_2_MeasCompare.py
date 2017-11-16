from splot.splot import data_dict, Splot, bgcolor

#get the data file Paths:
data1Path = "data/2/sub_20161114-235343_Ag0_ct_180_2c77c1_0001.gr"
data2Path = "data/2/sub_20161115-002440_Ag100_ct_180_c73701_0001.gr"

# Load the 2 Data sets, call them g1 and g2: use open marker for the Meas data
data_set1 = data_dict(data1Path, samplename ='Ag', scan = '0')
data_set2 = data_dict(data2Path, samplename ='Ag', scan = '100')

# plot axis setup: a sinlge panel plot
myplot = Splot()

# plot data at the sinlge panel, no need to write row and col numbers
myplot.plot_data(**data_set1)
myplot.plot_data(**data_set2)

#plot the difference between the two data sets at panel(r=0, c=0):
myplot.curves_diff(data_set1, data_set2)

# Figure configuration, the last step
myplot.config(context='manu')

# Show the figure and save
myplot.show()
myplot.save(name = 'Example_2_MeasCompare', form ='pdf')