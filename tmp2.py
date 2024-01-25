import sys

argc = len(sys.argv)

if argc != 2:
    sys.exit('Incorrect Number of command line arguments')

x = sys.argv[0]
print(x)