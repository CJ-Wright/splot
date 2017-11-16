from splot.splot import data_dict, Splot, bgcolor

#get the data file Paths:
data1Path = "data/1/80"
data2Path = "data/1/10"

# Load the 2 Data sets, call them g1 and g2: use open marker for the Meas data
g1 = data_dict(data1Path, samplename ='G', scan='80', marker='o', linestyle='')
g2 = data_dict(data2Path, samplename ='G', scan='10', marker='o', linestyle='')

# plot axis setup: 2 rows x 2 col
myplot = Splot(2, 2)

# plot data set 1 at upper left panel, plot data set 2 at lower left panel
myplot.plot_data(**g1, r=0, c=0, calc=True, diff=True)
myplot.plot_data(**g2, r=1, c=0, calc=True, diff=True)

# plot data set 1 with scale = 2.4. Plot at upper right panel
myplot.plot_data(**g1, r=0, c=1, scal = 2.4, calc=True, diff=True)

# plot data set 2 at lower right panel, with scale = 1.3
myplot.plot_data(**g2, r=1, c=1, scal = 1.3, calc=True, diff=True)

# Optional: addjust the plotting range at the first column: plot data from 0-30
myplot.set_xlim(0, 0, 35)
# Optional: addjust the plotting range at the second column: from 1-24
myplot.set_xlim(1, 1.5, 24)

# Figure configuration is always the last step 
# No specifying in context, so the legends come back.
myplot.config(context='manu')

# See the figure / Save the figure
myplot.show()
myplot.save(name = 'Example_1_MutipanMeasCalcDiff', form ='pdf')