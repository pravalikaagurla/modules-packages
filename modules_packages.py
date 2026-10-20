Python 3.13.14 (tags/v3.13.14:fd17997, Jun 10 2026, 13:03:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import math
>>> import random
>>> import datetime
>>> #1.math module
>>> number = 25
>>> square_root = math.sqrt(number)
>>> print("1.math module")
1.math module
>>> print("Number:", number)
Number: 25
>>> print("square root:",square_root)
square root: 5.0
>>> #2.Random module
>>> random_number = random.randint(1,100)
>>> print("2.Random module")
2.Random module
>>> print("Random number between 1 and 100:", random_number)
Random number between 1 and 100: 99
>>> #3.Datetime module
>>> current_datetime = datetime.datetime.now()
>>> print("3.Datetime module")
3.Datetime module
>>> print("current date and time:", current_datetime.strftime("%d-%m-%y %H:%M:%S"))
current date and time: 20-10-26 12:57:46
