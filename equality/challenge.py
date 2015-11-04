#!/usr/bin/python3

from urllib import request
import re

if __name__ == "__main__":

    response = request.urlopen("http://www.pythonchallenge.com/pc/def/equality.html")
    html = response.read().decode("utf-8").split("<!--")[-1]

    regex = re.compile("(?<![A-Z])[A-Z]{3}[a-z][A-Z]{3}(?![A-Z])")

    matches = regex.findall(html)

    print("".join([match[3] for match in matches]))

    for match in matches:
        small = match[3]
