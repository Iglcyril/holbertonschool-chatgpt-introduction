#!/usr/bin/python3
import sys
# we work with an array of string, in ther first case of this array there are the name of the script
# so we start from index 1 to print only the arguments passed to the script
for i in range(1, len(sys.argv)):
    print(sys.argv[i])