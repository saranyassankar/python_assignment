Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> num1 = float(input("Enter the first number: "))
... 
Enter the first number: 34.6
>>> num2 = float(input("Enter the second number: "))
Enter the second number: 56.9
>>> num3 = float(input("Enter the third number: "))
Enter the third number: 78.9
>>> maximum = num1
>>> minimum = num1
>>> if num2 > maximum:
...    maximum = num2
... elif num2 < minimum:
...    minimum = num2
... 
>>> if num3 > maximum:
...     maximum = num3
... elif num3 < minimum:
...     minimum = num3
... 
>>> print("Maximum value:", maximum)
Maximum value: 78.9
>>> print("Minimum value:", minimum)
Minimum value: 34.6
