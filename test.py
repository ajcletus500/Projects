#!/usr/bin/python2.7
import sys
import requests
import datetime
import time
import ftplib
import os


from requests.packages.urllib3.exceptions import InsecureRequestWarning

li = ['|', '/', '-', '\\']
idx=0

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

today = datetime.date.today()
old = today - datetime.timedelta(+90)
print 'the date is {0} and 90 days ago was {1}'.format(today, old)


url='http://www.peoplelikeus.org/piccies/codpaste/codpaste-teachingpack.pdf'
g=requests.get(url, headers={'Connection': 'close'}, verify=False)
print g.headers['content-type']


file_name = "download.html"
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
