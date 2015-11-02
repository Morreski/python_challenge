#!/usr/bin/python3
from string import ascii_lowercase, ascii_uppercase
from collections import deque

INPUT_TEXT = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."


def apply_padding(text, n):
    """Shift letters by a gap of n. It is case-sensitive"""
    for charset in (ascii_uppercase, ascii_lowercase):

        outtab = deque(charset)
        outtab.rotate(n)

        trans_dir = str.maketrans("".join(charset), "".join(outtab))

        text = text.translate(trans_dir)

    return text


if __name__ == "__main__":

    OUTPUT_TEXT = apply_padding(INPUT_TEXT, -2)
    print(OUTPUT_TEXT)
