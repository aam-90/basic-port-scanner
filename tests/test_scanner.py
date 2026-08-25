import unittest

from scanner.validators import (
    validate_ports,
    validate_timeout
)


class TestValidators(unittest.TestCase):

    def test_valid_ports(self):
        validate_ports(1, 20)

    def test_invalid_start_port(self):
        with self.assertRaises(ValueError):
            validate_ports(0, 20)

    def test_invalid_end_port(self):
        with self.assertRaises(ValueError):
            validate_ports(1, 70000)

    def test_reversed_ports(self):
        with self.assertRaises(ValueError):
            validate_ports(20, 1)

    def test_valid_timeout(self):
        validate_timeout(1)

    def test_invalid_timeout(self):
        with self.assertRaises(ValueError):
            validate_timeout(0)


if __name__ == "__main__":
    unittest.main()