import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

#Initial conditions
V0=[225] #The initial volume of the tumor  we simulate in mm^3
t=np.linspace(0,600,800) #Time vector in days

#Parameters we are using for the Bertalanffy-Pütter differential equation
a=2/3 #Describing the inflow of nutrients/energy to the tumor
b=1 #Describing the energy needed for the tumor to sustain itself
p=0.1 #Describing the multiplicative rate of the tumor cell population growth
q=0.01 #Describing the rate of tumor cell death

Parameters=(a,b,p,q) #We choose to put the parameters in a tuple to pass them easily to the function

def von_bertalanffy_model(variables,t,Parameters):
    V=variables[0] #We define the first variable V which is the volume of the tumor at each time point t
    a=Parameters[0] #We assign the inflow of energy to the tumor as the first parameter of the model
    b=Parameters[1] #We assign the energy needed for the tumor to sustain itself as the second parameter of the model
    p=Parameters[2] #We assign the proliferation rate of the tumor cell population as the third parameter of the model
    q=Parameters[3] #We assign the rate of tumor cell death as the fourth and final parameter of the model

    dVdt = p*V**a - q*V**b #We define the von Bertalanffy-Pϋtter differential equation that describes the growth of the tumor volume over time, given certain parameters

    return([dVdt]) #We return the value of the ODE at every time point t 

Volume=odeint(von_bertalanffy_model,V0,t,args=(Parameters,)) #We use the odeint function to find the solution of the ODE that describes the growth of the tumor we haveworked on over time

#We then plot the results of the model in order to have a visual representation of the growth of the tumor over time

plt.plot(t,Volume[:,0],color='green',linewidth=1.7,label='von Bertalanffy Tumor Growth Model')
plt.title('von Bertalanffy Tumor Growth Model',fontsize=18,fontweight='bold',color='darkgreen')
plt.xlabel('Time in days',fontsize=10,color='darkgreen')
plt.ylabel('Volume of Tumor in mm^3',fontsize=10,color='darkgreen')
plt.grid(alpha=0.2)
plt.legend()
plt.savefig("von_bertalanffy_tumor_growth_model.png",dpi=150)
plt.show()
