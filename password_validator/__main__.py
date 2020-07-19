import sys
from .filereader import file_reader

def main():
    
    args = sys.argv[1:]
    weak_password = file_reader(args[0])

    for line in sys.stdin:
        npass = ""
        line = line.strip()
        for n, ch in enumerate(line):
            if ord(ch) > 31 and ord(ch) < 127:
                npass = npass + ch
            else:
                npass = npass + "*"
        if(n < 7):
            print(npass+" -> Error: Too Short")
        
        if(n > 63):
            print(npass+" -> Error: Too Long")

        if(line in weak_password):
            print(npass+" -> Error: Too common")

        if('*' in npass):
            print(npass+" -> Error: Invalid Charaters")
        


if __name__ == '__main__':
    main()