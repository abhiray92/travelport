from urllib.request import urlopen, Request
import re
import os

def downloadAndSave():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
    reg_url = "https://www.irelandwestairport.com/flight_information"
    req = Request(url=reg_url, headers=headers)
    html = urlopen(req).read().decode('utf-8')
    p = re.compile(r"<(.*?)(src|href)=\"(?!http)(.*?)\"(.*?)>")
    updatedFileContents = p.sub(srcrepl, html)
    with open('index.html', 'r+') as fid:
        fid.write(updatedFileContents)

def srcrepl(match):
   "Return the file contents with paths replaced"
   absolutePath = "https://www.irelandwestairport.com" #update the URL to be prefixed here.
   print("<" + match.group(1) + match.group(2) + "=" + "\"" + absolutePath + match.group(3) + match.group(4) + "\"" + ">")
   return "<" + match.group(1) + match.group(2) + "=" + "\"" + absolutePath + match.group(3) + match.group(4) + "\"" + ">"

downloadAndSave()
