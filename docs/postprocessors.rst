############
Process data
############

.. highlight:: html+django

You might want to compress your javascript and or css files you use with
sekizai. Since the ``render_block`` tag cannot be in a block tag (like the
``compress`` tag from django_compressor), it accepts an optional list of
processor functions to process the data. You can specify the processors using
import paths pointing to your callable, for example to call the function ``foo``
in the package ``spam.eggs`` you use following tag::

    {% render_block "js" using "spam.eggs.foo" %}

.. highlight:: python

Your processor function must accept exactly one argument, the data in this
namespace, and return a string holding the processed data.

An example processor which removes newlines would be::

    def my_processor(data):
        return data.replace('\n', '')


******************
Builtin processors
******************

sekizai.contrib.django_compressor.css
=====================================

Compresses the CSS using `django_compressor`_ and merges them into a single
file. Requires django_compressor to be installed.


sekizai.contrib.django_compressor.js
====================================

Compresses the Javascript using `django_compressor`_ and merges them into a
single file. Requires django_compressor to be installed.