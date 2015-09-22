__author__ = 'sherpa'
import urllib2
import re
def main():
    webUrl = urllib2.urlopen("http://money.cnn.com/services/speakup/speakup.html")
    print "result code: " + str(webUrl.getcode())
    data = webUrl.read()
   # print type(data)
   # print type(webUrl)
    emails = re.findall(r'[\w\.-]+@[\w\.-]+',data)
    for email in emails:
        print email

if __name__ == "__main__":
    main()
