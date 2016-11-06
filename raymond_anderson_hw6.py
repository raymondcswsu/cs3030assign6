#!/usr/bin/env python3
import sys
from urllib.request import urlopen

def help():
    """
    Inform user of parameters of program
    """
    print("Usage is: python3 raymond_anderson_hw6.py <file Input>")
    return

def main(link):
    """
    Returns top 25 errors from an error log 
    Args:
        link:
            The link to the error log
    """
    with urlopen(link) as data:
        errors = []
        for line in data:
            
            sections = line.decode('utf-8').split(']')
        
            newSections = sections[-1].split(',')
            
            errors.append(newSections[0])
               
            
        #print(errors)
        errors.sort()
        i = 0
        numErrors = []
        while errors[i] != errors[-1]:
             
            numErrors.append((errors.count(errors[i]),errors[i]))
            i += errors.count(errors[i])
        
        numErrors.sort(reverse=True)
        errors=[]
        for i in range(25):
            errors.append(numErrors[i])

        print("*** Top 25 page errors ***")

        for error in errors:
            print("Count: " + str(error[0]) + " Error: " + error[-1])

        
                
    return


if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
        exit(0)
    else:
        help()
        exit(1)
    


