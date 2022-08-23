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

    def test_class(self):
        pass

    def test_function(self):
        pass
