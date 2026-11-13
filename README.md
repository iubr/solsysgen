# Solar system generator

## What is this software for
Implements a Python code which generates a solar system based on a simple heliocentric model with circular orbits in 2D.

This is the code structure:

```text
solsysgen/
|----- __init__.py
|----- celestial_object.py     # Parent class of Sun and Planet 
|----- sun.py                  # Sun class
|----- planet.py               # Planet class
|----- solarsystem.py          # SolarSystem class
|----- checkpoint.py           # Read/write from/to checkpoint files.
```

Here is an equation:
```math
E = mc^2
```

a link [here](https://astronomy.stackexchange.com/questions/26728/simple-mathematical-models-of-solar-systems)

- Implement a Sun class with mass, radius and luminosity as attributes. This is an inline equation $E=mc^2$

- Implement a Planet class with attributes mass, radius, type, starting position, distance from the sun, orbital velocity, period, etc. 

- Implement a SolarSystem class consisting of one sun and a collection of planets. Allow the user to define the attributes of the sun and the number of planets in the solar system, then generate a set of planets following (some) of the rules described here. Determine the planets' periods of rotation based on Kepler's third law.

![solar system illustration](solar_system.png)

## How to install

Installation instructions go here.

## How to run

Examples of running the code go here


## Other information 
