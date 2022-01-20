from __future__ import division
import numpy
import matplotlib.pyplot as pyplot

def f(x):
	'''This function is equivalent to the mathematical function f(x)=x^2*sin(x)'''
	return x**2*numpy.sin(x)

def g(x):
	'''This function is the indefinite integral of f(x)'''
	return 2*x*numpy.sin(x)+(2-x**2)*numpy.cos(x)

def integrate_simpson(x0,x1,n_panels):
	'''This function calculates the definite integral of the function f(x) over the interval [x0,x1] using Simpson's rule and N panels'''
	panel_width=(x1-x0)/n_panels
	area=0
	for i in range(n_panels):
		#Find the left edge of this panel
		a=x0+i*panel_width
		#Find the right edge of this panel
		b=a+panel_width
		area=area+(b-a)/6*(f(a)+4*f((a+b)/2)+f(b))
	return area

#Range of panel counts to be evaluated and bounds to integrate over
panel_counts=[4,8,16,32,64,128,256,512,1024]
x0,x1=0,2

#For reference, calculate the definite integral of f(x) over the interval [x0,x1] using g(x)
ref=g(x1)-g(x0)

#Calculate the value of the relative error in the numerical method for each panel count and put them in a Python list
y_data=[]
for i in panel_counts:
	error=abs((integrate_simpson(x0,x1,i)-ref)/ref)
	y_data.append(error)

#Plot a graph of the relative error in the numerical method against the number of panels used
pyplot.figure(figsize=(6,6))
pyplot.title("Error scaling with Simpson's rule")
pyplot.ylabel("relative error in numerical method")
pyplot.xlabel("number of panels used")
pyplot.plot(panel_counts,y_data,"-o",ms=10)
pyplot.loglog()
pyplot.show()
