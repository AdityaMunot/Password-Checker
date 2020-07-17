from setuptools import setup
setup(
    name = 'password_validator',
    version = '0.1.0',
    packages = ['password_validator'],
    entry_points = {
        'console_scripts': [
            'password_validator = password_validator.__main__:main'
        ]
    })