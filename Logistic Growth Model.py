import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Initial Conditions
y0=[2] # we start the model with 2 bacteria

t=np.linspace(0,1000,num=2500) # bacteria growth being shown over 1000 time units, with 2500 interim points 

# Parameters we are using in the model

r=0.1 # growth rate of bacteria
K=10000 # carrying capacity of the environment in which the bacteria are growing

parameters=[r,K] # We define the parameters into a list so that is is easier to pass them into the odeint function

def model(variables,t,parameters):

    P = variables[0] # we define the variable P which is the population of bacteria at each time point t
    r= parameters[0] # we assign the growth rate of bacteria as the first parameter of the function
    K= parameters[1] # we assign the carrying capacity of given environment as the second parameter of the function

    dPdt = r*P*(1-P/K) # we define the ODE that describes the growth of bacteria over time, given certain parameters
    
    return([dPdt]) # we return the value of the ODE at every time point t

population=odeint(model,y0,t,args=(parameters,)) 

# Now we plot the results of the model to visualize the growth of the bacteria that we have simulated over time

plt.plot(t,population[:,0],color='pink',linewidth=2)
plt.title('Bacteria Logistic Growth Model',fontsize=25,fontweight='bold',color='purple')
plt.xlabel('Time (in arbitrary units)',fontsize=15,color='purple')
plt.ylabel('Population of Bacteria', fontsize=15,color='purple')
plt.savefig("logistic_growth.png", dpi=150) 
plt.show() 