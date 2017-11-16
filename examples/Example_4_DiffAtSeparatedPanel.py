from splot.splot import data_dict, Splot

#plot axis setup: 1 rows 2 columns
myplot = Splot(2,1)

r = [0, 20, 50, 80, 100]
for i in r:
    # load the data:
    dataPath = "data/4/"+str(i)
    G = data_dict(dataPath, samplename ='Ag', scan = str(i), 
                  marker = 'o', Linestyle='')

    # plot data: y offset is set to the number of the file name
    myplot.plot_data(**G, offsety = i, calc=True, diff = True, diffoffset=0)
    
    # plot diff data at the bottom panel: Turn down the Meas and Calc curve, 
    # Only turn on the diff by diff = True and meas = False.
    myplot.plot_data(**G, r=1, c=0, diff = True, meas = False, diffoffset=i/24)

myplot.config(legend='out')

# Show figure and save
myplot.show()
myplot.save(name='Example_4_DiffAtSeparatedPanel', form='pdf')