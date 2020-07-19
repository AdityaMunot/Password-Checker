import unittest
import os

class password_validator_test(unittest.TestCase):

    def test_entrypoint(self):
        exit_status = os.system('password_validator --help')
        assert exit_status == 0

if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)