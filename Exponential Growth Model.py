import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Initial Conditions
y0=[4] # we begin with 4 tumor cells assuming we are in the early stages of tumor growth
t=np.linspace(0,500,num=1500) # tumor cells' growth being shown over 500 time units, with 1500 interim points

# Parameters we are using in the model

r=0.2 # proliferation rate of tumor cells (1/unit time)

parameters=[r] 

def expmodel(variables,t,parameters):
    P = variables[0] # we define the variable P which is the population of tumor cells at each time point t
    r= parameters[0] # we assign the growth rate of tumor cells as the parameter of the function
    dPdt = r*P # we define the ODE that describes the growth of tumor cells over time, resources are assumed to be unlimited
    return([dPdt]) # we return the value of the ODE at every time point t

population=odeint(expmodel,y0,t,args=(parameters,)) 

# We continue by plotting the results of the model to visualize the growth of the tumor cells at this early stage of tumor growth
plt.plot(t,population[:,0],color='blue',linewidth=3)
plt.title('Tumor Cell Exponential Growth Model',fontsize=20,fontweight='bold',color='steelblue')
plt.xlabel('Time (in arbitrary units)',fontsize=10,color='blue')
plt.ylabel('Population of Tumor Cells', fontsize=10,color='blue')
plt.grid(alpha=0.5)
plt.savefig("exponential_growth_of_tumor_cells.png", dpi=150)
plt.show()