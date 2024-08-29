from __future__ import division
import numpy
import matplotlib.pyplot as pyplot
import matplotlib.colors

def f(z):
	'''This function is equivalent to the mathematical function f(z) = z**4 - 1.'''
	return z**4 - 1

def g(z):
	'''This function returns the analytical derivative of f(z) with respect to z.'''
	return 4 * z**3

#Set the maximum number of iterations to make and the convergence criteria
max_iter = 35
convergence_criteria = 1e-5

def newton_raphson(z0):
	'''This function uses the Newton-Raphson method to find the roots of f(z).'''
	#Initialise the simulation parameter
	z = z0
	for i in range(max_iter):
		z = z - f(z) / g(z)
		f_after = f(z)
		if abs(f_after) < convergence_criteria:
			break
	#Quantise the roots
	if numpy.angle(z) > -1/4*numpy.pi and numpy.angle(z) < 1/4*numpy.pi:
		return numpy.array([0, i])
	elif numpy.angle(z) > 1/4*numpy.pi and numpy.angle(z) < 3/4*numpy.pi:
		return numpy.array([1, i])
	elif numpy.angle(z) > 3/4*numpy.pi and numpy.angle(z) < -3/4*numpy.pi:
		return numpy.array([2, i])
	elif numpy.angle(z) > -3/4*numpy.pi and numpy.angle(z) < -1/4*numpy.pi:
		return numpy.array([3, i])
	else:
		return numpy.array([4, i])

pyplot.figure()

#Set the number of points on each axis for all the subplots
n_points = 300

#Set the range to plot over for the top two subplots
x0_out, x1_out = -2.0, 2.0
y0_out, y1_out = -2.0, 2.0
#Calculate the resulting step size between the points on each axis
dx_out = (x1_out - x0_out) / n_points
dy_out = (y1_out - y0_out) / n_points
#Generate all the x and y values
x_axis_out = numpy.arange(x0_out, x1_out, dx_out)
y_axis_out = numpy.arange(y0_out, y1_out, dy_out)

#Plot the roots on the top left subplot
pyplot.subplot(221)
pyplot.title("Identified roots")
pyplot.ylabel("Imaginery")
pyplot.yticks(numpy.arange(y0_out, y1_out + 1.0, 1.0))
pyplot.xlabel("Real")
pyplot.xticks(numpy.arange(x0_out, x1_out + 1.0, 1.0))
#Label the plot to show which colour corresponds which which root
pyplot.annotate("1", xy = (0, 0), xytext = (1.4, -0.1), color = "white")
pyplot.annotate("i", xy = (0, 0), xytext = (0, 1.4), color = "white")
pyplot.annotate("-1", xy = (0, 0), xytext = (-1.4, -0.1))
pyplot.annotate("- i", xy = (0, 0), xytext = (0, -1.4))

#Put the data into an array
dat_1 = numpy.zeros((len(y_axis_out), len(x_axis_out)))
for iy, y in enumerate(y_axis_out):
	for ix, x in enumerate(x_axis_out):
		dat_1[iy, ix] = newton_raphson(x+y*1j)[0]

#Plot the data
im = pyplot.imshow(dat_1, extent = (x0_out, x1_out, y0_out, y1_out), origin = "lower", cmap = matplotlib.cm.hot)

#Plot the convergence time on the top right subplot
pyplot.subplot(222)
pyplot.title("Convergence time")
pyplot.ylabel("Imaginery")
pyplot.yticks(numpy.arange(y0_out, y1_out + 1.0, 1.0))
pyplot.xlabel("Real")
pyplot.xticks(numpy.arange(x0_out, x1_out + 1.0, 1.0))

dat_2 = numpy.zeros((len(y_axis_out), len(x_axis_out)))
for iy, y in enumerate(y_axis_out):
	for ix, x in enumerate(x_axis_out):
		dat_2[iy, ix] = newton_raphson(x+y*1j)[1]

im = pyplot.imshow(dat_2, extent = (x0_out, x1_out, y0_out, y1_out), origin = "lower", cmap = matplotlib.cm.BuPu)
pyplot.colorbar(im, orientation = "vertical")

#Set the range to plot over for the bottom two subplots
x0_in, x1_in = 1.4, 1.8
y0_in, y1_in = 1.4, 1.8
#Calculate the resulting step size between the points on each axis
dx_in = (x1_in - x0_in) / n_points
dy_in = (y1_in - y0_in) / n_points
#Generate all the x and y values
x_axis_in = numpy.arange(x0_in, x1_in, dx_in)
y_axis_in = numpy.arange(y0_in, y1_in, dy_in)

#Plot the roots on the bottom left subplot
pyplot.subplot(223)
pyplot.title("x100 zoom")
pyplot.ylabel("Imaginery")
pyplot.yticks(numpy.arange(y0_in, y1_in + 0.1, 0.1))
pyplot.xlabel("Real")
pyplot.xticks(numpy.arange(x0_in, x1_in + 0.1, 0.1))

dat_3 = numpy.zeros((len(y_axis_in), len(x_axis_in)))
for iy, y in enumerate(y_axis_in):
	for ix, x in enumerate(x_axis_in):
		dat_3[iy, ix] = newton_raphson(x+y*1j)[0]

im = pyplot.imshow(dat_3, extent = (x0_in, x1_in, y0_in, y1_in), origin = "lower", cmap = matplotlib.cm.hot)

#Plot the convergence time on the bottom right subplot
pyplot.subplot(224)
pyplot.title("x100 zoom")
pyplot.ylabel("Imaginery")
pyplot.yticks(numpy.arange(y0_in, y1_in + 0.1, 0.1))
pyplot.xlabel("Real")
pyplot.xticks(numpy.arange(x0_in, x1_in + 0.1, 0.1))

dat_4 = numpy.zeros((len(y_axis_in), len(x_axis_in)))
for iy, y in enumerate(y_axis_in):
	for ix, x in enumerate(x_axis_in):
		dat_4[iy, ix] = newton_raphson(x+y*1j)[1]

im = pyplot.imshow(dat_4, extent = (x0_in, x1_in, y0_in, y1_in), origin = "lower", cmap = matplotlib.cm.BuPu)
pyplot.colorbar(im, orientation = "vertical")

pyplot.tight_layout()
pyplot.show()
