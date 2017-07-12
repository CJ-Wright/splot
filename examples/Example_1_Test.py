from splot import data_dict, Splot, c
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
g1 = data_dict( (r1, Gtrunc1), samplename ='G1', scan = 'Orginal', color = c[8], marker = 'o', linestyle = ":")
#g1 = data_dict( (r1, Gtrunc1), samplename ='G1', scan = 'Orginal')

g1diff = data_dict( (r1, Gdiff1), samplename = 'G1', scan = 'Diff', color = 'r', linestyle = "--")
g1calc = data_dict( (r1, Gcalc1), samplename  = 'G1', scan = 'Calc')

# Setup Data for the plot: user can use the group style sheet
g2 = data_dict( (r2, Gtrunc2), samplename ='G2', scan = 'Orginal', color = 'r', marker = 'o', linestyle = "--")
g2calc = data_dict( (r2, Gcalc2), samplename = 'G2', scan = 'Calc2', linestyle = "--")
g2diff = data_dict( (r2, Gdiff2), samplename = 'G2', scan = 'Diff', color = c[0], linestyle = "-")

# plot axis setup: here we have 2 rows x 1 col
H = Splot(2, 1)

# plot data
H.plot_data(**g1, r=0, c=0)
H.plot_data(**g1calc, r=0, c=0, diff = True)
#Test the diffC() offset:
H.diff_c(0,0, offset = 0)
H.plot_data(**g1diff, r=0, c=0, offsety = -4)

H.plot_data(**g2, r=1, c=0)
H.plot_data(**g2calc, r=1, c=0, diff = True, legend='in')
H.diff_c(r=1,c=0, offset = 0)
H.plot_data(**g2diff, r=1, c=0, offsety = -6, legend = 'in')

#change the figure aspect ratio:
H.figure_size(6, 8)

H.show()