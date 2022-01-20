from __future__ import division
import numpy
import matplotlib.pyplot as pyplot

#Set the half life of the isotope in hours: 20.8
T_HALF=20.8
TAU=T_HALF/numpy.log(2)

def f(n):
	'''This function implements the differential equation for the radioactive decay of n nuclei'''
	return -n/TAU

def analytic(N0,timebase):
	'''This function returns the atom count for a series of times, given an initial number of atoms N0'''
	return N0*numpy.exp(-timebase/TAU)

def solve_euler(N0,t1,N_PANELS):
	'''This function uses Euler's method to solve the differential equation'''
	dt=t1/N_PANELS
	#Initialise simulation parameter
	n=N0
	#Make an array to hold the counts at each time point
	n_history=numpy.zeros((N_PANELS),dtype=numpy.float32)
	n_history[0]=N0
	for i in range(1,N_PANELS):
		n=n+f(n)*dt
		n_history[i]=n
	return n_history

def solve_heun(N0,t1,N_PANELS):
	'''This function uses Heun's method to solve the differential equation'''
	dt=t1/N_PANELS
	#Initialise simulation parameter
	n=N0
	#Make an array to hold the counts at each time point
	n_history=numpy.zeros((N_PANELS),dtype=numpy.float32)
	n_history[0]=N0
	for i in range(1,N_PANELS):
		k0=f(n)
		k1=f(n+k0*dt)
		n=n+dt/2*(k0+k1)
		n_history[i]=n
	return n_history

#Set the initial number of nuclei
N0=1200
#The programme integrates over the range 0 <= t < t1. Set t1 in hours.
t1=60
#Set the number of panels to divide the time range into and calculate the time at the start of each panel
N_PANELS=15
timebase=numpy.arange(0,t1,t1/N_PANELS)

#Evaluate the various methods
n_analytic=analytic(N0,timebase)
n_euler=solve_euler(N0,t1,N_PANELS)
n_heun=solve_heun(N0,t1,N_PANELS)

pyplot.figure()

#Plot the upper graph: both numeric decay curves, as well as the analytic solution, against time
pyplot.subplot(211)
pyplot.title("Radioactive decay curves")
pyplot.ylabel("atom count")
pyplot.xlabel("time / hours")
pyplot.plot(timebase,n_analytic,color="grey",label="analytic solution")
pyplot.plot(timebase,n_euler,color="red",label="Euler's method")
pyplot.plot(timebase,n_heun,color="blue",label="Heun's method",linestyle="--")
pyplot.legend()

#Plot the lower graph: the absolute relative error in the two numeric decay curves against time
pyplot.subplot(212)
pyplot.title("Error scaling compared for ODE solvers")
pyplot.ylabel("absolute relative error")
pyplot.xlabel("time / hours")
error_euler=abs((n_euler-n_analytic)/n_analytic)
pyplot.plot(timebase,error_euler,color="red",label="Euler's method")
error_heun=abs((n_heun-n_analytic)/n_analytic)
pyplot.plot(timebase,error_heun,color="blue",label="Heun's method")
pyplot.semilogy()
pyplot.legend(loc=4)

pyplot.tight_layout()
pyplot.show()
