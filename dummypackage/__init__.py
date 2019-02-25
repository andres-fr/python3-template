# -*- coding:utf-8 -*-


r"""
Main init file docstring. It exemplifies the usage of `restructured text
<http://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_,
 like:

* *Italics*
* **Bold**
* Numbered and nested lists:
   #. This is a numbered list
   #. Nested lists have at least three characters indentation
* ``Inline literals``
* Parameter fields: see class and method docstrings.



#######################
Section about sections:
#######################

* Surrounding chars have to be at least as long as the title
* No explicit hierarchy, but this recommended: ``#, *, =, -, ^, "`` (the first
 two with overline).


Subsection:
===========

To exemplify the usage of :math:`\text{\LaTeX}` and nested quotes, nothing best
 that the words of Isaac Newton himself:

   "If I have seen further it is by standing on the shoulders of Giants."

Or, in other words:

.. math::

   \sum_{k=1}^{\infty} k = -\frac{1}{12}


#################
Other structures:
#################

Field lists:

:Author:
    Homer J. Simpson
:Email: ``hjs@compuglobalhypermega.net``


Literal blocks, preceded by double colon::

   This is a literal block

   Markups are **not** rendered here.


Doctest blocks can be tested by the doc tool:

>>> [factorial(n) for n in range(6)]
[1, 1, 2, 6, 24, 120]
>>> [factorial(long(n)) for n in range(6)]
[1, 1, 2, 6, 24, 120]


Grid tables must be indented:
   +------------+------------+-----------+
   | Header 1   | Header 2   | Header 3  |
   +============+============+===========+
   | body row 1 | column 2   | column 3  |
   +------------+------------+-----------+
   | body row 2 | Cells may span columns.|
   +------------+------------+-----------+
   | body row 3 | Cells may  | - Cells   |
   +------------+ span rows. | - contain |
   | body row 4 |            | - blocks. |
   +------------+------------+-----------+


Simple table:

=====  =====  ======
   Inputs     Output
------------  ------
  A      B    A or B
=====  =====  ======
False  False  False
True   False  True
False  True   True
True   True   True
=====  =====  ======

"""


name = "dummypackage"
