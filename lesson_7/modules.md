# Modules

As your codebase becomes larger and larger, it becomes difficult to keep everything in one file.
Things just become too inconvenient. It is better to spread your code out over multiple files.

I have taken the code from the previous lesson, split it into pieces and moved each piece into
a separate Python file:

* The FuelType class has been moved to [fuel.py](fuel.py)
* The Engine, Tire and Door classes have been moved to [parts.py](parts.py)
* The FuelStation and Garage classes have been moved to [services.py](services.py)
* The Vehicle, Car and Motorcycle classes have been moved to [vehicles.py](vehicles.py)

The main.py file only contains the main function.

## Linking modules together

Moving our classes to other files looks good, but how to we refer to then from our main function?
How to we tell Python that the code for the FuelStation class can be found in the [services.py](services.py) file?
We can do this by using *import* statements. If we take a look at the top 
of the [main.py](main.py) file, we will see the following lines of code:

```Python
from services import FuelStation, Garage
from fuel import FuelType
from vehicles import Car, Motorcycle
from parts import Tire
```

These lines of code tell Python where the classes used in the main function can be found. These
lines all take the format of `from file_name import class_name`.

Take a look at the Python files in this lesson. Try removing one of the import lines and see what happens when your run the code. 
