# numerical-methods

This repository contains scripts that demonstrate various numerical methods.

## backwards-difference.py

This script uses the backwards difference method to estimate the derivatve of a function. For each of the several values of step size used, a curve is plotted showing the error in the corresponding estimate.

	python3 backwards-difference.py

Example output:

![backwards-difference](https://user-images.githubusercontent.com/97130665/150401262-a8ff538d-c658-4183-9809-c67c445f25f3.png)

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

![euler-heun](https://user-images.githubusercontent.com/97130665/150401322-055aadbc-9a01-4619-b8d1-fd80303c05ab.png)

Both the Euler and Heun methods split the solution of the given differential equation into a series of intervals. The Euler method uses the gradient of the solution at the beginning of each interval to estimate the next point in the solution. This assumes that the solution is linear. However, the Heun method uses the average of the gradients at the beginning and end of each interval to estimate the next point in the solution. Therefore, the Heun method is more accurate than the Euler method as it takes the fact that the solution may be nonlinear into consideration.

## monte-carlo.py

This script uses random numbers to estimate the value of pi. A curve is plotted showing the root mean square value of the error against the number of random points cast.

	python3 monte-carlo.py

Example output:

![monte-carlo](https://user-images.githubusercontent.com/97130665/150401346-d9524f28-5623-4c1b-9797-b63de5108b2b.png)

The accuracy increases with the number of points. Whether a point lies within the quarter-circle or not is random. Therefore, due to the central limit theorem, the error in the resulting estimate of pi is inversely proportional to the square root of the number of points.
