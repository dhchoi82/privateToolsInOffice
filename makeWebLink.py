import sys, os

if "__running__" not in os.listdir():
    with open("__running__","w") as check0:
        check0.write("This is the 1st running check file of 'makeWebLink.py'.")
    os.system('cmd /c "makeWebLink.py"')

check1 = open("__running__","r")
chkstr = check1.read()
if chkstr == "This is the 1st running check file of 'makeWebLink.py'.":
    check1.close()
    check2 = open("__running__","w")
    check2.write("This is the 2nd running check file of 'makeWebLink.py'.")
    check2.close()
elif chkstr == "This is the 2nd running check file of 'makeWebLink.py'.":
    check1.close()
    os.remove("__running__")
    sys.exit()
else:
    input('별도의 "__running__" 파일이 존재합니다.')
    sys.exit()

############################################################
### 아래의 url = "" 구문의 따옴표 안에 URL 주소를 써 넣으세요.###
############################################################

url = ""                                                   #

############################################################

if "webLink.html" in os.listdir():
    if input("webLink.html 파일이 존재합니다. 덮어쓸까요?(y/n):") != "y":
        sys.exit()

if len(sys.argv) != 1:
    url = sys.argv[1]
elif url == "":
    url = input("URL을 입력하세요:")

if url[:4] != "http":
    url = "http://" + url

with open("webLink.html","w") as linkFile:
    linkFile.write(
"""<!DOCTYPE HTML>
<html>
    <head>
        <meta http-equiv="refresh" content="0;url='{0}'" />
    </head>
</html>""".format(url)
    )
