import sys
import argparse
import os
from password_validator.filereader import file_reader

def main():

    my_parser = argparse.ArgumentParser(prog="password_validator", description="")
    my_parser.add_argument('Path', metavar='path', type=str, help='the path to common passwords file')
    args = my_parser.parse_args()

    path = args.Path

    if not os.path.isfile(path):
        print('The file specified does not exist')
        sys.exit()

    weak_password = file_reader(path)

    for line in sys.stdin:
        npass = ""
        line = line.strip()
        
        for n, ch in enumerate(line):
            if ord(ch) > 31 and ord(ch) < 127:
                npass = npass + ch
            else:
                npass = npass + "*"

        if('*' in npass):
            print(npass+" -> Error: Invalid Charaters")
            continue

        if(n < 7):
            print(npass+" -> Error: Too Short")
            continue

        if(n > 63):
            print(npass+" -> Error: Too Long")
            continue

        if(line in weak_password):
            print(npass+" -> Error: Too common")
            continue

if __name__ == '__main__':
    main()