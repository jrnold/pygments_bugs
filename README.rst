================
Pygments Stan
================

`Pygments <http://pygments.org/>`_ support for the `STAN
<http://code.google.com/p/stan/>`_ language.


Installation and Usage
--------------------------

Install the module using setuptools.

.. code:: 

   python setup.py install


Use `pygmentize <http://pygments.org/docs/cmdline/>`_ to format the code. 

.. code::

   pygmentize -O full -o example.html example.stan
