# PythonCookbook
Collection of recipes for the perfect Python meal.

## Basic rules for docstrings:
* use triple quotes
* 1st line is a short description
* Blank-line and then a more detailed description

Using reStructuredText. Follow https://devguide.python.org/


## Sphinx:
* type sphinx-quickstart
* It will ask for a root folder ('docs'). 
* Make sure the autodoc plugin is enabled.
* sphinx-apidoc -o docs example
    * (sphinx-apidoc -o docs . -f)
* emacs conf.py
* In the conf.py file add 
    * 	import os
    * 	import sys
    * 	sys.path.append(os.path.abspath('..'))
* cd docs
* make html

## Guidelines
The cookbook is a collection of recipes. Each recipe contains:
* A description (mandatory) 
* A long description [optional]
* Ingredients (following PEP8 conventions)
* Category (mandatory)
* Method