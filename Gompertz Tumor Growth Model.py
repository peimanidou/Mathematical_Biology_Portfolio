import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Initial Conditions
y0=[0.5] # Initial volume of the tumor with unit x^3 
t=np.linspace(0,3000,1000) # Tumor volume is measured over a time period of 300 arbitrary units with 1000 time points 

# Parameters we are using in the Gompertz Model

r=0.01 # Intrinsic tumor growth rate
K = 10000 # Carrying capacity of the tumors volume

Parameters= (r,K) # We are putting the parameters in a tuple to pass them to the function

def gompertz_model(variables,t,Parameters):

    V = variables[0] # We define the first variable V which is th volume of the tumor at each time point t
    r = Parameters[0] # We assign the intrinsic growth rate of the tumor as the first parameter of the function
    K = Parameters[1] # We assign the carrying capacity of the tumor as the second parameter of the function

    dVdt = r*V*np.log(K/V) # We define the function that describes the growth of the tumor volume over time, given certain parameters

    return([dVdt]) # We return the value of the ODE at every time point t

Volume=odeint(gompertz_model,y0,t,args=(Parameters,)) # We use the odeint function to find the solution of the ODE that describes the growth of the tumors volume over time

# Finally, we plot the results of the model to visualize the growth of the tumor that we have worked on over time 

plt.plot(t,Volume[:,0],color='orange',linewidth=1.5,label=' Gompertz Tumor Growth Model')
plt.title('Gompertz Tumor Growth Model',fontsize=15,fontweight='bold',color='brown')
plt.xlabel('Time (in arbitrary units)',fontsize=10,color='brown')
plt.ylabel('Volume of Tumor', fontsize=10,color='brown')
plt.grid(alpha=0.5)
plt.legend()
plt.savefig("gompertz_tumor_growth_model.jpg", dpi=150)
plt.show()
