#####################
Templatetag reference
#####################


**********
addtoblock
**********

Syntax:: ``{% addtoblock <namespace> %}...{% endaddtoblock [<namespace>] %}``

Adds it's contents to the specified namespace.


************
render_block
************

Syntax: ``{% render_block <namespace> [using "<processor1>" ["<processor2>" [...]]] %}``

Renders the specified namespace, optionally processing the data before
displaying it.

Processors must be import paths of the format
``"mypackage.mymodule.mycallable"`` and are not resolved against the context.


********
add_data
********

Syntax: ``{% add_data <namespace> <data> %}``

Adds a bit of data to the specified namespace.


*********
with_data
*********

Syntax: ``{% with_data <namespace> as <varname> %}...{% end_with_data %}``

Renders it's contents with the data from the specified namespace in the variable
specified.