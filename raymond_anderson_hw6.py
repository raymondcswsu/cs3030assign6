#!/usr/bin/env python3
import sys
from urllib.request import urlopen

def main():
    link="http://icarus.cs.weber.edu/~hvalle/cs3030/data/error.log.test"
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

        for error in numErrors:
            print("Count: " + str(error[0]) + " Page: " + error[-1])
                
                

        

            
            
            
            
            
            
            
        
                        

    return


if __name__ == '__main__':
    main()
    exit(0)


