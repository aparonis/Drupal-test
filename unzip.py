import base64
import glob
import os

files = sorted([f for f in os.listdir("./pman")])

with open("pman.zip", "wb+") as pk:
    for f in files:
        with open("./pman/" + f, "rb") as inn:
            pk.write(inn.read())


