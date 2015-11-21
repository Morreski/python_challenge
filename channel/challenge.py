#!/usr/bin/python3

from urllib import request
from zipfile import ZipFile
from tempfile import TemporaryFile


if __name__ == "__main__":
    zip_url = "http://www.pythonchallenge.com/pc/def/channel.zip"
    zip_bytes = request.urlopen(zip_url).read()

    # Wrap bytes inside a temporaryfile
    t = TemporaryFile()
    t.write(zip_bytes)

    zf = ZipFile(t)

    # Get number according to hints found in readme.txt
    file_name = "90052.txt"
    comment_list = []
    while True:
        file_content = zf.read(file_name).decode("utf-8")
        comment = zf.getinfo(file_name).comment.decode("utf-8")
        comment_list.append(comment)
        try:
            # if last word is not an int, we can stop.
            int(file_content.split()[-1])
            file_name = file_content.split()[-1] + ".txt"
        except ValueError:
            print("".join(comment_list))
            break
