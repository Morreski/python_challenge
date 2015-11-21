#!/usr/bin/python3
import subprocess

if __name__ == "__main__":
    proc = subprocess.Popen(["python3", "channel/challenge.py"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    answer_from_channel = proc.communicate()[0].decode("utf-8")

    seen_letters = []
    for char in answer_from_channel:
        if char in seen_letters:
            continue
        seen_letters.append(char)

    print("".join(seen_letters))
