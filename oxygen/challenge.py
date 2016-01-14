#!/usr/bin/python3

from urllib import request
from PIL import Image
from io import BytesIO

if __name__ == "__main__":

    r = request.urlopen("http://www.pythonchallenge.com/pc/def/oxygen.png").read()

#   Ok, that one was a bit tough so i'll explain the way i solved it.
#   I first assumed that an info was encoded in the image, possibly one character by gray squares.
#   Gray can be obtained by settings all RGB bytes to the same value, so i wrote this:
    b = BytesIO()
    b.write(r)
    b.seek(0)
    img = Image.open(b)

    grays = [data[0] for data in img.getdata() if data[0] == data[1] == data[2]]
#   Ok seems there is a pattern in those data: blocks of 8 identical values.
#   With a closer look to the image, it seems that squares are 7 pixels wide
#   Let's decode what we have

#   But first, we should keep only one value for each block.

    chars = [chr(p) for p in grays]

    unique_chars = []
    for i, c in enumerate(chars):
        if i % 7 != 0:
            continue

        unique_chars.append(c)

#   Seems there is something in this list that says "smart guy, you made it..."
#   There is a plain text python list at the end

#   Now we need to decode what's in the encoded list:
    plain_list = unique_chars[74:117]
    print(plain_list)

    print("".join([chr(x) for x in [105, 110, 116, 101, 103, 114, 105, 116, 121]]))
