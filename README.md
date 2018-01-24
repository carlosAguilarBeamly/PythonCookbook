Getting the Most Out of docstrings Part 1 – PEP 257 and Sphinx:

Basic rules for docstrings:
- use triple quotes
- 1st line is a short description
- Blank-line and then a more detailed description

Using reStructuredText. Follow https://devguide.python.org/


Sphinx:

type sphinx-quickstart
It will ask for a root folder ('docs'). make sure the autodoc plugin is enabled.
sphinx-apidoc -o docs example
emacs conf.py
In the conf.py file add 
	import os
	import sys
	sys.path.append(os.path.abspath('..'))
make html