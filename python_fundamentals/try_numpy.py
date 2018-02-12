''' Optional Assignment: NumPy
Build a simple program using the NumPy module.
You might have heard of NumPy. It's a library created for handling more complex mathematical functions. NumPy is often cited as being an important asset in any Data Scientist's toolkit and is widely used by scientists, mathematicians, engineers, and more.
Much like the module from the previous assignment, you'll want to install NumPy in a virtual environment.
Here's what I did to install numpy... The virtual env I had create earlier is named pyproj:
$ source pyproj/bin/activate
I now see a (pyproj) appear at the beginning of myproject terminal prompt indicating that you are working inside the virtualenv. Then I installed requests in the virtualenv
$ pip install numpy '''

import numpy as np
a = np.arange(15).reshape(3, 5)
print "a:", a
print "a.shape = ", a.shape
print "a.ndim = ", a.ndim
print "a.dtype.name = ", a.dtype.name
print "a.itemsize = ", a.itemsize
print "a.size = ", a.size
print "type(a) = ", type(a)
b = np.array([6, 7, 8])
print "b:", b
print "type(b) = ", type(b)
