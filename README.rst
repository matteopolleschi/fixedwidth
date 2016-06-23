Test script:
python -m pyIMPPN.tests.pyimppn_test

Easy two-way conversion between Python dictionaries and fixed-width files.
The FixedWidth class has been used in production without modification for 
several years.

This module has also proven useful for "debugging" a fixed-width spec --
an invalid configuration reports an error that may not be obvious from
reading the spec document.



Notes:

#.  A field must have a start_pos and either an end_pos or a length.
    If both an end_pos and a length are provided, they must not conflict.

#.  A field may not have a default value if it is required.

#.  Supported types are string, integer, and decimal.

#.  Alignment and padding are required.

