#!/usr/bin/python3

import codecs
import os
import sys
from tkinter import Tk, messagebox

text = ""

if os.path.exists("raw.txt")==False:
    root = Tk()
    root.withdraw()
    if messagebox.askyesno(message="raw.txt 파일이 없습니다.\nraw.txt 파일을 만드시겠습니까?"):
        with codecs.open("raw.txt","w",encoding="utf8") as f:
            f.write(text)
    
    sys.exit("You need lines in raw.txt.")

with codecs.open("raw.txt","r",encoding="utf8") as f:
    text = f.read()
    
textList = text.split("\n")
textList.sort()
text = "\n".join(textList)

with codecs.open("sort.txt","w",encoding="utf8") as f:
    f.write(text)
