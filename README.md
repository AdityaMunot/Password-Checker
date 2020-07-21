# Password Validator

[![build status of master](https://travis-ci.org/AdityaMunot/password_validator.svg?branch=master)](https://travis-ci.org/AdityaMunot/password_validator)

# Background
NIST recently updated their Digital Identity Guidelines in June 2017. The new guidelines specify general rules for handling the security of user supplied passwords. Previously passwords were suggested to have certain composition rules (special characters, numbers, etc.), hints and expiration times. Those have gone out the window and the new suggestions are as follows: Passwords MUST

1. Have an 8 character minimum
2. AT LEAST 64 character maximum
3. Only allow printable ASCII characters and spaces
4. Not be a common password

# Project
A program to detect if a password meets these requirements. 

1. Have at least 8 Character

2. Can have 64 character maximum

3. Allowed only ASCII characters

4. Check not a common password

Program takes a file of newline delimited common passwords to check if a password is in that file and print invalid passwords to the command line and print * for any unprintable character

# Requirement

OS - Linux

Software - Python 3.6+

# Installation - Production

```bash
$ git clone https://github.com/AdityaMunot/password_validator.git
$ bash install.sh
```

# Installation - Development

```bash
$ git clone https://github.com/AdityaMunot/password_validator.git
```

For use in Development:

* Open install.sh

* comment and uncomment the following way.

* ```bash
  # production setup #
  # pip3 install .
  
  # development setup #
  pip3 install -e .
  ```
  

This will reduce the hassle of keep installing the cli tool.

```bash
$ bash install.sh
```

# Usage

```bash
$ cat <path to input text file> | password_validator <path to common password text file>
```

#  Result 

```bash
$ cat test_file/input_passwords.txt | password_validator test_file/weak_password_list.txt
mom -> Error: Too Short
password1 -> Error: Too common
Bj**rk****oacute* -> Error: Invalid Charaters
pipi -> Error: Too Short
**** -> Error: Invalid Charaters
```

## Author

Managed by [Aditya Munot](https://github.com/AdityaMunot)