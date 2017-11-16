from splot.splot import data_dict, Splot, bgcolor

# plot axis setup: a single water fall plot
myplot = Splot()

for i in range (11):
    #load data: only the measured data will be plotted in this example,
    dataPath = "data/3/"+str(i*10)
    G = data_dict(dataPath, samplename ='Ag', scan = str(i*10))
    
    #plot data: y offset is 0.5 unit below to the above curve 
    myplot.plot_data(**G, scal=1, offsety = i*-1)

# Always configure the plot at the last step 
# Optional: add a title and change the label (the configuration here is ugly 
#                                    just for the purpose of showing an example)
# myplot.config(title="G(r) Plot", title_math = False,
#              x='r', xunit='nm', y='G', yunit='nm^(-2)', label_math=False)
myplot.config(context='manu')

# See the figure
myplot.show()
# Save figure
myplot.save(name = "Example_3_WaterfallMeas", form = "pdf")