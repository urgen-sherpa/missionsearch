#!/usr/bin/python
#author: urgen sherpa
#To write this to file
from bs4 import BeautifulSoup
import requests
mylist = []
response = requests.get('http://www.standalone-sysadmin.com/blog/')
soup = BeautifulSoup(response.content)

for link in soup.find_all("a"):
    mylist.append(str(link.get("href")))

with open("linksfile.txt", "a+") as filehandler_for_linkout:
    for link in mylist:
        filehandler_for_linkout.write(link+"\r\n")
