#!/usr/bin/python2.7
import sys
import requests
import datetime
import time
import ftplib
import os



import urllib
import urllib2


url = 'http://www.blog.pythonlibrary.org/wp-content/uploads/2012/06/wxDbViewer.zip'

print "downloading with urllib"
urllib.urlretrieve(url, "code.zip")

print "downloading with urllib2"
f = urllib2.urlopen(url)
data = f.read()
with open("code2.zip", "wb") as code:
    code.write(data)



li = ['|','/', '-', '\\']
idx=0

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

today = datetime.date.today()
old = today - datetime.timedelta(+90)
print 'the date is {0} and 90 days ago was {1}'.format(today, old)


'''url='https://www.sample-videos.com/img/Sample-jpg-image-30mb.jpg'
g=requests.get(url, headers={'Connection': 'close'}, verify=False)
print g.headers['content-type']
'''

file_name = "code.zip"
with open(file_name, "wb") as f:
        print "Downloading %s" % file_name
        response = requests.get(url, stream=True)
        total_length = response.headers.get('content-length')
        print total_length
        if total_length is None: # no content length header
            f.write(response.content)
        else:
            dl = 0
            total_length = int(total_length)
            for data in response.iter_content(chunk_size=50000):
                dl += len(data)
                f.write(data)
                done = int(50 * dl / total_length)
                #time.sleep(.1)
                thiselem = li[idx]
                idx = (idx + 1) % len(li)
                nextelem = li[idx]
                sys.stdout.write("\rDownloading... %s" %(thiselem))
                #sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50-done)) )

        sys.stdout.write("\rDownload Complete")
        sys.stdout.flush()



session = ftplib.FTP('ftp.dlptest.com')
session.login('dlpuser@dlptest.com', 'eiTqR7EMZD5zy7M')
session.mkd('abc/')
file = open('download.html','rb')                  # file to send
session.storbinary('STOR abc/download.html', file)     # send the file
file.close()                                    # close file and FTP
session.quit()



#https://stackoverflow.com/questions/2028517/python-urllib2-progress-hook
