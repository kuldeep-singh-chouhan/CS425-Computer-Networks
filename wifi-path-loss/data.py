# 200530 Kuldeep Singh Chouhan

import numpy as np
import matplotlib.pyplot as plt

# for question 1
#define data of distances and RSSI
x = np.array([0.0, 0.0, 0.0, 0.0, 0.3010299956639812, 0.3010299956639812, 0.3010299956639812, 0.3010299956639812, 0.47712125471966244, 0.47712125471966244, 0.47712125471966244, 0.47712125471966244, 0.6020599913279624, 0.6020599913279624, 0.6020599913279624, 0.6020599913279624, 0.6989700043360189, 0.6989700043360189, 0.6989700043360189, 0.6989700043360189, 0.7781512503836436, 0.7781512503836436, 0.7781512503836436, 0.7781512503836436, 0.8450980400142568, 0.8450980400142568, 0.8450980400142568, 0.8450980400142568])
y = np.array([-71,-73,-76,-81,-73,-76,-79,-82,-79,-79,-81,-82,-82,-80,-83,-89,-77,-83,-89,-84,-84,-88,-86,-88,-88,-88,-88,-88])

#find line of best fit
a, b = np.polyfit(x, y, 1)

#add points to plot
plt.scatter(x, y, color='goldenrod')

#add line of best fit to plot
plt.plot(x, a*x+b, color='steelblue', linestyle='--', linewidth=2)
plt.xlabel("Distance from the transmitter (in log(d/d_0))")
plt.ylabel("Received Signal Strength (in dBm)")


# for question 2
# sample for RSSI values
collectedStrength = np.array([-71,-76,-81,-82,-84])

predictedDistance = []
predictionError = []
i=1

strength_d0 = 68  # signal strength at d=1m
refernceDistance = 2.24

for elem in collectedStrength:
    predictedDistance.append(10**((elem+strength_d0)/a))
    predictionError.append(abs(10**((elem+strength_d0)/a) - i*refernceDistance))
    i=i+1


print("Best Fit Line equation: y = " + "{:.2f}".format(b) + " + {:.2f}".format(a) + "x")

z=[]
for i in x:
    z.append(-74.04 -15.13*i)
    
sum=0

for i in range(0,len(x)):
    sum = sum + (y[i]-z[i])*(y[i]-z[i])
print("Variance: ", sum/(len(x)-1)) 

print("Predicted Distance (in m): ",predictedDistance)
print("Error in Predicted Distance (in m): ",predictionError)
print("Average Error (in m): ", np.average(predictionError)) 

#add fitted regression equation to plot
plt.show()