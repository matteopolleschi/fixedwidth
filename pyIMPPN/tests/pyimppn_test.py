#!/usr/bin/env python

"""
Tests for the pyIMPPN function.
"""

import unittest
from ..pyimppn import imppn_line

class TestIMPPN(unittest.TestCase):
    """
    Test of the FixedWidth class.
    """

    def test_basic(self):
        """
        Test a simple, valid example.
        """
        result_string = imppn_line(TRF_DITTA="7")
        good = ("""
        7


        """)

        self.assertEquals(result_string, good)