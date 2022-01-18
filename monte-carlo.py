'''This module uses random numbers to estimate the value of pi. A curve is plotted showing the root mean square value of the error against the number of random points cast.'''

from __future__ import division
import numpy
import numpy.random
import matplotlib.pyplot as pyplot

def estimate_pi(n):
	'''This function estimates the value of pi using the 'hit and miss' method of Monte Carlo integration.'''
	#Generate n random x and y coordinates
	xs = numpy.random.uniform(0, 1, n)
	ys = numpy.random.uniform(0, 1, n)
	#Initialise the simulation parameter
	points_within = 0
	for i in range(n):
		if xs[i]**2 + ys[i]**2 <= 1:
			points_within = points_within + 1
		else:
			points_within = points_within
	return 4 * points_within / n

def measure_error(n):
	'''This function calls estimate_pi(n) 80 times and calculates the root mean square value of the error in those estimates.'''
	#Create an array to store all the estimates of pi
	pi_values = numpy.zeros(80)
	for i in range(80):
		pi_values[i] = estimate_pi(n)
	#Calculate the root mean square value of the error in the estimates of pi
	return numpy.mean((pi_values - numpy.pi)**2)**(1/2)

pyplot.figure()

#Range of point counts to be evaluated
point_counts = [25, 50, 100, 200, 400, 800, 1600, 3200, 6400, 12800, 25600, 51200]

#Evaluate the root mean square value of the error for each point count and put them in a Python list
y_data = []
for i in point_counts:
	error = measure_error(i)
	y_data.append(error)

#Plot a graph of the root mean square value of the error against point count
pyplot.title("Error scaling with the 'hit and miss' method")
pyplot.ylabel("rms error")
pyplot.xlabel("number of points cast")
pyplot.plot(point_counts,y_data,"-o")
pyplot.loglog()
pyplot.show()

#COMMENT: The accuracy increases with the number of points. Whether a point lies within the quarter-circle or not is random. Therefore, due to the central limit theorem, the error in the resulting estimate of pi is inversely proportional to the square root of the number of points.

