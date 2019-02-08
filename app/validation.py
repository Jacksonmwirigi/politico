from flask import Flask, request
import re

class Validations:
    
    def is_url_image(self, image_url):
        image_formats = ("image/png", "image/jpeg", "image/jpg")
        r = request.head(image_url)
        if r.headers["content-type"] in image_formats:
            return True
        return False


    def is_valid_string(self, x):
        self. x= x
    # input_str = raw_input("Please provide some info: ")
        if not re.match("^[a-z]*$", x):
            return x
        else:    
            return False  
