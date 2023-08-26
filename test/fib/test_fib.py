"""test fib implementation."""

import unittest
import logging
import sys
from fibonacci.fib import fib


class FibTest(unittest.TestCase):
    """Class FibTest."""

    def setUp(self):
        """setUp."""
        debug = True
        self.fib = fib.Fib()

        if debug:
            logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
            self.log = logging.getLogger("FibTestLog")

    def test_example_class(self):
        """Example test of the fibonacci class."""
        self.assertEqual(self.fib.get_fib(1), 1)

    def test_example_function(self):
        """Example test of the fibonacci function."""
        self.assertEqual(fib.calculate_fib(1), 1)
