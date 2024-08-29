from __future__ import division
import numpy
import numpy.random
import matplotlib.pyplot as pyplot
import matplotlib.colors

def f(x, y):
	'''This function returns the energy density.'''
	return 2000 - x**2 - y**2

run_time = 100					#run time in seconds
dt = 0.1					#timestep in seconds
timebase = numpy.arange(0, run_time, dt)	#an array containing all the time points in seconds
v = 2						#speed of bacteria in microns per second
k = 0.2						#sensitivity of bacteria
x0, y0 = 30, 20					#origin of bacteria in microns

def random_walk(x0, y0):
	'''This function returns the trajectory of a bacterium.'''
	#Set an initial bearing
	theta = 0
	#Make two lists to hold the x and y coordinates respectively of the trajectory at each time point
	x_values = [x0]
	y_values = [y0]
	#Initialise the simulation parameters
	x = x0
	y = y0
	#Make a shift register
	shift = [700, 700, 700, 700, 700, 700, 700, 700, 700, 700]
	while len(y_values) < len(timebase):
		#Evaluate de/dt at the time point
		de = shift[-1] - shift[0]
		de_dt = de / (10 * dt)
		#Calculate the probability of not tumbling at the time point
		t_half = 1 + k * de_dt
		if t_half < 0.1:
			t_half = 0.1
		tau = t_half / numpy.log(2)
		pnt = numpy.exp(- dt / tau)
		#Account for a tumble if necessary
		if numpy.random.uniform() > pnt:
			if len(y_values) < len(timebase):
				x_values.append(x)
				y_values.append(y)
				shift.append(f(x, y))
				shift = shift[-10:]
				theta = 2 * numpy.pi * numpy.random.uniform()
		x = x + v * numpy.cos(theta) * dt
		y = y + v * numpy.sin(theta) * dt
		if len(y_values) < len(timebase):
			x_values.append(x)
			y_values.append(y)
			shift.append(f(x, y))
			shift = shift[-10:]
	#Put the trajectory into an array
	trajectory = numpy.array((x_values, y_values))
	return trajectory

pyplot.figure()

#Set the range to plot over and number of points on each axis
x_axis_start, x_axis_end = -20, 40
y_axis_start, y_axis_end = -30, 40
n_points = 1000
#Calculate the resulting step size between the points on each axis
dx = (x_axis_end - x_axis_start) / n_points
dy = (y_axis_end - y_axis_start) / n_points
#Generate all the x and y values
x_axis = numpy.arange(x_axis_start, x_axis_end, dx)
y_axis = numpy.arange(y_axis_start, y_axis_end, dy)
#Put the data into an array
dat = numpy.zeros((len(y_axis), len(x_axis)))
for iy, y in enumerate(y_axis):
	for ix, x in enumerate(x_axis):
		dat[iy, ix] = f(x, y)

sub221 = pyplot.subplot(221)
pyplot.title("Bacteria trajectories")
pyplot.xlabel("x / microns")
pyplot.ylabel("y / microns")
im = pyplot.imshow(dat, extent = (x_axis_start, x_axis_end, y_axis_start, y_axis_end), origin = "lower", cmap = matplotlib.cm.gray, norm = matplotlib.colors.Normalize(vmin = -3000, vmax = 2000))
pyplot.colorbar(im, orientation = "vertical")

sub222 = pyplot.subplot(222)
pyplot.title("Simplified trajectories")
pyplot.xlabel("x / microns")
pyplot.ylabel("y / microns")
pyplot.axis([-10, 40, -10, 30])

#Two arrays to store the square displacements for each bacterium at each time point
square_differences_origin = numpy.zeros((20, 1000))
square_differences_maximum = numpy.zeros((20, 1000))

for i in range(20):
	values = random_walk(x0, y0)
	
	sub221.plot(values[0, :], values[1, :])
	
	sub222.plot([values[0, 0], values[0, -1]], [values[1, 0], values[1, -1]], marker = "o")
	
	x_differences_origin = values[0, :] - 30.0
	y_differences_origin = values[1, :] - 20.0
	square_displacements_origin = x_differences_origin**2 + y_differences_origin**2
	square_differences_origin[i] = square_displacements_origin
	
	x_differences_maximum = values[0, :]
	y_differences_maximum = values[1, :]
	square_displacements_maximum = x_differences_maximum**2 + y_differences_maximum**2
	square_differences_maximum[i] = square_displacements_maximum

mean_square_differences_origin = []
for i in range(len(timebase)):
	mean_square_differences_origin.append(1 / 20 * numpy.sum(square_differences_origin[:, i]))

mean_square_differences_maximum = []
for i in range(len(timebase)):
	mean_square_differences_maximum.append(1 / 20 * numpy.sum(square_differences_maximum[:, i]))

pyplot.subplot(212)
pyplot.title("Mean square displacements")
pyplot.xlabel("time / s")
pyplot.ylabel("MSD / microns")
pyplot.plot(timebase, mean_square_differences_origin, color = "blue", label = "from origin")
pyplot.plot(timebase, mean_square_differences_maximum, color = "green", label = "from maximum energy")
pyplot.legend(loc = 5)

pyplot.tight_layout()
pyplot.show()
