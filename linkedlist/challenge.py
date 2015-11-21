#!/usr/bin/python3
from urllib import request


def get_next_number(n):
    url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s"
    response = request.urlopen(url % n).read().decode("utf-8")
    number = response.split()[-1]
    return number

if __name__ == "__main__":
    number = 12345
    for _ in range(400):
        number = get_next_number(number)
        try:
            int(number)
        except ValueError:
            print(number)
