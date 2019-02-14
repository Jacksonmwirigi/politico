import re
import datetime
import urllib.request as req
from urllib.request import urlopen, URLError
import urllib.parse as p
from datetime import datetime
from flask import Flask, jsonify, make_response, request

VALID_IMAGE_EXTENSIONS = [
    """"List of valid image exstensions"""
    ".jpg",
    ".jpeg",
    ".png",
    ".gif",
]


def valid_url_extension(url, extension_list=VALID_IMAGE_EXTENSIONS):
    """Validates logo url for valid image extensions"""
    return any([url.endswith(e)
                for e in extension_list])


def is_office_key_correct(request):
    """Checks for correct keys in the request """
    my_keys = ['office_name', 'office_type']
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


def page_not_found(error):
    return make_response(jsonify({
        "status": "not found",
        "message": "url not found",
        "error": 404

    }), 404)


def internal_server_error(error):
    return make_response(jsonify({
        "status": "serevr error",
        "message": "server not responding",
        "error": 500
    }), 500)


def bad_request(error):
    return make_response(jsonify({
        "status": "bad request",
        "message": "url not found",
        "error": 400
    }), 400)


def method_not_allowed(error):
    return make_response(jsonify({
        "status": 405,
        "message": "Method Not allowed"
    }), 405)
