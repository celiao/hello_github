README file.

Play with Markdown features
=======================================

- first bullet
- second bullet

Now some code
-------------

Here it is:
```python
print('This is some python code.')
print('Here is some more code.')


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

#) Another enumerated list item

#) Second item  

Images:

.. image:: /path/to/image.jpg

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

