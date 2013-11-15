From: http://en.wikipedia.org/wiki/ReStructuredText
===================================================
Headers:

Section Header
==============

Subsection Header
-----------------

Lists:

- A bullet list item

- Second item

  - A sub item

- Third item

1) An enumerated list item

2) Second item

   a) Sub item that goes on at length and thus needs
      to be wrapped. Note the indentation that must
      match the beginning of the text, not the 
      enumerator.

      i) Sub-sub item

3) Third item

4) Another enumerated list item

5) Second item  

Images:

.. image:: https://pypip.in/d/textblob/badge.png
    :target: https://crate.io/packages/textblob/
    :alt: Number of PyPI downloads

Named links:

A sentence with links to Wikipedia_ and the `Linux kernel archive`_.

.. _Wikipedia: http://www.wikipedia.org/
.. _Linux kernel archive: http://www.kernel.org/

Anonymous links:

Another sentence with an `anonymous link to the Python website`__.

__ http://www.python.org/

N.B.: named links and anonymous links are enclosed in grave accents (`), and not in apostrophes (').

Literal blocks:

::

  some literal text

This may also be used inline at the end of a paragraph, like so::

  some more literal text

.. code-block:: python

   print("A literal block directive explicitly marked as python code")

End of file.
