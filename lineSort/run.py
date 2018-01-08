import codecs

text = ""

with codecs.open("raw.txt","r",encoding="utf8") as f:
    text = f.read()
    
textList = text.split("\n")
textList.sort()
text = "\n".join(textList)

with codecs.open("sort.txt","w",encoding="utf8") as f:
    f.write(text)
