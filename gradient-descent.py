from __future__ import division
import numpy
import matplotlib.pyplot as pyplot
import matplotlib.colors

def f(x, y):
	'''This is Rosenbrocks Banana Function - the function to be minimised.'''
	return (1-x)**2 + 100*(y-x**2)**2

def grad(x, y):
	'''This function returns the vector gradient of f(x, y).'''
	#Evaluate the partial derivatives
	df_dx = 2*(200*x**3 - 200*x*y + x - 1)
	df_dy = 200*(y - x**2)
	#Find the gradient of the funtion
	grad = numpy.array((df_dx, df_dy))
	return grad

#Set the maximum number of gradient descent steps to make and the convergence criteria
max_iter = 10000
convergence_criteria = 1e-10

def gradient_descent(x0, y0, gamma):
	'''This function takes an initial point and a gamma parameter and performs a number of iterations of the gradient descent method from that point, returning the trajectory.'''
	#Initialise the simulation parameter
	r = numpy.array((x0, y0))
	#Make two lists to store the values of x and y after each iteration
	x_values = []
	y_values = []
	x_values.append(r0[0])
	y_values.append(r0[1])
	for i in range(max_iter):
		#Evaluate f(r) before and after each iteration
		f_before = f(r[0], r[1])
		r = r - gamma * grad(r[0], r[1])
		f_after = f(r[0], r[1])
		#Append the new values of x and y to the lists
		x_values.append(r[0])
		y_values.append(r[1])
		#Terminate the for loop early upon reaching the convergence criteria
		if abs(f_after - f_before) < convergence_criteria:
			break
	#Put the trajectory into an array
	trajectory = numpy.array((x_values, y_values))
	return trajectory

#Set the range to plot over and number of points on each axis
x0, x1 = -0.2, 1.2
y0, y1 = 0.2, 1.2
n_points = 1000

#Calculate the resulting step size between the points on each axis
dx = (x1 - x0) / n_points
dy = (y1 - y0) / n_points
#Generate all the x and y values
x_axis = numpy.arange(x0, x1, dx)
y_axis = numpy.arange(y0, y1, dy)

#Put our data into some array
dat = numpy.zeros((len(y_axis), len(x_axis)))
for iy, y in enumerate(y_axis):
	for ix, x in enumerate(x_axis):
		dat[iy, ix] = f(x, y)

pyplot.figure(figsize = (11,6))
pyplot.title("Gradient descent trajectories")
pyplot.xlabel("x")
pyplot.ylabel("y")

#Plot f(x, y)
im = pyplot.imshow(dat, extent = (x0, x1, y0, y1), origin = "lower", cmap = matplotlib.cm.gray, norm = matplotlib.colors.LogNorm(vmin = 0.01, vmax = 200))
pyplot.colorbar(im, orientation = "vertical")

#Set the starting point and the different values of gamma
r0 = (0.2, 1.0)
gammas = [7e-7, 0.003, 0.002]

#Plot the trajectory for each value of gamma
for gamma in gammas:
	values = gradient_descent(r0[0], r0[1], gamma)
	if gamma == gammas[0]:
		pyplot.plot(values[0, :], values[1, :], marker = "o", color = "blue", label = "gamma too small")
	elif gamma == gammas[1]:
		pyplot.plot(values[0, :], values[1, :], marker = "o", color = "red", label = "gamma too large")
	elif gamma == gammas[2]:
		pyplot.plot(values[0, :], values[1, :], marker = "o", color = "green", label = "gamma well chosen")
		#Find the minimum of the function
		x_minimum = values[0, -1]
		y_minimum = values[1, -1]
		print("Minima occurs at %.2f, %.2f" % (x_minimum, y_minimum))

pyplot.legend(loc = 3)
pyplot.show()
