# numerical-methods

This repository contains scripts that demonstrate various numerical methods.

## backwards-difference.py

This script uses the backwards difference method to estimate the derivatve of a function. For each of the several values of step size used, a curve is plotted showing the error in the corresponding estimate.

	python3 backwards-difference.py

Example output:

![backwards-difference](https://user-images.githubusercontent.com/97130665/150409317-95b0076e-ca7c-4a41-99a1-a579f025d8a8.png)

The maximum precision of a floating-point number in Python is 16 significant figures. Therefore, when dx is too small there is a varying percentage error in f(x)-f(x-dx), explaining the erratic error plot. When dx is too large, the estimate loses accuracy because f(x) is nonlinear.

## simpson.py

This script calculates the definite integral of a function using Simpson's 1/3 rule. A curve is plotted showing the relative error in the numerical method against the number of panels used.

	python3 simpson.py

Example output:

![simpson](https://user-images.githubusercontent.com/97130665/150401285-0db0cfaa-ee79-44ff-8cf4-6e7a2320ea71.png)

As the panel count increases, the quadratic fits for each panel become more accurate, so the accuracy of the numerical method increases.

It is interesting to note that, since the precision of floating-point numbers in Python is finite, there is a varying percentage error in integrate_simpson(x0,x1,i)-ref. This becomes significant when the panel count exceeds 1e3 and causes the corresponding accuracy of the method to fluctuate.

## euler-heun.py

This script uses both Euler and Heun's methods to solve the differential equation that describes radioactive decay. A figure containing two graphs is produced: the upper graph plots both numeric decay curves, as well as the analytic solution, against time; the lower graph plots the absolute relative error in the numeric decay curves against time.

	python3 euler-heun.py

Example output:

![euler-heun](https://user-images.githubusercontent.com/97130665/150409899-07589d94-ec1c-414e-af49-15f7b8d0b9a5.png)

Both the Euler and Heun methods split the solution of the given differential equation into a series of intervals. The Euler method uses the gradient of the solution at the beginning of each interval to estimate the next point in the solution. This assumes that the solution is linear. However, the Heun method uses the average of the gradients at the beginning and end of each interval to estimate the next point in the solution. Therefore, the Heun method is more accurate than the Euler method as it takes the fact that the solution may be nonlinear into consideration.

## gradient-descent.py

This script produces a plot and text illustrating the different behaviours of the gradient descent method when finding the minimum of Rosenbrock's Banana Function. It also gives where the minimum of the function occurs.

	python3 gradient-descent.py

Example output:

![gradient-descent](https://user-images.githubusercontent.com/97130665/150395299-323108c2-81fc-4962-9516-a9455b838d50.png)

When the step size parameter is too small, convergence is very slow. Indeed, despite 10,000 gradient descent steps, the plotted trajectory for this case does not reach the minimum. When the step size is too large, the gradient descent method is unstable as the trajectory either overshoots the minimum or never reaches it at all. Indeed, the plotted trajectory for this case reaches the valley of the function but does not approach the minimum.

## chemotaxis.py

This script produces a simulation of Chemotaxis, a modified random walk used by some bacteria to find food sources.

	python3 chemotaxis.py

Example output:

![chemotaxis](https://user-images.githubusercontent.com/97130665/151034964-9af19b63-158e-4742-9ea4-dcb91c7557dd.png)

The sensitivity of the bacteria, k, cannot be too big. Indeed, when k is very large, the bacteria behave very similarly to the case where k = 0.2: they reach the position of maximum energy density in around fifty seconds. When k is too small, the bacteria take longer to reach the position of maximum energy density. This is because the bacteria are less likely to tumble when the energy density is decreasing.

## newton-raphson.py

This script demonstrates the chaotic behaviour of the Newton-Raphson method.

	python3 newton-raphson.py

Example output:

![newton-raphson](https://user-images.githubusercontent.com/97130665/150395723-2d24309d-741f-494f-8325-bacee6ef067a.png)

The left-hand diagrams show the identified roots for different ranges of seed points; the right-hand diagrams show the number of iterations, or convergence time, to locate the identified roots for these seed points. Both sets of diagrams demonstrate the chaotic behaviour of the respective aspect of the Newton-Raphson method because they are extremely complex. This shows that, although they are completely deterministic, both aspects are highly sensitive to the initial conditions and exhibit topological mixing. Furthermore, the images in the diagrams are said to be fractal in nature because they have self-similarity, that is, they look the same at difference scales. This is shown by the lower diagrams which have different scales to the corresponding diagrams above.

## monte-carlo.py

This script uses random numbers to estimate the value of pi. A curve is plotted showing the root mean square value of the error against the number of random points cast.

	python3 monte-carlo.py

Example output:

![monte-carlo](https://user-images.githubusercontent.com/97130665/150401346-d9524f28-5623-4c1b-9797-b63de5108b2b.png)

The accuracy increases with the number of points. Whether a point lies within the quarter-circle or not is random. Therefore, due to the central limit theorem, the error in the resulting estimate of pi is inversely proportional to the square root of the number of points.
