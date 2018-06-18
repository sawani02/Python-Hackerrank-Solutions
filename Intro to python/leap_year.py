# Challenge link: https://www.hackerrank.com/challenges/write-a-function/copy-from/54269250
def is_leap(year):
    leap = False
    
    # Logic for leap year
    if (year%4 == 0) and (year%100 != 0 or year%400 == 0) :
        leap = True
        return leap
    else:
        
        leap = False
        return leap
    
    
 
    
    return leap

is_leap(1990)
