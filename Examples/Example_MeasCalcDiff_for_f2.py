import sys  
sys.path.append('../splot')
from splot import *

#### Load Data Set 1:
dataPath1 = "examples_data/f2/sub_20161114-235343_Ag0_ct_180_2c77c1_0001.gr"
r1 = np.loadtxt(dataPath1, skiprows=27, usecols=(0,))
G1 = np.loadtxt(dataPath1, skiprows=27, usecols=(1,))
# Load Data Set 2:
dataPath2 = "examples_data/f2/sub_20161115-002440_Ag100_ct_180_c73701_0001.gr"    
r2 = np.loadtxt(dataPath2, skiprows=27, usecols=(0,))
G2 = np.loadtxt(dataPath2, skiprows=27, usecols=(1,))

#Setup Data for the plot:
data_set1 = data_dict( (r1, G1), samplename ='G1', scan = 'Data')
data_set2 = data_dict( (r2, G2), samplename ='G2', scan = 'Data', 
                      linestyle = '', marker = 'o')

# plot axis setup: a sinlge plot
H = Splot()

# plot data
H.plot_data(**data_set1)
H.plot_data(**data_set2, legend = 'in', diff = True)
