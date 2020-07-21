import unittest
import os
import subprocess
from password_validator.filereader import file_reader


class password_validator_test(unittest.TestCase):

    def test_entrypoint(self):
        exit_status = os.system('password_validator --help')
        assert exit_status == 0

    def test_filereader(self):
        read_data = file_reader("test_file/input_passwords.txt")
        test_data = ["mom","password1","Bj��rk����oacute�","pipi","भारत"]
        self.assertEqual(test_data,read_data)

    def test_toolcli(self):
        output = [subprocess.check_output("cat test_file/input_passwords.txt | password_validator test_file/weak_password_list.txt", shell=True)]
        result = [b"mom -> Error: Too Short\npassword1 -> Error: Too common\nBj**rk****oacute* -> Error: Invalid Charaters\npipi -> Error: Too Short\n**** -> Error: Invalid Charaters\n"]
        self.assertEqual(result,output)

if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)