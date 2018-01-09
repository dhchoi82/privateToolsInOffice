#!/usr/bin/python3

import codecs
import os
import sys
from tkinter import Tk, messagebox

text = "Sample\r\n123456\r\n가나다\r\nㅋㅋㅋ\r\nabc\r\nzzz\r\n아저씨"

if os.path.exists("raw.txt")==False:
    root = Tk()
    root.withdraw()
    if messagebox.askyesno(message="raw.txt 파일이 없습니다.\nraw.txt 파일을 만드시겠습니까?"):
        with codecs.open("raw.txt","w",encoding="utf-8-sig") as f:
            f.write(text)
    
    sys.exit("You need lines in raw.txt.")

with codecs.open("raw.txt","r",encoding="utf-8-sig") as f:
    text = f.read()
    
textList = text.split("\r\n")
textList.sort()
text = "\r\n".join(textList)

with codecs.open("sort.txt","w",encoding="utf-8-sig") as f:
    f.write(text)
