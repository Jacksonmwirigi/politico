import re
import datetime
from datetime import datetime
from flask import Flask, jsonify, make_response, request

VALID_IMAGE_EXTENSIONS = [
    """"List of valid image exstensions"""
    ".jpg",
    ".jpeg",
    ".png",
    ".gif",
]


def check_no_digits(word):
    """checks for valid string """
    """Checks for characters , name should not have digits """
    if word.isdigit:
        return "Only String expected "
    else:
        pass


def valid_url_extension(url, extension_list=VALID_IMAGE_EXTENSIONS):
    """Validates logo url for valid image extensions"""
    return any([url.endswith(e)
                for e in extension_list])


def is_office_key_correct(request):
    """Checks for correct keys in the request """
    my_keys = ['name', 'candidate_id', 'date_created']
    error = []
    for key in my_keys:
        if not key in request.json:
            error.append(key)

    return error
def is_party_key_correct(request):
    """Checks for correct keys in the request """
    my_keys = ['name', 'hqAddress', 'logoUrl']
    error = []
    for key in my_keys:
        if not key in request.json:
            error.append(key)

    return error    


def check_valid_date(date_text):
    """Validating date input """
    #user_input = input('Enter the date in mm/dd/yyyy format: ')
    try:
        if datetime.strptime(date_text, '%m/%d/%Y'):
            return date_text
            
    except ValueError:
        return print('The date {} is invalid'.format(date_text))
