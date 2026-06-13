# test_coinmap.py
"""
Tests for CoinMap module.
"""

import unittest
from coinmap import CoinMap

class TestCoinMap(unittest.TestCase):
    """Test cases for CoinMap class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CoinMap()
        self.assertIsInstance(instance, CoinMap)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CoinMap()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
