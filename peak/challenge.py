#!/usr/bin/python3
from urllib import request
import pickle

if __name__ == "__main__":
    response = request.urlopen("http://www.pythonchallenge.com/pc/def/banner.p")
    mysterious_list = pickle.load(response)

    for sublist in mysterious_list:
        line = ''
        for word in sublist:
            line += word[0] * word[1]
        print(line)
