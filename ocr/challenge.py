#!/usr/bin/python3

from urllib import request
from string import ascii_letters

if __name__ == "__main__":

    response = request.urlopen("http://www.pythonchallenge.com/pc/def/ocr.html")
    html = response.read().decode("utf-8").split("below")[-1]

    seeking_chars = list(ascii_letters) + [" ", ".", "'"]

    found_chars = [c for c in html if c in seeking_chars]

    print("".join(found_chars))
