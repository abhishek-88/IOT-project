Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def add(x,y):
	sum = x+y;
	return sum;

<<<<<<< HEAD
>>> a = 57
>>> b = 3
>>> print("Sum is = ", add(a,b))
Sum is =  60
=======
>>> add (10,20)
>>> add
<function add at 0x03E1BD60>
>>> c
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    c
NameError: name 'c' is not defined
>>> def addition (a,b):
	c=a+b;
	return c;

>>> a=300
>>> b=20
>>> print("The addition is = " , addition(a,b))
The addition is =  30
>>>>>>> 1b1e0cc66224cc716ca85204c6eb54b4377bef90
>>> 