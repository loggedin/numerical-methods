from __future__ import division
import numpy
import matplotlib.pyplot as pyplot

def f(x):
	'''This function is equivalent to the mathematical function f(x)=cos(x)'''
	return numpy.cos(x)

def g(x):
	'''This function is the analytical derivative of f(x) with respect to x'''
	return -numpy.sin(x)

def g_bdm(x,dx):
	'''This function uses the backwards difference method to estimate the derivative of f(x) with respect to x, using a step size of dx'''
	return (f(x)-f(x-dx))/dx

#Make a series of 100 uniformally spaced values between -2*pi and 2*pi
xs=numpy.linspace(-2*numpy.pi,2*numpy.pi,100)

#Evaluate the derivatives
df_dx_small=g_bdm(xs,dx=1e-14)
df_dx_large=g_bdm(xs,dx=1e-2)
df_dx_good=g_bdm(xs,dx=1e-7)
df_dx_analytical=g(xs)

#Plot the error in the estimates of the derivative of f(x) with respect to x, as calculated using several values of dx
pyplot.figure(figsize=(8,4))
pyplot.title("Error in estimates of df/dx")
pyplot.xlabel("x")
pyplot.ylabel("error in estimate of df/dx")
pyplot.plot(xs,df_dx_small-df_dx_analytical,color="blue",label="dx is too small")
pyplot.plot(xs,df_dx_large-df_dx_analytical,color="red",label="dx is too large")
pyplot.plot(xs,df_dx_good-df_dx_analytical,color="green",label="dx is well chosen")
pyplot.legend()
pyplot.show()
